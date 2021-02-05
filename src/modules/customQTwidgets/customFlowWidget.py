from PyQt5.QtGui import  QResizeEvent
from PyQt5.QtWidgets import (
    QGridLayout, QGroupBox, 
    QScrollArea, QWidget
)

class FlowWidget(QWidget):
    def __init__(self, parent ):
        super().__init__(parent=parent)
        self.minwidth = 100
        self.minheight = 100
        self.items = list()
        gb = QGroupBox()
        self.items_layout = QGridLayout()
        gb.setLayout(self.items_layout)
        scrol = QScrollArea ()
        scrol.setWidget(gb)
        scrol.setWidgetResizable(True)
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(scrol)
        self.items_layout.setSpacing(0)
        self.parent_ = parent

    def getParent(self):
        return self.parent_
                    
    def draw(self):
        col_c = int(self.width()/self.minwidth)
        if col_c == 0:
            col_c = 1
        for i in range(len(self.items)):
            widget = self.items[i]            
            self.items_layout.addWidget(widget,int(i/col_c),int(i%col_c))
                
    def addWidget(self,widget:QWidget):
        self.items.append(widget)
        if widget.minimumHeight()>self.minheight:
            self.minheight = widget.minimumHeight()

        if widget.minimumWidth() > self.minwidth:
            self.minwidth = widget.minimumWidth()
        self.draw()
        
    def resizeEvent(self, a0: QResizeEvent):
        super().resizeEvent(a0)
        self.draw()

    def removeItem(self,widget):
        for i in self.items:
            if i == widget:
                self.items.remove(i)
            self.items_layout.removeWidget(i)
            
            i.close()
            i.setDisabled(True)
            i.setParent(None)
        self.draw()

