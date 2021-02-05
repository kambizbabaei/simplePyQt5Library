from utils.dbhelper import dbHelper

class event:
    def __init__(self,parent) -> None:
        self.parent = parent

    def login(self):
        username = self.parent._username_lineedit.text()
        passwors = self.parent._password_lineedit_.text()
        if username=="" or passwors =="":
            self.parent.empty_error()
            return
        user = dbHelper().get_user(username= username,password= passwors)
        if user is not None:
            if user[4]==1:
                self.parent._parent.open(user[0])
            return
        self.parent.wrongpassword()

    def forget(self):
        username = self.parent._username_lineedit.text()
        if username =="":
            self.parent._fill_usernane()
            return
        
        self.parent._parent.changeToForget(username )


