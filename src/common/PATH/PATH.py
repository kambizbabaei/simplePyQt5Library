from os import path

local_database = path.normpath(path.join(path.dirname(__file__),"../Database"))+"/"
mainWidget_images = [
    path.normpath(path.join(path.dirname(__file__),"../assets/admin.png")),
    path.normpath(path.join(path.dirname(__file__),"../assets/books.png")),
    path.normpath(path.join(path.dirname(__file__),"../assets/mybooks.png")),
    path.normpath(path.join(path.dirname(__file__),"../assets/setting.png")),
    path.normpath(path.join(path.dirname(__file__),"../assets/plus.png"))
    ]

CSS_LOGIN = path.normpath(path.join(path.dirname(__file__),"../styles/loginpage.css"))
CSS_BOOKPREVIEW = path.normpath(path.join(path.dirname(__file__),"../styles/bookpreview.css"))
CSS_MAINWINDOW = path.normpath(path.join(path.dirname(__file__),"../styles/mainwindow.css"))
