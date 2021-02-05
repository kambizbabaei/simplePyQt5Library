from PyQt5.QtWidgets import  QTableWidgetItem
from PyQt5.QtGui import QContextMenuEvent

from utils.dbhelper import dbHelper

class cQTableWidgetItem(QTableWidgetItem): 

    def __init__(self,parent = None,event_=None,userid = None,type_=None):
        QTableWidgetItem.__init__(self,parent)
        self.event_=event_(self)
        self.activated = False
        self.type_ = type_
        
        self.username = userid
        self.init()
        self.setdata()

    def setdata(self):
        if self.type_ == 0:
            if self.activated:
                self.setText("ACTIVATED")
                return
            self.setText("DEACTIVATED")
        else:
            self.setText(self.username)

    def init(self):
        self.username,_,_,_,self.activated = dbHelper().get_user_by_uid( dbHelper().get_user_by_username(self.username))

    def active(self):
        self.activated = True
        if self.type_ == 0:
            self.setText("ACTIVATED")
        dbHelper().active_user(dbHelper().get_user_by_username(self.username))

    def deactive(self):
        self.activated = False
        if self.type_ == 0:
            self.setText("DEACTIVATED")
        dbHelper().deactive_user(dbHelper().get_user_by_username(self.username))
        
    def contextMenuEvent(self,parent ,event: QContextMenuEvent) -> None:
        if self.event_ is not None:
            self.event_.context(parent,event)