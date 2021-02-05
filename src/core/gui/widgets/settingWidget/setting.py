from typing import Text
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAbstractItemView, QApplication, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

from utils.dbhelper import dbHelper



class setting(QWidget):
    def __init__(self, parent,username) -> None:
        super().__init__(parent=parent)
        self._parent = parent
        self.username = username
        self.rowid = dbHelper().get_user_by_username(self.username)
        self.init()
        self.addComponnent()
        self.setData()
        self.setDataToComponnents()
        
    def init(self):
        self.main = QVBoxLayout(self)
        self.main_top = QHBoxLayout()
        self.main_botton = QHBoxLayout()
        self.main.addLayout(self.main_top)
        self.main.addLayout(self.main_botton)
        self.setLayout(self.main)
        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()
        self.main_top.addLayout(self.left_layout,1)
        self.main_top.addLayout(self.right_layout,4)

    def addComponnent(self):
        for i in ["sec. question","sec. answer","username","password"]:
            label = QLabel(self)
            label.setText(i)
            self.left_layout.addWidget(label)

        self.s_q_ = QLineEdit()
        self.s_a_ = QLineEdit()
        self.username_lineedit = QLineEdit()
        self.password_lineedit = QLineEdit()

        self.right_layout.addWidget(self.s_q_)
        self.right_layout.addWidget(self.s_a_)
        self.right_layout.addWidget(self.username_lineedit)
        self.right_layout.addWidget(self.password_lineedit)
         
        for i in range(2):
            q =QLabel()
            q.setAccessibleName("transparent")
            self.main_botton.addWidget(q)

        self.save_button = QPushButton()
        self.save_button.setText("Save")
        self.save_button.clicked.connect(self.update)

        self.main_botton.addWidget(self.save_button)
        
    def setData(self):
        user = dbHelper().get_user_by_uid( self.rowid)
        self.c_username ,self.c_password , self.c_sec_q , self.c_sec_a ,_=user

    def setDataToComponnents(self):
        self.username_lineedit.setText(self.c_username)
        self.password_lineedit.setPlaceholderText("[Type To Change Password]")
        self.s_q_.setText(self.c_sec_q)
        self.s_a_.setText(self.c_sec_a)

    def change(self):
        self.username_lineedit.setPlaceholderText("")
        self.username_lineedit.setAccessibleName("")
        self._parent.setStyleSheets()
        
    def update(self):
        if self.username_lineedit.text() =="" or self.s_q_.text() == "" or self.s_a_.text() == "":

            if self.username_lineedit.text() =="":
                self.username_lineedit.setPlaceholderText("[this field is empty]")

            if self.s_q_.text() == "" :
                self.s_q_.setPlaceholderText("[this field is empty]")

            if self.s_a_.text() == "":
                self.s_a_.setPlaceholderText("[this field is empty]")

            return

        if dbHelper().update_user(self.c_username,self.username_lineedit.text(),self.password_lineedit.text(),self.s_q_.text(),self.s_a_.text()) == -1:
            self.username_lineedit.setText("")
            self.username_lineedit.setPlaceholderText("This User Name Exist")
            self.username_lineedit.setAccessibleName("error")
            return
        self.setData()

    def setHidden(self, hidden: bool) -> None:
        self.setData()
        self.setDataToComponnents()
        return super().setHidden(hidden)

def start():
    from sys import (
        argv as sys_argv, exit 
    )
    q_application = QApplication(sys_argv)
    main_window = setting(None,'dsf')
    main_window.show()
    q_application.exec_()

if __name__ == "__main__":
    start()