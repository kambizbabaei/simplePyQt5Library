from utils.dbhelper import dbHelper


class events:
    def __init__(self,parent) -> None:
        self.parent = parent
        self.username = parent.username

    def changepassword(self):

        sec_ans =  self.parent.sec_a_lineedit.text()
        user =dbHelper().get_user_by_uid( dbHelper().get_user_by_username( self.username)[0])
        print(user)
        password = self.parent._new_password_lineedit.text()
        if sec_ans =="" or password=="":
            self.parent.empty_error()
            return
        if user is not None:
            if user[3] == sec_ans:
                dbHelper().update_password(user[0],password)
        self.parent._password_changed_()



