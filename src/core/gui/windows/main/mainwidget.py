from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
)

from common.PATH.PATH import CSS_BOOKPREVIEW, CSS_MAINWINDOW
from core.gui.widgets.settingWidget.setting import setting
from modules.customQTwidgets.cQlabel import cQlabel
from modules.customQTwidgets.customFlowWidget import FlowWidget
from utils.dbhelper import dbHelper
from core.gui.widgets.bookPreviewWidget.book_preview import bookPreviewWidget
from core.gui.widgets.bookEditWidget.book_edit import bookEditPage
from core.gui.widgets.adminWidget.adminWidget import adminTableWidget
from utils.parser import parser

class mainWidget(QWidget):

    def __init__(self, parent=None, username=None) -> None:
        super().__init__(parent=parent)
        self.username = username
        self.items = list()
        self.init()
        self.init_data()
        self.update()
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setAccessibleNames()
        self.setStyleSheets()
        self.setMinimumSize(800,600)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self._add_book_button.setGeometry(int(.8*self.width())-20,int(.8*self.height())-20,90,90)
        return super().resizeEvent(a0)
        
    def setStyleSheets(self) -> None:
        self.setStyleSheet(parser(CSS_MAINWINDOW))

    def setAccessibleNames(self):
        self._side_panel_layout.setAccessibleName("sidebar")
        self._admins_widget.setAccessibleName("transparent")
        self._search_lineedit.setAccessibleName("search")
        self._add_book_button.setAccessibleName("add")
        self._add_book_button.setStyleSheet("border-radius: 45px;")


    def init(self):
        # self._add_layouts()
        self._addCompponnents()

    def clear(self):
        if len(self.items) !=0:
            for i in self.items:
                self._book_list_widget.removeItem(i)
                # self.removeItem(i)
            self.items = list()

    def removeItem(self,widget):
        for i in self.items:
            if i == widget:
                self.items.remove(i)
                self._book_list_widget.removeItem(i)
            # i.setParent(None)
            # del i

    def mybooks(self):
        self._search_lineedit.setHidden(False)
        self._add_book_button.setHidden(False)
        self._books_label.setAccessibleName("transparent")
        self._admin_label.setAccessibleName("transparent")
        self._mybooks_label.setAccessibleName("sidebar_clicked")
        self._setting_label.setAccessibleName("transparent")
        self.setStyleSheets()
        self._setting_widget.setHidden(True)
        self._admins_widget.setHidden(True)
        self._book_list_widget.setHidden(False)
        self.clear()
        books = dbHelper().mybooks(self.username)
        if books is not None:
            for i in books:
                book = bookPreviewWidget(i[0],self._book_list_widget)
                book.setMinimumSize(300,100)
                book.setMaximumSize(300,200)
                self.items.append(book)
                self._book_list_widget.addWidget(book)

    def search(self,text):
        
        self.clear()
        books = dbHelper().search(text)
        for i in books:
            book = bookPreviewWidget(i[0],self._book_list_widget)
            book.setMinimumSize(300,100)
            book.setMaximumSize(300,200)
            self.items.append(book)
            self._book_list_widget.addWidget(book)

    def update(self):
        self._search_lineedit.setHidden(False)
        self._add_book_button.setHidden(False)
        self._books_label.setAccessibleName("sidebar_clicked")
        self._admin_label.setAccessibleName("transparent")
        self._mybooks_label.setAccessibleName("transparent")
        self._setting_label.setAccessibleName("transparent")
        self.setStyleSheets()
        self._setting_widget.setHidden(True)
        self._admins_widget.setHidden(True)
        self._book_list_widget.setHidden(False)
        self.clear()
        books = dbHelper().get_books()
        for i in books:
            book = bookPreviewWidget(i[0],self)
            book.setMinimumSize(300,100)
            book.setMaximumSize(300,200)
            self.items.append(book)
            self._book_list_widget.addWidget(book)

    def setting(self):
        self._books_label.setAccessibleName("transparent")
        self._admin_label.setAccessibleName("transparent")
        self._mybooks_label.setAccessibleName("transparent")
        self._setting_label.setAccessibleName("sidebar_clicked")
        self.setStyleSheets()
        self._book_list_widget.setHidden(True)
        self._admins_widget.setHidden(True)
        self._setting_widget.setHidden(False)
        self._add_book_button.setHidden(True)
        self._search_lineedit.setHidden(True)
        
    def admins(self):
        self._search_lineedit.setHidden(True)
        self._add_book_button.setHidden(True)

        self._books_label.setAccessibleName("transparent")
        self._admin_label.setAccessibleName("sidebar_clicked")
        self._mybooks_label.setAccessibleName("transparent")
        self._setting_label.setAccessibleName("transparent")
        self.setStyleSheets()
        self._book_list_widget.setHidden(True)
        self._admins_widget.setHidden(False)
        self._setting_widget.setHidden(True)

    def _addCompponnents(self):
        self._central_layout = QHBoxLayout(self)
        self._side_panel_layout = QWidget()
        self._side_panel_layout.setLayout(QVBoxLayout())
        
        self._main_panel_layout = QVBoxLayout()
        self._book_list_widget = FlowWidget(self)
        self._add_book_button = cQlabel(self)
        self._add_book_button.setGeometry(int(.8*self.width()),int(.8*self.height()),90,90)
        self._search_lineedit = QLineEdit(self)
        self._search_lineedit.setPlaceholderText("search")
        self._search_lineedit_layout = QHBoxLayout()
        self._books_label = cQlabel()
        self._mybooks_label = cQlabel()
        self._setting_label = cQlabel()
        self._setting_widget = setting(self,self.username)
        self._setting_widget.setHidden(True)
        self._admin_label = cQlabel()
        self._admins_widget = adminTableWidget(self)
        self._admins_widget.setHidden(True)
        self._search_lineedit_layout.addSpacing(100)
        self._search_lineedit_layout.addWidget(self._search_lineedit)

        def s():
            text = self._search_lineedit.text()
            if text is None:
                self.update()
            else:
                self.search(text)
                
        self._search_lineedit.textChanged.connect(s)
        self._search_lineedit_layout.addSpacing(100)

        self._central_layout.addWidget(self._side_panel_layout,1)
        self._central_layout.addLayout(self._main_panel_layout,4)

        self._main_panel_layout.addLayout(self._search_lineedit_layout,1)
        self._main_panel_layout.addWidget(self._book_list_widget,6)
        self._main_panel_layout.addWidget(self._admins_widget,6)
        self._main_panel_layout.addWidget(self._setting_widget,6)
        self._main_panel_layout.setSpacing(0)
        self._main_panel_layout.setContentsMargins(0,0,0,0)

        self._side_panel_layout.layout().addWidget(self._books_label,1)
        self._side_panel_layout.layout().addWidget(self._mybooks_label,1)
        self._side_panel_layout.layout().addWidget(self._setting_label,1)
        self._side_panel_layout.layout().addWidget(self._admin_label,1)

        def edit():
            self.be = bookEditPage(parent=self)
            self.be.exec_()
            self.update()
        self._add_book_button.clicked.connect(edit)

        self._admin_label.clicked.connect(self.admins)

        self._mybooks_label.clicked.connect(self.mybooks)

        self._books_label.clicked.connect(self.update)

        self._setting_label.clicked.connect(self.setting)

        self._add_book_button.setAccessibleName("border-radius: 30px;")
            

    def init_data(self):
        from common.PATH.PATH import mainWidget_images
        labels = [
            self._admin_label,
            self._books_label,
            self._mybooks_label,
            self._setting_label,
            self._add_book_button
            ]
        for i in range(5):
            qpixelmap = QPixmap(mainWidget_images[i])
            labels[i].setPixmap(qpixelmap.scaled(90,90))
        

def start():
    from sys import (
        argv as sys_argv, exit 
    )
    q_application = QApplication(sys_argv)
    main_window = mainWidget()
    main_window.show()
    q_application.exec_()

if __name__ == "__main__":
    start()