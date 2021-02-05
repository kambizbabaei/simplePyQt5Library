from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import QByteArray
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QGridLayout, QHBoxLayout, QLabel
)


from common.PATH.PATH import CSS_BOOKPREVIEW
from modules.customQTwidgets.cQWidget import customQWidget as QWidget
from utils.dbhelper import dbHelper
from core.gui.widgets.bookPreviewWidget.events import bookPreviewEvent
from core.gui.widgets.bookEditWidget.book_edit import bookEditPage
from utils.parser import parser

class bookPreviewWidget(QWidget):
    """
    book preview widget
    """
    def __init__(self, uniqueId:str ,parent ):
        """
        :param uniqueId: book unique id
        :param parent: parent widget obj
        """
        self._event = bookPreviewEvent(self)
        self._parent = parent

        super().__init__( event_=self._event)
        
        self._uid = uniqueId
        self._dbHelper:dbHelper = dbHelper()
        self.init()
        self.init_data()
        self.setAutoFillBackground(True)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setAccessibleNames()
        self.setStyleSheet(parser(CSS_BOOKPREVIEW))

    def setAccessibleNames(self) :
        pass

    def init(self):
        self._add_layouts()
        self._addCompponnents()

    def init_data(self):
        self._getDataFromDataBase()
        self._setDataToWidgets()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        if self.qimg is not None:
            self.__image_label.setPixmap(QPixmap( self.qimg).scaled(self.__image_label.width(),self.__image_label.height()))
        return super().resizeEvent(a0)

    def _setDataToWidgets(self):
        self.__name_label_text.setText("Book Name :")
        self.__author_name_label_text.setText("Written By :")
        self.__releasedate_label_text.setText("Release Date : ")
        self.__name_label.setText(self._book_name)
        self.__author_name_label.setText(self._book_author_name)
        self.__releasedate_label.setText(self._book_release_date)
        self.qimg = None
        if self._book_image == "None":
            self.__image_label.setText(self._book_name)
        else:
            self.qimg = QtGui.QImage.fromData(self._book_image)
            pixmap = QPixmap.fromImage(self.qimg)
            self.__image_label.setPixmap(pixmap)

        self._book_image = None #remove image bytedata for memory management

    def _getDataFromDataBase(self):
        book_data = self._dbHelper.get_book(uid = self._uid)
        self._book_name = book_data[0]
        self._book_author_name = book_data[1]
        self._book_release_date = book_data[10]
        self._book_image = book_data[13]
        del book_data
        
    def _add_layouts(self):
        
        self._central_widget = QHBoxLayout()
        self.setLayout(self._central_widget)
        self._image_layout = QHBoxLayout() #book image will show inside this layout
        self._central_widget.addLayout(self._image_layout,1) #with second argument we make image one third of the widget
        self._info_layout = QGridLayout()
        self._central_widget.addLayout(self._info_layout,1) #with second argument we make info two third of the widget

    def _addCompponnents(self):
        self.__image_label  = QLabel()
        self.__name_label  = QLabel()
        self.__releasedate_label  = QLabel()
        self.__author_name_label = QLabel()
        self.__name_label_text  = QLabel()
        self.__releasedate_label_text  = QLabel()
        self.__author_name_label_text = QLabel()
        self._image_layout.addWidget(self.__image_label)
        self._info_layout.addWidget(self.__name_label,0,1)
        self._info_layout.addWidget(self.__name_label_text,0,0)
        self._info_layout.addWidget(self.__author_name_label_text,1,0)
        self._info_layout.addWidget(self.__author_name_label,1,1)
        self._info_layout.addWidget(self.__releasedate_label_text,2,0)
        self._info_layout.addWidget(self.__releasedate_label,2,1)

    def delete_book(self):
        self._dbHelper.delete_book(self._uid)
        self._parent.removeItem(self)
        self._parent.update()

    def edit_book(self):
        ep= bookEditPage(self._parent,self._uid)
        ep.exec()
        self.init_data()
        self._parent.update()
        del ep
