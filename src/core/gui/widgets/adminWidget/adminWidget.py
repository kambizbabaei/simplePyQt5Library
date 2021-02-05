from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAbstractItemView, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

from modules.customQTwidgets.cQTableWidgetItem import cQTableWidgetItem
from utils.dbhelper import dbHelper
from core.gui.widgets.adminWidget.events import events


class adminTableWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.flag = True

        self.event_=events
        self.setTable()
        self.addItems()
        self.main = QVBoxLayout()
        self.setLayout(self.main)
        self.main.addWidget(self.__tablewidget_admins_)
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,QtWidgets.QSizePolicy.MinimumExpanding))

        
    def setTable(self):
        if self.flag:
            self.__tablewidget_admins_ :QTableWidget = QTableWidget(self)
        first_row_item = QTableWidgetItem("ADMINS")
        first_row_item.setFlags(QtCore.Qt.NoItemFlags)
        first_row_item_2= QTableWidgetItem("ACTIVE STATUS")
        first_row_item_2.setFlags(QtCore.Qt.NoItemFlags)
        self.__tablewidget_admins_.setRowCount(1)
        self.__tablewidget_admins_.setColumnCount(2)
        self.__tablewidget_admins_.setItem(0,0,first_row_item)
        self.__tablewidget_admins_.setItem(0,1,first_row_item_2)
        self.__tablewidget_admins_.horizontalHeader().setHidden(True)
        self.__tablewidget_admins_.setVerticalHeaderItem(0,QTableWidgetItem(" "))
        # self.__tablewidget_admins_.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.__tablewidget_admins_.setSelectionMode(QAbstractItemView.SingleSelection)
        self.__tablewidget_admins_.horizontalHeader().setSectionResizeMode(0,QtWidgets.QHeaderView.Stretch)
        self.__tablewidget_admins_.horizontalHeader().setSectionResizeMode(1,QtWidgets.QHeaderView.Stretch)
        self.flag = False
        
        
    def clear(self):
        self.__tablewidget_admins_.setRowCount(0)
    
    def addItems(self):
        users = dbHelper().get_users()
        itemflags =QtCore.Qt.ItemFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        for i in users:
            row_number:int = self.__tablewidget_admins_.rowCount()
            self.__tablewidget_admins_.setRowCount(row_number+1)
            username = i[0]
            row_item1 : cQTableWidgetItem = cQTableWidgetItem(userid=username,type_=1,event_=self.event_)
            row_item1.setFlags(itemflags)
            row_item2: cQTableWidgetItem = cQTableWidgetItem(userid=username,type_=0,event_=self.event_)
            row_item2.setFlags(itemflags)
            self.__tablewidget_admins_.setItem(row_number,0,row_item1)
            self.__tablewidget_admins_.setItem(row_number,1,row_item2)
            self.__tablewidget_admins_.setVerticalHeaderItem(row_number,QTableWidgetItem(str(row_number)))

    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None:
        if self.event_ is not None:
            row = self.__tablewidget_admins_.rowAt(event.pos().y())
            col = self.__tablewidget_admins_.columnAt(event.pos().x())
            cell:cQTableWidgetItem = self.__tablewidget_admins_.item(row, col)
            if row !=0:
                cell.contextMenuEvent(self,event)
        self.clear()
        self.setTable()
        self.addItems()

        
