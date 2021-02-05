from PyQt5.QtWidgets import (
     QLabel, QLineEdit, QPushButton, QWidget, QMainWindow, QApplication, QGridLayout
    )
from PyQt5 import QtCore

import typing

from core.gui.widgets.signupWidget.signupWidget import signup_window
from core.gui.widgets.loginWidget.loginWidget import signin_window
from core.gui.widgets.recoverPasswordWidget.recover import recovery_widget

class first_page(QMainWindow):
    def __init__(self, parent: typing.Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)

        self.__add_pages__()
        

        self.__init_window__()
        self.logininfo = 0

    def _change_view_to_signup(self):

        self.setMaximumSize(self.signup_page.maximumSize())
        self.setMinimumSize(self.signup_page.minimumSize())
        self.signin_page.setVisible(False)
        if self.recover_page is not None:
            self.recover_page.setVisible(False)
        self.signup_page.setVisible(True)


    def _change_view_to_signin(self):

        self.setMaximumSize(self.signin_page.maximumSize())
        self.setMinimumSize(self.signin_page.minimumSize())
        self.signup_page.setVisible(False)
        if self.recover_page is not None:
            self.recover_page.setVisible(False)
        self.signin_page.setVisible(True)
        
        

    def __init_window__(self):
        self.signup_page.setVisible(True)
        self.setMaximumSize(self.signup_page.maximumSize())
        self.setMinimumSize(self.signup_page.minimumSize())
        # self.signin_page.setVisible(True)
        # self.setMaximumSize(self.signin_page.maximumSize())
        # self.setMinimumSize(self.signin_page.minimumSize())

    def __add_pages__(self):
        self.signup_page:QWidget = signup_window(self)
        self.signup_page.setVisible(False)
        self.signin_page :QWidget = signin_window(self)
        self.signin_page.setVisible(False)
        self.recover_page = None

    def open(self,uid):
        self.logininfo = 1
        self.uid = uid
        self.close()

    def changeToForget(self,username):
        self.recover_page:QWidget = recovery_widget(self,username)
        self.recover_page.setVisible(False)
        self.signin_page.setVisible(False)
        self.signin_page.setVisible(False)
        self.recover_page.setVisible(True)
        pass


def run():
    from sys import argv as sys_argv
    app = QApplication(sys_argv)
    fp = first_page()
    fp.show()
    app.exec_()
    app.exit()
    if fp.logininfo == 1:
        return fp.uid
    return -1
    