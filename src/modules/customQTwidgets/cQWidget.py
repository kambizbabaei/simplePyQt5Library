from PyQt5.QtWidgets import QWidget


class customQWidget(QWidget): 
    """
    this class implement right click menu for each instance of it self ,context menu provided from event_ obj
    """
    def __init__(self,parent = None,event_=None):
        """
        for initializing the class : you should put an event object as input
        which contains this method: context_menu_event(parent,event)
        if this requrement doesnt satisfy right click will have no impact
        on running proccess
        """
        QWidget.__init__(self,parent)
        self.event_=event_
        self.setAutoFillBackground(True)

    def contextMenuEvent(self, event ) -> None:
        """
        this method recive a method as input and run the method when right click occurred
        param event contains click information like pos
        """
        if self.event_ is not None:
            self.event_.context_menu_event(self,event)
            