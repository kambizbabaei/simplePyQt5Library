from PyQt5.QtWidgets import QAction, QMenu


class events:
    def __init__(self,parent) -> None:
        self.parent__ = parent

    def context(self,parent,event):
        context_menu = QMenu()
        activ = QAction("ACTIVE")
        deactiv = QAction("DEACTIVE")
        if self.parent__.activated == 0:
            context_menu.addAction(activ)

        if self.parent__.activated == 1:
            context_menu.addAction(deactiv)
        action = context_menu.exec_(parent.mapToGlobal(event.pos()))
        if action == activ :
            self.parent__.active()
        if action == deactiv:
            self.parent__.deactive()
