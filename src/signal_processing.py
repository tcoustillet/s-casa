#!/usr/bin/env python3
"""
Created on Wed Nov  11 10:10:59 2026

@author: tcoustillet

Signal processing helpers, independent of the GUI.
"""

import numpy as np
from scipy.signal import detrend, find_peaks, peak_prominences


def preprocess(signal, detrend_type=None):
    """Return the signal, detrended if requested (original mean kept).

    Args:
    -----
        signal (np.ndarray): Raw signal.
        detrend_type (str or None): "linear" or "constant". If None, the
            signal is returned unchanged.
    """

    if detrend_type is None:
        return signal

    return detrend(signal, type=detrend_type) + np.mean(signal)


def detect_peaks(signal, **params):
    """Detect peaks with `scipy.signal.find_peaks`.

    Prominences are always computed, whatever the parameters, so that
    callers can rely on them.

    Args:
    -----
        signal (np.ndarray): signal to analyse.
        **params: Keyword arguments forwarded to `find_peaks` (height,
            threshold, distance, prominence, width).

    Returns:
    --------
        tuple[np.ndarray, np.ndarray]: Indices of the detected peaks and
            their prominences.

    Note:
    -----
        For more details, please visit:
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html
    """

    peaks, _ = find_peaks(signal, **params)
    prominences = peak_prominences(signal, peaks)[0]
    return peaks, prominences
