#!/usr/bin/env python3
"""
Created on Fri Nov  7 13:39:16 2025

Entry point of the application.

Creates the Qt application, instantiates the main window and starts the
event loop. Run it from the project root: `python scasa.py`.

@author: CoustilletT
"""

import sys

from PySide6.QtWidgets import QApplication

from src.ui.uiscasa import ScasaMainWindow

if __name__ == "__main__":
    scasaApp = QApplication(sys.argv)
    scasaWindow = ScasaMainWindow()
    scasaWindow.show()
    sys.exit(scasaApp.exec())
