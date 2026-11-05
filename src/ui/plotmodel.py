#!/usr/bin/env python3
"""
Created on Fri Nov  7 14:13:08 2025

@author: tcoustillet
"""

import pyqtgraph as pg
from scipy.signal import find_peaks

pg.setConfigOptions(antialias=True)


def plot(
    plotWidget,
    x,
    y,
    height,
    threshold,
    distance,
    prominence,
    width,
    show_prominence,
):
    """
    Plot a (calcium) signal and detect its peaks using scipy.signal.find_peaks.

    The function displays the input signal, identifies peaks according to
    the specified detection parameters, and optionally visualizes their
    prominence.

    args:
    -----
        plotWidget (pg.PlotWidget): PyQtGraph widget used to display the plot.
        x (array-like): X-axis values corresponding to the signal samples,
        usually "Frames".
        y (array-like): Y-axis values of the signal to be plotted,
        usually "F/F0".
        height (float or None): Minimum required height of a peak.
        threshold (float or None): Minimum vertical distance between a peak and
        its neighboring samples.
        distance (int or None): Minimum horizontal distance (in samples)
        between neighboring peaks.
        prominence (float or None): Minimum required prominence of a peak.
        width (float or None): Minimum required width of a peak.
        show_prominence (bool): If True, displays the prominence of each
        detected peak as a vertical orange line.

    Returns:
    --------
        None: The function updates the provided PlotWidget directly.

    Note:
    -----
        For more details, please visit:
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html
    """

    # Clear axis.
    plotWidget.clear()

    # Style.
    y1_pen = pg.mkPen(color="#1f77b4", width=2)
    peaks_pen = pg.mkPen(color="red", width=2)
    prominence_pen = pg.mkPen(color="darkorange", width=2)

    # Plots (signal + peaks)
    plotted_signal = plotWidget.plot(x, y, pen=y1_pen, name="data")

    if any(
        arg is not None
        for arg in (height, threshold, distance, prominence, width)
    ):
        top_peaks, properties = find_peaks(
            x=y,
            height=height,
            threshold=threshold,
            distance=distance,
            prominence=prominence,
            width=width,
        )
        scatter_top_peaks = pg.ScatterPlotItem(
            x=x[top_peaks],
            y=y[top_peaks],
            size=6,
            symbol="x",
            pen=peaks_pen,
            name=f"n = {len(top_peaks)} detected peaks)",
        )

        plotWidget.addItem(scatter_top_peaks)

    if show_prominence:
        for i, p in enumerate(top_peaks):
            ymin = y[p] - properties["prominences"][i]
            ymax = y[p]
            line = pg.PlotDataItem(
                [x[p], x[p]], [ymin, ymax], pen=prominence_pen
            )
            plotWidget.addItem(line)

    # Customize plot
    plotWidget.showGrid(x=True, y=True)
    label_styles = {"color": "k", "font-size": "14px"}
    title_style = {"color": "k", "font-size": "18px"}
    plotWidget.setLabel("left", "data", **label_styles)
    plotWidget.setLabel("bottom", "# frame", **label_styles)
    plotWidget.setTitle(
        f"Number of detected peaks: {len(top_peaks)}", **title_style
    )

    return None
