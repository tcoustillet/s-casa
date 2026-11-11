#!/usr/bin/env python3
"""
Created on Fri Nov  7 13:41:33 2025

@author: CoustilletT
"""

import os

import numpy as np
from PySide6.QtCore import QEvent
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
)

from .. import signal_processing as sp
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
        n_frames (int): Number of frames (rows) of the loaded data.
        signal_duration (float): Total signal duration in seconds.
        peaks (np.ndarray): Indices of the last detected peaks. None until
            a refresh has been done on loaded data.
        prominences (np.ndarray): Prominence of each peak in `peaks`.
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
        self.n_frames = 0
        self.signal_duration = 0.0

        # Signal attributes
        self.peaks = None
        self.prominences = None

        # Connect main buttons.
        self.browseButton.clicked.connect(self.open_raw_data)

        self.plotprocessedWidget.setBackground("w")
        self.plotButton.clicked.connect(self.refresh)

        # Enable drag and drop.
        self.setAcceptDrops(True)

        # Handle line edit events.
        QApplication.instance().installEventFilter(self)

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

    def eventFilter(self, watched, event):
        """Validate the frame interval when clicking outside the line edit.

        Args:
        -----
            watched (QObject): The object receiving the event.
            event (QEvent): The event.

        Returns:
            bool: Always False, so the event is still processed normally.
        """
        if (
            event.type() == QEvent.MouseButtonPress
            and self.frameIntervalLineEdit.hasFocus()
            and watched is not self.frameIntervalLineEdit
        ):
            self.frameIntervalLineEdit.clearFocus()
        return super().eventFilter(watched, event)

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
        text = self.frameIntervalLineEdit.text()
        return int(text) if text else None

    def _on_frame_interval_changed(self):
        """Recompute the total signal duration."""
        self._update_signal_duration()
        self.update_signal_statistics()

    def _update_signal_duration(self):
        """Update duration label (number of frames x frame interval / 1000)."""
        # Get signal duration and convert into seconds.
        interval = self._get_frame_interval()

        if interval is None or self.n_frames == 0:
            self.signal_duration = 0.0
            self.durationSignalLabel.setText(
                "<b>Signal total duration =</b> -"
            )
            return

        # Convert milliseconds into seconds.
        self.signal_duration = interval * self.n_frames
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

        self.peaks = None
        self.prominences = None

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

        # Draw the new signal right away.
        self.refresh()

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
        detrend_type = (
            self.detrendComboBox.currentText()
            if self.detrendCheckBox.isChecked()
            else None
        )

        return sp.preprocess(self.raw_data["F/F0"].values, detrend_type)

    def plot_data(self, signal):
        """Plot the signal and the peaks of the last detection.

        Args:
        -----
            signal (np.ndarray): Signal on which the peaks were detected.
        """
        # Update plot.
        plotm.plot(
            plotWidget=self.plotprocessedWidget,
            x=self.raw_data["Frame"].values,
            y=signal,
            peaks=self.peaks,
            prominences=self.prominences,
            show_prominence=self.prominenceCheckBox.isChecked(),
        )

    def refresh(self):
        """Detect peaks once, then update the plot and the labels."""
        if self.raw_data is None:
            return

        signal = self._get_signal()

        self.peaks, self.prominences = sp.detect_peaks(
            signal, **self._get_current_parameters()
        )

        self.plot_data(signal)
        self.update_signal_statistics()

    def update_signal_statistics(self):
        """Update the mean amplitude and frequency labels.

        Values are only displayed if prominence display is enabled and at
        least one peak was detected and the signal duration is known.
        """
        n_peaks = 0 if self.peaks is None else len(self.peaks)

        if (
            self.prominenceCheckBox.isChecked()
            and n_peaks > 0
            and self.signal_duration > 0
        ):
            self.amplitudeLabel.setText(
                f"Mean amplitude = {np.mean(self.prominences):.3g} ± "
                f"{np.std(self.prominences):.3g}"
            )
            self.frequenceLabel.setText(
                f"Frequency = {n_peaks / self.signal_duration:.3g} Hz "
                f"(s<sup>-1</sup>) ({n_peaks} ÷ {self.signal_duration})"
            )
        else:
            self.amplitudeLabel.setText("Mean amplitude = ???")
            self.frequenceLabel.setText("Frequency = ???")
