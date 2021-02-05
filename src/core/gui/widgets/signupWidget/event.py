from utils.dbhelper import dbHelper

class event:
    def __init__(self,parent) -> None:
        self.parent = parent

    def signup(self):

        username = self.parent._username_lineedit.text()
        passwors = self.parent._password_lineedit_.text()
        sec_q = self.parent.sec_q.text()
        sec_a = self.parent.sec_p.text()
        if username =="" or passwors =="" or sec_a =="" or sec_q =="":
            self.parent.empty_error()
            return
        user = dbHelper().add_user(username,passwors,sec_q,sec_a)
        if user is None:
            self.parent._username_exist()
            return
        self.parent.wait()
    
