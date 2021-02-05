from PyQt5.QtWidgets import (
     QLabel, QLineEdit, QPushButton, QWidget, QMainWindow
    )
from PyQt5 import QtCore

import typing
from common.PATH.PATH import CSS_LOGIN

from core.gui.widgets.signupWidget.event import event
from utils.parser import parser

class signup_window(QWidget):
    def __init__(self, parent: QMainWindow) -> None:
        super().__init__(parent=parent)
        self.parent_= parent
        self._init_window_()    
        self._add_component_()
        self._event = event(self)
        self.setAccessibleNames()
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet(parser(CSS_LOGIN))

    def _init_window_(self):
        self.setFixedSize(500,300)

    def setAccessibleNames(self):
        self._login_button_.setAccessibleName("hiddenbutton")
        self._password_lineedit_.setAccessibleName("passwordcontainer")

    def _add_component_(self):
        self.__login_button_()
        self.__signup_button_()
        self.__username_lineedit_()
        self.__password_lineedit_()
        self.__username_label_()
        self.__password_label_()
        self.__sec_q_label_()
        self.__sec_a_label_()
        self.__sec_q_lineedit_()
        self.__sec_p_lineedit_()
        self.__error_label__()

    def _username_exist(self):
        self.__error_label.setText("this username exist,try another one")

    def empty_error(self):
        self.__error_label.setText("please fill all fileds")

    def __error_label__(self):
        self.__error_label = QLabel(self)
        self.__error_label.setGeometry(140,45,250,20)
        self.__error_label.setStyleSheet(""" color: red;  """)

    def __sec_p_lineedit_(self):

        self.sec_p:QLineEdit = QLineEdit(self)
        self.sec_p.setPlaceholderText("Enter Answer")
        self.sec_p.setGeometry(140,145,250,20)

    def __sec_q_lineedit_(self):
        self.sec_q:QLineEdit = QLineEdit(self)
        self.sec_q.setPlaceholderText("Enter Question")
        self.sec_q.setGeometry(140,118,250,20)

    def __sec_a_label_(self):
        self.__sec_a_label:QLabel = QLabel(self)
        self.__sec_a_label.setText("sec. answer :")
        self.__sec_a_label.setGeometry(80,145,60,15)

    def __sec_q_label_(self):
        self._username_label:QLabel = QLabel(self)
        self._username_label.setText("sec. ques. :")
        self._username_label.setGeometry(80,118,60,15)

    def __signup_button_(self):
        self._signup_button_ : QPushButton = QPushButton(self)
        self._signup_button_.setGeometry(210,180,80,50)
        self._signup_button_.setText("Signup")
        self._signup_button_.setAccessibleName("signup_button")
        def s ():
            self._event.signup()
        self._signup_button_.clicked.connect(s)

    def __login_button_(self):
        self._login_button_: QPushButton = QPushButton(self)
        self._login_button_.setText("do you have an account? signin.")
        self._login_button_.setGeometry(155,160,200,22)
        self._login_button_.setAccessibleName("text_button")

        def login_button():
            self.parent_._change_view_to_signin()
        self._login_button_.clicked.connect(login_button)

    def __username_lineedit_(self):
        self._username_lineedit:QLineEdit = QLineEdit(self)
        self._username_lineedit.setPlaceholderText("Enter Username")
        self._username_lineedit.setGeometry(140,65,250,20)
        self._username_lineedit.setAccessibleName("line_edit")

    def __password_lineedit_(self):
        self._password_lineedit_:QLineEdit = QLineEdit(self)
        self._password_lineedit_.setPlaceholderText("Enter Password")
        self._password_lineedit_.setEchoMode(QLineEdit.Password)
        self._password_lineedit_.setGeometry(140,90,250,20)
        self._password_lineedit_.setAccessibleName("line_edit")

    def __username_label_(self):
        self._username_label:QLabel = QLabel(self)
        self._username_label.setText("username :")
        self._username_label.setGeometry(80,65,60,15)

    def __password_label_(self):
        self._password_label:QLabel = QLabel(self)
        self._password_label.setText("password :")
        self._password_label.setGeometry(80,90,60,15)

    def wait(self):
        self.__error_label.setText("wait for account activision")
