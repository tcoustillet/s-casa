#!/usr/bin/env python3
"""
Created on Fri Nov  7 14:13:08 2025

@author: tcoustillet
"""

import pyqtgraph as pg

pg.setConfigOptions(antialias=True)


def plot(plotWidget, x, y, peaks, prominences, show_prominence):
    """
    Plot a (calcium) signal together with its already detected peaks.

    args:
    -----
        plotWidget (pg.PlotWidget): PyQtGraph widget used to display the plot.
        x (array-like): X-axis values corresponding to the signal samples,
            usually "Frames".
        y (array-like): Y-axis values of the signal to be plotted,
            usually "F/F0".
        peaks (np.ndarray): Indices of the detected peaks.
        prominences (np.ndarray): Prominence of each detected peak.
        show_prominence (bool): If True, displays the prominence of each
            detected peak as a vertical orange line.

    Returns:
    --------
        None: The function updates the provided PlotWidget directly.
    """

    # Clear axis.
    plotWidget.clear()

    # Style.
    y1_pen = pg.mkPen(color="#1f77b4", width=2)
    peaks_pen = pg.mkPen(color="red", width=2)
    prominence_pen = pg.mkPen(color="darkorange", width=2)

    # Main plot (signal)
    plotWidget.plot(x, y, pen=y1_pen, name="data").setZValue(0)

    # Prominences, if any.
    if show_prominence:
        for peak, prominence in zip(peaks, prominences):
            line = pg.PlotDataItem(
                [x[peak], x[peak]],
                [y[peak] - prominence, y[peak]],
                pen=prominence_pen,
            )
            line.setZValue(1)
            plotWidget.addItem(line)

    # Top peaks.
    scatter_top_peaks = pg.ScatterPlotItem(
        x=x[peaks],
        y=y[peaks],
        size=6,
        symbol="x",
        pen=peaks_pen,
        name=f"n = {len(peaks)} detected peaks",
    )
    scatter_top_peaks.setZValue(2)
    plotWidget.addItem(scatter_top_peaks)

    # Customize plot
    plotWidget.showGrid(x=True, y=True)
    label_styles = {"color": "k", "font-size": "14px"}
    title_style = {"color": "k", "font-size": "18px"}
    plotWidget.setLabel("left", "data", **label_styles)
    plotWidget.setLabel("bottom", "# frame", **label_styles)
    plotWidget.setTitle(
        f"Number of detected peaks: {len(peaks)}", **title_style
    )
