
from PyQt5 import QtCore
from PyQt5.QtCore import  Qt
from utils.dbhelper import dbHelper

class event:
    def __init__(self,parent) -> None:
        super().__init__()
        self.parent = parent
    
    def save(self):
        _book_name  = self.parent._book_name_lineedit.text()
        _book_author_name =self.parent._book_author_lineedit.text()
        _book_pages =self.parent._book_pages_lineedit.text()
        _book_edition =self.parent._book_edition_lineedit.text()
        _book_isbn =self.parent._book_isbn_lineedit.text()
        _book_publisher =self.parent._book_publisher_lineedit.text()
        _book_language =self.parent._book_language_lineedit.text()
        _book_translator =self.parent._book_translate_lineedit.text()
        _book_uploader  =self.parent._parent.username
        
        _book_release_date  =self.parent._book_firstpublishdate_lineedit.text()
        _book_editionpublishdate =self.parent._book_editionpublishdate_lineedit.text()
        _book_desc =self.parent._book_desc_textedit.toPlainText()
        _book_image = None
        if _book_isbn == "" or _book_name == "" or _book_pages == ""or _book_author_name == "":
            #TODO add error label
            return
        if self.parent._book_image_label.pixmap() is not None:
            if self.parent.fileaddress is not None:
                with open(self.parent.fileaddress,'rb') as file:
                    _book_image = file.read()
            else:
                _book_image = self.parent._book_image_label.pixmap()

        if self.parent.mode == 1:
            from datetime import datetime
            _book_uploaddate =datetime.now()
            dbHelper().add_book(_book_name,_book_author_name,_book_pages,_book_isbn,_book_edition,_book_publisher,_book_language,_book_translator,_book_uploader,_book_uploaddate,_book_release_date,_book_editionpublishdate,_book_desc,_book_image)
            self.parent.close()
        else:
            #edit book info 
            dbHelper().editbook(_book_name,_book_author_name,_book_pages,_book_edition,_book_isbn,_book_publisher,_book_language,_book_translator,_book_release_date,_book_editionpublishdate,_book_desc,_book_image,self.parent._uid)
            self.parent.close()
            

    def cancel(self):
        self.parent.close()


