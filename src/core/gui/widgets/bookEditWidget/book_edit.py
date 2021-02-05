from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import  QPixmap
from PyQt5.QtWidgets import (
    QDialog, QFileDialog, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget
)
from common.PATH.PATH import CSS_LOGIN

from modules.customQTwidgets.cQlabel import cQlabel

from utils.dbhelper import dbHelper
from utils.parser import parser
from .event import event


class bookEditPage(QDialog):

    def __init__(self, parent,uniqueId=None) -> None:
        # self._event = bookPreviewEvent(self)
        self._parent = parent
        self.mode =1
        super().__init__()
        self._uid = uniqueId
        self._dbHelper:dbHelper = dbHelper()
        self.init()
        self.init_data()
        self._event = event(self)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet(parser(CSS_LOGIN))
        
    def init(self):
        self._add_layouts()
        self._addCompponnents()

    def init_data(self):
        if self._uid is not None:
            self.mode = 0
            self._getDataFromDataBase()
            self._setDataToWidgets()    

    def _add_layouts(self):

        self._central_widget = QHBoxLayout(self)
        self._left_layout = QGridLayout()
        self._right_layout =QVBoxLayout ()
        self._central_widget.addLayout(self._left_layout)
        self._central_widget.addLayout(self._right_layout)
        self._right_top_layout = QVBoxLayout()
        self._right_bottom_layout = QHBoxLayout()  
        self._right_layout.addLayout(self._right_top_layout)
        self._right_layout.addLayout(self._right_bottom_layout)

    def _addCompponnents(self):

        self._book_name_label = QLabel("Name : ")
        self._book_name_lineedit = QLineEdit()
        self._book_author_label = QLabel("Author : ")
        self._book_author_lineedit = QLineEdit()
        self._book_pages_label = QLabel("Total Pages : ")
        self._book_pages_lineedit = QLineEdit()
        self._book_edition_label = QLabel("Edition Number : ")
        self._book_edition_lineedit = QLineEdit()
        self._book_isbn_label = QLabel("ISBN : ")
        self._book_isbn_lineedit = QLineEdit()
        self._book_publisher_label = QLabel("Publisher : ")
        self._book_publisher_lineedit = QLineEdit()
        self._book_language_label = QLabel("Language")
        self._book_language_lineedit = QLineEdit()
        self._book_translate_label = QLabel("Translated by : ")
        self._book_translate_lineedit = QLineEdit()
        self._book_firstpublishdate_label = QLabel("First Release Date : ")
        self._book_firstpublishdate_lineedit = QLineEdit()
        self._book_editionpublishdate_label = QLabel("Editon Release Date : ")
        self._book_editionpublishdate_lineedit = QLineEdit()
        self._book_desc_label = QLabel("Info")
        self._book_desc_textedit = QTextEdit()
        self._book_image_label = cQlabel()
        self._book_image_label.setStyleSheet("""border: 2px solid grey;""")
        self._save_button = QPushButton("Save Changes")
        self._cancel_button = QPushButton("Cancel")

        self._left_layout.addWidget(self._book_name_label,0,0)
        self._left_layout.addWidget(self._book_name_lineedit,0,1)
        self._left_layout.addWidget(self._book_author_label,1,0)
        self._left_layout.addWidget(self._book_author_lineedit,1,1)
        self._left_layout.addWidget(self._book_pages_label,2,0)
        self._left_layout.addWidget(self._book_pages_lineedit,2,1)
        self._left_layout.addWidget(self._book_edition_label,3,0)
        self._left_layout.addWidget(self._book_edition_lineedit,3,1)
        self._left_layout.addWidget(self._book_isbn_label,4,0)
        self._left_layout.addWidget(self._book_isbn_lineedit,4,1)
        self._left_layout.addWidget(self._book_publisher_label,5,0)
        self._left_layout.addWidget(self._book_publisher_lineedit,5,1)
        self._left_layout.addWidget(self._book_language_label,6,0)
        self._left_layout.addWidget(self._book_language_lineedit,6,1)
        self._left_layout.addWidget(self._book_translate_label,7,0)
        self._left_layout.addWidget(self._book_translate_lineedit,7,1)
        self._left_layout.addWidget(self._book_firstpublishdate_label,10,0)
        self._left_layout.addWidget(self._book_firstpublishdate_lineedit,10,1)
        self._left_layout.addWidget(self._book_edition_label,11,0)
        self._left_layout.addWidget(self._book_edition_lineedit,11,1)
    
        self._right_bottom_layout.addWidget(self._save_button)
        self._right_bottom_layout.addWidget(self._cancel_button)

        self._right_top_layout.addWidget(self._book_image_label,10)
        self._right_top_layout.addWidget(self._book_desc_label,1)
        self._right_top_layout.addWidget(self._book_desc_textedit,10)
        def s ():
            self._event.save()
        self._save_button.clicked.connect(s)

        def c():
            self._event.cancel()
            
        self._cancel_button.clicked.connect(c)

        def i ():
            self.set_image_to_label()
        
        self._book_image_label.clicked.connect(self.set_image_to_label)

        self._book_name_lineedit.setPlaceholderText("[required]")
        self._book_author_lineedit.setPlaceholderText("[required]")
        self._book_pages_lineedit.setPlaceholderText("[required]")
        self._book_isbn_lineedit.setPlaceholderText("[required]")
        


        
        

    def _getDataFromDataBase(self):
        book_data = self._dbHelper.get_book(uid = self._uid)
        self._book_name = book_data[0]
        self._book_author_name = book_data[1]
        self._book_pages = book_data[2]
        self._book_edition = book_data[3]
        self._book_isbn = book_data[4]
        self._book_publisher = book_data[5]
        self._book_language = book_data[6]
        self._book_translator = book_data[7]
        self._book_uploader = book_data[8]
        self._book_uploaddate = book_data[9]
        self._book_release_date = book_data[10]
        self._book_editionpublishdate = book_data[11]
        self._book_desc = book_data[12]
        self._book_image = book_data[13]
        del book_data
    def _setDataToWidgets(self):

        self._book_name_lineedit.setText(self._book_name)
        self._book_author_lineedit.setText(self._book_author_name)
        self._book_pages_lineedit.setText(self._book_pages)
        self._book_edition_lineedit.setText(self._book_edition)
        self._book_isbn_lineedit.setText(self._book_isbn)
        self._book_publisher_lineedit.setText(self._book_publisher)
        self._book_language_lineedit.setText(self._book_language)
        self._book_translate_lineedit.setText(self._book_translator)
        self._book_firstpublishdate_lineedit.setText(self._book_release_date)
        self._book_editionpublishdate_lineedit.setText(self._book_editionpublishdate)
        self._book_desc_textedit.setPlainText(self._book_desc)
        self.fileaddress = None
        if self._book_image is None or self._book_image == "None":
            self._book_image_label.setText(self._book_name)
        else:
            self.qimg = QtGui.QImage.fromData(self._book_image)
            pixmap = QPixmap.fromImage(self.qimg)
            self._book_image_label.setPixmap(pixmap)
            pass

    def set_image_to_label(self):
        img_file_name = QFileDialog.getOpenFileName(self,"Browse For Image ...","c\\","Image File(*.jpg,*jpeg)")
        if img_file_name[0] !="":
            pixmap = QPixmap(img_file_name[0])
            self.fileaddress  = img_file_name[0]
            pixmap = pixmap.scaled(self._book_image_label.width(),self._book_image_label.height())
            self._book_image_label.setPixmap(pixmap)






        

        
