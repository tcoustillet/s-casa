#!/usr/bin/env python3
"""
Created on Fri Nov  7 13:41:33 2025

@author: CoustilletT
"""

import os

import numpy as np
from PySide6.QtWidgets import QFileDialog, QMainWindow, QMessageBox
from scipy.signal import detrend, find_peaks

from . import pandasmodel as pandasm
from . import plotmodel as plotm
from .ui_scasaMainWindow import Ui_MainWindow


class ScasaMainWindow(QMainWindow, Ui_MainWindow):
    """Main window hosting the widgets and the slots of the application.

    Attributes:
    -----------
        raw_data (pd.DataFrame): Loaded data with the columns "Frame" and
            "F/F0". Only defined once a file has been loaded.
        unprocessed_model (PandasModel): Table model displaying `raw_data`.
        mean_signal (float): Mean of the "F/F0" signal.
        std_signal (float): Standard deviation of the "F/F0" signal.
    """

    def __init__(self):
        """Set up the UI and connect all signals to their slots."""
        super().__init__()
        self.setupUi(self)

        # Initialize data attributes.
        self.raw_data = None
        self.unprocessed_model = None
        self.mean_signal = None
        self.std_signal = None

        # Connect main buttons.
        self.browseButton.clicked.connect(self.open_raw_data)

        self.plotprocessedWidget.setBackground("w")
        self.plotButton.clicked.connect(self.plot_data)

        # Enable drag and drop.
        self.setAcceptDrops(True)

        # Connect sliders and spin boxes.
        self._connect_parameter_controls()

        # Connect additional controls.
        self.setHeightPushButton.clicked.connect(self.set_height_value)
        self.detrendCheckBox.toggled.connect(self.plot_data)
        self.detrendComboBox.currentIndexChanged.connect(self.plot_data)
        self.prominenceCheckBox.toggled.connect(self.plot_data)

    def _connect_parameter_controls(self):
        """Synchronize sliders and spin boxes."""

        parameter_pairs = (
            (self.heightSlider, self.heightDoubleSpinBox, 1000),
            (self.thresholdSlider, self.thresholdDoubleSpinBox, 1000),
            (self.prominenceSlider, self.prominenceDoubleSpinBox, 1000),
            (self.widthSlider, self.widthDoubleSpinBox, 1000),
            (self.distanceSlider, self.distanceSpinBox, 1),
        )

        for slider, spinbox, scale in parameter_pairs:
            slider.valueChanged.connect(
                lambda value, box=spinbox, factor=scale: self._set_silently(
                    box, value / factor
                )
            )

            spinbox.valueChanged.connect(
                lambda value, bar=slider, factor=scale: self._set_silently(
                    bar, round(value * factor)
                )
            )

            slider.valueChanged.connect(self.plot_data)
            spinbox.valueChanged.connect(self.plot_data)

    @staticmethod
    def _set_silently(widget, value):
        """Set a widget value without emitting its signals."""
        widget.blockSignals(True)
        widget.setValue(value)
        widget.blockSignals(False)

    @staticmethod
    def _is_xlsx(url):
        """Return True if a QUrl points to a local .xlsx file."""
        return url.toLocalFile().lower().endswith(".xlsx")

    def dragEnterEvent(self, event):
        """Accept a drag only if it carries a .xlsx file.

        Args:
        -----
            event (QDragEnterEvent): The drag enter event.
        """
        if event.mimeData().hasUrls() and any(
            self._is_xlsx(url) for url in event.mimeData().urls()
        ):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        """Load the dropped .xlsx file.

        Args:
        -----
            event (QDropEvent): The drop event.
        """
        for url in event.mimeData().urls():
            if self._is_xlsx(url):
                self.open_dropped_data(url.toLocalFile())
                break

    def open_dropped_data(self, path):
        """Load a file dropped on the window and display its content.

        Fills the table view and updates the file name, mean and standard
        deviation labels. A warning is shown if the file cannot be loaded.

        Args:
        -----
            path (str): Path to the dropped .xlsx file.
        """
        try:
            data = pandasm.load_data(path)
            signal = data["F/F0"].values
        except Exception:
            QMessageBox.warning(
                self,
                "Error",
                "Unable to load the file.\nThe file must contain at least the "
                "columns: Frame and F/F0.",
            )
            return

        self.raw_data = data
        self.unprocessed_model = pandasm.PandasModel(self.raw_data)

        # Update table.
        self.tableView.setModel(self.unprocessed_model)

        # Update filename.
        self.fileNameLabel.setText(
            f"<b>Loaded file:</b> {os.path.basename(path)}"
        )

        # Update signal metrics.
        self.mean_signal = np.mean(signal)
        self.std_signal = np.std(signal)
        self.meanSignalLabel.setText(
            f"<b>Signal mean =</b> {self.mean_signal:.3f} "
            f"(exact value: {self.mean_signal:.10f})"
        )
        self.stdSignalLabel.setText(
            f"<b>Signal standard deviation =</b> {self.std_signal:.3f} "
            f"(exact value: {self.std_signal:.10f})"
        )

    def open_raw_data(self):
        """Open a file dialog, then load and display the selected data.

        The dialog starts in the current working directory. Fills the table
        view and updates the file name, mean and standard deviation labels.
        Does nothing if the dialog is cancelled.
        """
        start_dir = os.getcwd()
        data_path, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select your file",
            dir=start_dir,
            filter="Calcium(*.xlsx);;All files(*)",
        )

        if data_path:
            self.raw_data = pandasm.load_data(data_path)
            self.unprocessed_model = pandasm.PandasModel(self.raw_data)
            self.tableView.setModel(self.unprocessed_model)

            self.fileNameLabel.setText(
                f"<b>Loaded file:</b> {os.path.basename(data_path)}"
            )

            self.mean_signal = np.mean(self.raw_data["F/F0"].values)
            self.std_signal = np.std(self.raw_data["F/F0"].values)
            self.meanSignalLabel.setText(
                f"<b>Signal mean =</b> {self.mean_signal:.3f} "
                f"(exact value: {self.mean_signal:.10f})"
            )
            self.stdSignalLabel.setText(
                f"<b>Signal standard deviation =</b> {self.std_signal:.3f} "
                f"(exact value: {self.std_signal:.10f})"
            )

    def set_height_value(self):
        """Set the height argument to the signal mean + standard deviation."""
        if self.mean_signal is None:
            return
        self.heightDoubleSpinBox.setValue(
            round(self.mean_signal + self.std_signal, 3)
        )

    def plot_data(self):
        """Detect peaks with the current parameters and plot the result.

        Reads the detection parameters (height, threshold, distance,
        prominence, width) from the spin boxes, optionally detrends the
        signal, runs `scipy.signal.find_peaks` and updates the plot. The mean
        amplitude (mean prominence ± standard deviation) and the frequency
        labels are updated only if prominence display is enabled.
        """

        # Retrieve detection parameters.
        height = self.heightDoubleSpinBox.value()
        threshold = self.thresholdDoubleSpinBox.value()
        distance = self.distanceSpinBox.value()
        prominence = self.prominenceDoubleSpinBox.value()
        width = self.widthDoubleSpinBox.value()

        self.heightValue.setText(f"{height:.3f}")
        self.thresholdValue.setText(f"{threshold:.3f}")
        self.distanceValue.setText(f"{distance}")
        self.prominenceValue.setText(f"{prominence:.3f}")
        self.widthValue.setText(f"{width:.3f}")

        if self.raw_data is None:
            return

        # Signal detrend.
        if self.detrendCheckBox.isChecked():
            data = detrend(
                self.raw_data["F/F0"].values,
                type=self.detrendComboBox.currentText(),
            )
            # Preserve the original mean.
            data += np.mean(self.raw_data["F/F0"].values)
        else:
            data = self.raw_data["F/F0"].values

        # Peak detection.
        top_peaks, properties = find_peaks(
            x=data,
            height=height,
            threshold=threshold,
            distance=distance,
            prominence=prominence,
            width=width,
        )

        # Display prominence if requested.
        show_prominence = self.prominenceCheckBox.isChecked()

        # Update plot.
        plotm.plot(
            plotWidget=self.plotprocessedWidget,
            x=self.raw_data["Frame"].values,
            y=data,
            height=height,
            threshold=threshold,
            distance=distance,
            prominence=prominence,
            width=width,
            show_prominence=show_prominence,
        )

        # Update amplitude and frequency labels.
        prominences = properties["prominences"]
        if show_prominence and len(prominences) > 0:
            self.amplitudeLabel.setText(
                f"Mean amplitude = {np.mean(properties['prominences']):.3g} ± "
                f"{np.std(properties['prominences']):.3g}"
            )
            self.frequenceLabel.setText(
                f"Frequency = {len(top_peaks) / 150:.3g} Hz (s<sup>-1</sup>)"
            )
        else:
            self.amplitudeLabel.setText("Mean amplitude = ???")
            self.frequenceLabel.setText("Frequency = ???")
