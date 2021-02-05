from PyQt5.QtWidgets import (
     QLabel, QLineEdit, QPushButton, QWidget, QGridLayout, QVBoxLayout, QMainWindow, QApplication
    )
from PyQt5 import QtCore

from common.PATH.PATH import CSS_LOGIN
from core.gui.widgets.recoverPasswordWidget.event import events
from utils.dbhelper import dbHelper
from utils.parser import parser

class recovery_widget(QWidget):
    def __init__(self, parent: QMainWindow,username ) -> None:
        super().__init__(parent=parent)
        self.parent_= parent
        self.username = username
        self._init_window_()    
        self._add_component_()
        self._event = events(self)
        self.setAccessibleNames()
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet(parser(CSS_LOGIN))
        self.setdata()

    def _init_window_(self):
        self.setFixedSize(500,300)

    def setAccessibleNames(self):
        self._login_button_.setAccessibleName("hiddenbutton")
        self._new_password_lineedit.setAccessibleName("passwordcontainer")

    def _add_component_(self):
        self.__login_button_()
        self._change_password_button_()
        self._new_password_lineedit_()
        self.__seq_q_label__()
        self._new_password_label__()
        self.__sec_a_label_()
        self.__sec_a_lineedit_()
        self.__error_label__()


    def _password_changed_(self):
        self.__error_label.setText("your password changed if your answer is correct")

    def empty_error(self):
        self.__error_label.setText("Please Fill All Fileds")

    def __error_label__(self):
        self.__error_label = QLabel(self)
        self.__error_label.setGeometry(140,45,250,20)
        self.__error_label.setStyleSheet(""" color: red;  """)

    def __sec_a_lineedit_(self):

        self.sec_a_lineedit:QLineEdit = QLineEdit(self)
        self.sec_a_lineedit.setPlaceholderText("Enter Answer")
        self.sec_a_lineedit.setGeometry(140,145,250,20)

    def setdata(self):
        if(dbHelper().get_user_by_username( self.username) != None):
            user_seq =dbHelper().get_user_by_uid( dbHelper().get_user_by_username( self.username)[0])[2]
            self.__sec_q_label.setText(user_seq)

    def __sec_a_label_(self):
        self.__sec_a_label:QLabel = QLabel(self)
        self.__sec_a_label.setText("sec. answer :")
        self.__sec_a_label.setGeometry(80,145,60,15)

    def _change_password_button_(self):
        
        self._change_password_button : QPushButton = QPushButton(self)
        self._change_password_button.setGeometry(210,180,80,50)
        self._change_password_button.setText("Submit")
        self._change_password_button.setAccessibleName("signup_button")
        def s ():
            self._event.changepassword()
        self._change_password_button.clicked.connect(s)


    def __login_button_(self):
        self._login_button_: QPushButton = QPushButton(self)
        self._login_button_.setText("do you have your password? signin.")
        self._login_button_.setGeometry(155,160,200,22)
        self._login_button_.setAccessibleName("text_button")

        def login_button():
            self.parent_._change_view_to_signin()

        self._login_button_.clicked.connect(login_button)


    def _new_password_lineedit_(self):

        self._new_password_lineedit:QLineEdit = QLineEdit(self)
        self._new_password_lineedit.setPlaceholderText("Enter New Password")
        self._new_password_lineedit.setEchoMode(QLineEdit.Password)
        self._new_password_lineedit.setGeometry(140,115,250,20)

    def __seq_q_label__(self):

        self.__sec_q_label:QLabel = QLabel(self)
        self.__sec_q_label.setGeometry(80,90,305,15)

    def _new_password_label__(self):
        
        self._new_password_label_:QLabel = QLabel(self)
        self._new_password_label_.setText("new password :")
        self._new_password_label_.setGeometry(80,115,60,15)


