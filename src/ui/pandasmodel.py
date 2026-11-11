#!/usr/bin/env python3
"""
Created on Fri Nov  7 13:51:06 2025

@author: tcoustillet
"""

import pandas as pd
from PySide6.QtCore import QAbstractTableModel, Qt

# Column names of the loaded data.
FRAME_COLUMN = "Frame"
SIGNAL_COLUMN = "F/F0"
REQUIRED_COLUMNS = [FRAME_COLUMN, SIGNAL_COLUMN]


class PandasModel(QAbstractTableModel):
    """Table model for hosting pandas dataframes in a Qt view.

    Adapts a DataFrame to the model/view framework so that it can be displayed
    in a QTableView. Numeric values are rounded for display and all cells are
    centered.

    Attributes:
    -----------
        unprocessed_data (pd.DataFrame): The DataFrame displayed by the model.
    """

    def __init__(self, unprocessed_data=None, parent=None):
        """Initialize the model.

        Args:
        -----
            unprocessed_data (pd.DataFrame): The data to display. Usally a
            two-column table: "Frame" and "F/F0". Defaults to None.
            parent (QObject, optional): The parent Qt object. Defaults to None.
        """

        super().__init__(parent)
        self.unprocessed_data = (
            pd.DataFrame() if unprocessed_data is None else unprocessed_data
        )

    def rowCount(self, parent=None):
        """Return the number of rows in the model."""
        return self.unprocessed_data.shape[0]

    def columnCount(self, parent=None):
        """Return the number of columns in the model."""
        return self.unprocessed_data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        """Return the data stored for a given cell and role.

        For the display role, numeric values are rounded to 6 decimals;
        non-numeric values are returned unchanged. For the text alignment
        role, cells are centered.

        Args:
        -----
            index (QModelIndex): The position of the cell.
            role (Qt.ItemDataRole, optional): The requested data role.
                Defaults to Qt.DisplayRole.

        Returns:
        --------
            The value to display (float or any), the alignment flag, or
            None if the index is invalid or the role is not handled.
        """
        if index.isValid():
            if role == Qt.DisplayRole:
                value = self.unprocessed_data.iloc[index.row(), index.column()]
                try:
                    return round(float(value), 6)
                except (ValueError, TypeError):
                    return value
            elif role == Qt.TextAlignmentRole:
                return Qt.AlignCenter
            return None
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Return the header label for a given row or column.

        Horizontal headers show the column names; vertical headers show
        the DataFrame index.

        Args:
        -----
            section (int): The row or column number.
            orientation (Qt.Orientation): Qt.Horizontal or Qt.Vertical.
            role (Qt.ItemDataRole, optional): The requested data role.
                Defaults to Qt.DisplayRole.

        Returns:
        --------
            str or None: The header label, or None if the role is not
            Qt.DisplayRole.
        """
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.unprocessed_data.columns[section]
            if orientation == Qt.Vertical:
                return str(self.unprocessed_data.index[section])
        return None


def load_data(data_path):
    """Load the table with the two columns of interest.

    Reads an Excel file and keeps only the "Frame" and "F/F0" columns.

    Args:
    -----
        data_path (str): Path to the Excel file (.xlsx).

    Returns:
    --------
        pd.DataFrame: A DataFrame with the columns "Frame" and "F/F0".

    Raises:
    -------
        ValueError: If a required column is missing.
        OSError: If the file cannot be opened.
    """
    data = pd.read_excel(data_path)

    missing = [col for col in REQUIRED_COLUMNS if col not in data.columns]
    if missing:
        raise ValueError(
            "The file must contain at least the columns: "
            f"{', '.join(REQUIRED_COLUMNS)}.\n"
            f"Missing: {', '.join(missing)}."
        )

    return data[REQUIRED_COLUMNS]
