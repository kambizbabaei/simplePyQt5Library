from PyQt5.QtWidgets import QApplication

from core.gui.windows.login.login import run
from core.gui.windows.main.mainwidget import mainWidget


def ship():
    login_info = run()
    if login_info != -1:
        from sys import argv as sys_argv
        app = QApplication(sys_argv)
        main = mainWidget(username=login_info)
        main.show()
        app.exec_()
