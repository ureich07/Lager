#!/usr/
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
import pandas as pd
from datetime import datetime

class PandasModel(QAbstractTableModel):
    """A model to interface a Qt view with pandas dataframe """

    def __init__(self, dataframe: pd.DataFrame, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._dataframe = dataframe

    def rowCount(self, parent=QModelIndex()) -> int:
        """ Override method from QAbstractTableModel

        Return row count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe)

        return 0

    def columnCount(self, parent=QModelIndex()) -> int:
        """Override method from QAbstractTableModel

        Return column count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe.columns)
        return 0

    def data(self, index: QModelIndex, role=Qt.ItemDataRole):
        """Override method from QAbstractTableModel

        Return data cell from the pandas DataFrame
        """
        if not index.isValid():
            return None
        
        value = self._dataframe.iloc[index.row(), index.column()]
        if role == Qt.DisplayRole or role == Qt.EditRole:
            sReturn = str(value)
            if isinstance(value, float):
                sReturn = "%.2f" % value
            if isinstance(value, datetime):
                sReturn = value.strftime("%Y-%m-%d")
            return sReturn
            
        if role == Qt.TextAlignmentRole:
            if isinstance(value, int) or isinstance(value, float):
                return Qt.AlignVCenter + Qt.AlignRight
            if isinstance(value, str):
                return Qt.AlignLeft + Qt.AlignVCenter
        
        return None

    def headerData(self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole):
        """Override method from QAbstractTableModel

        Return dataframe index as vertical header data and columns as horizontal header data.
        """
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._dataframe.columns[section])

            if orientation == Qt.Vertical:
                return str(self._dataframe.index[section])
        return None
    
    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self._dataframe.iloc[index.row(), index.column()] = value
            return True
        return False
    
    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
    
    def removeRows(self, position, rows, parent=QModelIndex()):
        start, end = position, position + rows - 1
        if 0 <= start <= end and end < self.rowCount(parent):
            self.beginRemoveRows(parent, start, end)
            for index in range(start, end + 1):
                self._dataframe.drop(index, inplace=True)
            self._dataframe.reset_index(drop=True, inplace=True)
            self.endRemoveRows()
            return True
        return False
    
    def insertRows(self, position, rows, parent=QModelIndex()):
         start, end = position, position + rows - 1
         if 0 <= start <= end:
             self.beginInsertRows(parent, start, end)
             for index in range(start, end + 1):
                 default_row = [[None] for _ in range(self._dataframe.shape[1])]
                 new_df = pd.DataFrame(dict(zip(list(self._dataframe.columns), default_row)))
                 self._dataframe = pd.concat([self._dataframe, new_df])
             self._dataframe = self._dataframe.reset_index(drop=True)
             self.endInsertRows()
             return True
         return False