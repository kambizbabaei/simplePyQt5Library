from PyQt5.QtWidgets import (
     QLabel, QLineEdit, QPushButton, QWidget, QGridLayout, QVBoxLayout, QMainWindow, QApplication
    )
from PyQt5 import QtCore

from core.gui.widgets.loginWidget.event import event

from common.PATH.PATH import CSS_LOGIN
from utils.parser import parser

class signin_window(QWidget):
    def __init__(self, parent: QMainWindow ) -> None:
        super().__init__(parent=parent)
        self._parent:QMainWindow = parent
        # self.event_ =event()
        self._init_window_()
        self._add_component_()
        self._event = event(self)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setAccessibleNames()
        self.setStyleSheet(parser(CSS_LOGIN))

    def empty_error(self):
        self.__error_label.setText("please fill all fileds")

    def _init_window_(self):
        self.setFixedSize(500,300)
        
        # self.setAccessibleName("windows")
        # self.setStyleSheet(window_default_style("windows",signuppage_additional_styles()))
        # self.main_layout = QVBoxLayout()
        # self.setLayout(self.main_layout)  

    def setAccessibleNames(self):
        self.__forget_button.setAccessibleName("hiddenbutton")
        self._signup_button.setAccessibleName("hiddenbutton")
        self._password_lineedit_.setAccessibleName("passwordcontainer")

    def _add_component_(self):
        self.__login_button_()
        self.__signup_button_()
        self.__username_lineedit_()
        self.__password_lineedit_()
        self.__username_label_()
        self.__password_label_()
        self.__forget_button_()
        self.__error_label_()

    def __error_label_(self):
        self.__error_label = QLabel(self)
        self.__error_label.setGeometry(140,95,200,22)
        self.__error_label.setStyleSheet(""" color: red;  """)

    def _fill_usernane(self):
        self.__error_label.setText("enter your username")
    
    def __forget_button_(self):
        self.__forget_button = QPushButton(self)
        self.__forget_button.setText("forget password")
        self.__forget_button.setGeometry(0,278,200,22)
        def f ():
            self._event.forget()
        self.__forget_button.clicked.connect(f)


    def __signup_button_(self):
        self._signup_button : QPushButton = QPushButton(self)
        self._signup_button.setText("you don't have an account? Signup.")
        self._signup_button.setGeometry(155,160,200,22)
        self._signup_button.setAccessibleName("text_button")
        def signup_button():
            self._parent._change_view_to_signup()
        self._signup_button.clicked.connect(signup_button)
        
    def __login_button_(self):
        self._login_button_: QPushButton = QPushButton(self)
        self._login_button_.setText("Signin")
        self._login_button_.setGeometry(210,180,80 ,50)
        self._login_button_.setAccessibleName("login_button")
        def c():
            self._event.login()
        self._login_button_.clicked.connect(c)
        
    def __username_lineedit_(self):
        self._username_lineedit:QLineEdit = QLineEdit(self)
        self._username_lineedit.setPlaceholderText("Enter Username")
        self._username_lineedit.setGeometry(140,115,250,20)
        self._username_lineedit.setAccessibleName("line_edit")

    def __password_lineedit_(self):
        self._password_lineedit_:QLineEdit = QLineEdit(self)
        self._password_lineedit_.setPlaceholderText("Enter Password")
        self._password_lineedit_.setEchoMode(QLineEdit.Password)
        self._password_lineedit_.setGeometry(140,142,250,20)
        self._password_lineedit_.setAccessibleName("line_edit")
        
    def __username_label_(self):   
        self._username_label:QLabel = QLabel(self)
        self._username_label.setText("username :")
        self._username_label.setGeometry(80,120,60,15)

    def __password_label_(self):
        self._password_label:QLabel = QLabel(self)
        self._password_label.setText("password :")
        self._password_label.setGeometry(80,145,60,15)

    def wrongpassword(self):
        self.__error_label.setText("wrong username or password")
        
