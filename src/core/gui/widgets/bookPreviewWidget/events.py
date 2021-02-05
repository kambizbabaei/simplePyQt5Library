from PyQt5.QtWidgets import (
    QMenu,QAction
)

class bookPreviewEvent:

    def __init__(self,parent) -> None:
        super().__init__()
        self.__parent = parent

    def context_menu_event(self,parent,event) :
        context_menu = QMenu()
        delete_action = QAction("Delete Book")
        context_menu.addAction(delete_action)
        edit_action = QAction("Edit Book")
        context_menu.addAction(edit_action)
        action = context_menu.exec_(parent.mapToGlobal(event.pos()))

        if action == delete_action:
            self.__parent.delete_book()
            # self.__parent._parent.update()

        elif action == edit_action:
            self.__parent.edit_book()
        
