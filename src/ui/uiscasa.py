#!/usr/bin/env python3
"""
Created on Fri Nov  7 13:41:33 2025

@author: CoustilletT
"""

import os

import numpy as np
from PySide6.QtGui import QIntValidator
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
        self.plotButton.clicked.connect(self.refresh)

        # Enable drag and drop.
        self.setAcceptDrops(True)

        # Connect sliders and spin boxes.
        self._connect_parameter_controls()

        # Connect frame interval line edit (must be an integer).
        self.frameIntervalLineEdit.setValidator(
            QIntValidator(1, 1_000_000, self)
        )
        self.frameIntervalLineEdit.editingFinished.connect(
            self.frameIntervalLineEdit.clearFocus
        )

        self.frameIntervalLineEdit.editingFinished.connect(
            self._on_frame_interval_changed
        )

        # Connect additional controls.
        self.setHeightPushButton.clicked.connect(self.set_height_value)
        self.detrendCheckBox.toggled.connect(self.refresh)
        self.detrendComboBox.currentIndexChanged.connect(self.refresh)
        self.prominenceCheckBox.toggled.connect(self.refresh)
        self._update_parameter_labels()

    def _update_frame_count_label(self):
        """Display the number of frames (rows) of the loaded data."""
        if self.raw_data is None:
            self.frameCountValue.setText("-")
            return

        self.frameCountValue.setText(f"{len(self.raw_data)}")
        self.n_frames = len(self.raw_data)
        self._update_signal_duration()

    def _get_frame_interval(self):
        """Return the frame interval as an int."""
        return int(self.frameIntervalLineEdit.text())

    def _on_frame_interval_changed(self):
        """Recompute the total signal duration."""
        self._update_signal_duration()
        self.update_signal_statistics()

    def _update_signal_duration(self):
        """Update duration label (number of frames x frame interval / 1000)."""
        # Get signal duration and convert into seconds.
        self.signal_duration = self._get_frame_interval() * self.n_frames
        self.signal_duration /= 1000

        self.durationSignalLabel.setText(
            f"<b>Signal total duration =</b> {self.signal_duration} s"
        )

    def _connect_parameter_controls(self):
        """Synchronize sliders, spin boxes and labels."""

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

            slider.valueChanged.connect(self._update_parameter_labels)
            spinbox.valueChanged.connect(self._update_parameter_labels)
            slider.valueChanged.connect(self.refresh)
            spinbox.valueChanged.connect(self.refresh)

    @staticmethod
    def _set_silently(widget, value):
        """Set a widget value without emitting its signals."""
        if isinstance(widget.value(), int):
            value = round(value)
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
                self._load_file(url.toLocalFile())
                break

    def open_raw_data(self):
        """Open a file dialog, then load and display the selected data.

        The dialog starts in the current working directory. Does nothing if
        the dialog is cancelled.
        """
        start_dir = os.getcwd()
        data_path, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select your file",
            dir=start_dir,
            filter="Calcium(*.xlsx);;All files(*)",
        )

        if data_path:
            self._load_file(data_path)

    def _load_file(self, path):
        """Load a data file and display its content.

        Fills the table view and updates the file name, mean and standard
        deviation labels. A warning is shown if the file cannot be read or
        does not contain the required columns.

        Args:
        -----
            path (str): Path to the .xlsx file.
        """
        try:
            data = pandasm.load_data(path)
        except (ValueError, OSError) as exc:
            QMessageBox.critical(self, "Error", str(exc))
            return

        signal = data["F/F0"].values

        self.raw_data = data
        self.unprocessed_model = pandasm.PandasModel(self.raw_data)

        # Update table.
        self.tableView.setModel(self.unprocessed_model)

        # Update filename.
        self.fileNameLabel.setText(
            f"<b>Loaded file:</b> {os.path.basename(path)}"
        )

        # Display the number of detected frames (rows).
        self._update_frame_count_label()

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

        self.durationSignalLabel.setText(
            f"<b>Signal total duration =</b> {self.signal_duration} s"
        )

    def set_height_value(self):
        """Set the height argument to the signal mean + standard deviation."""
        if self.mean_signal is None:
            return
        self.heightDoubleSpinBox.setValue(
            round(self.mean_signal + self.std_signal, 3)
        )

    def _get_current_parameters(self):
        """Return the current peak detection parameters as a dict."""
        return {
            "height": self.heightDoubleSpinBox.value(),
            "threshold": self.thresholdDoubleSpinBox.value(),
            "distance": self.distanceSpinBox.value(),
            "prominence": self.prominenceDoubleSpinBox.value(),
            "width": self.widthDoubleSpinBox.value(),
        }

    def _update_parameter_labels(self):
        """Display the current detection parameters next to their controls."""
        params = self._get_current_parameters()

        self.heightValue.setText(f"{params['height']:.3f}")
        self.thresholdValue.setText(f"{params['threshold']:.3f}")
        self.distanceValue.setText(f"{params['distance']}")
        self.prominenceValue.setText(f"{params['prominence']:.3f}")
        self.widthValue.setText(f"{params['width']:.3f}")

    def _get_signal(self):
        """Return the signal, detrended if requested (original mean kept)."""
        signal = self.raw_data["F/F0"].values

        if self.detrendCheckBox.isChecked():
            data = detrend(signal, type=self.detrendComboBox.currentText())
            # Preserve the original mean.
            data += np.mean(signal)
            return data

        return signal

    def plot_data(self):
        """Detect peaks with the current parameters and plot the result.

        Reads the detection parameters (height, threshold, distance,
        prominence, width) from the spin boxes, optionally detrends the
        signal, runs `scipy.signal.find_peaks` and updates the plot. The mean
        amplitude (mean prominence ± standard deviation) and the frequency
        labels are updated only if prominence display is enabled.
        """

        # Retrieve detection parameters.
        params = self._get_current_parameters()

        if self.raw_data is None:
            return

        data = self._get_signal()

        # Peak detection with the arguments stored in params.
        top_peaks, properties = find_peaks(x=data, **params)

        # Display prominence if requested.
        show_prominence = self.prominenceCheckBox.isChecked()

        # Update plot.
        plotm.plot(
            plotWidget=self.plotprocessedWidget,
            x=self.raw_data["Frame"].values,
            y=data,
            show_prominence=show_prominence,
            **params,
        )

    def refresh(self):
        """Update both the plot and the amplitude/frequency labels."""
        self.plot_data()
        self.update_signal_statistics()

    def update_signal_statistics(self):
        """Update the mean amplitude and frequency labels.

        Values are only displayed if prominence display is enabled and at
        least one peak was detected.
        """
        if self.raw_data is None:
            return

        top_peaks, properties = find_peaks(
            x=self._get_signal(), **self._get_current_parameters()
        )
        prominences = properties["prominences"]

        if self.prominenceCheckBox.isChecked() and len(prominences) > 0:
            self.amplitudeLabel.setText(
                f"Mean amplitude = {np.mean(prominences):.3g} ± "
                f"{np.std(prominences):.3g}"
            )
            self.frequenceLabel.setText(
                f"Frequency = {len(top_peaks) / self.signal_duration:.3g} Hz "
                f"(s<sup>-1</sup>) ({len(top_peaks)} ÷ {self.signal_duration})"
            )
        else:
            self.amplitudeLabel.setText("Mean amplitude = ???")
            self.frequenceLabel.setText("Frequency = ???")
