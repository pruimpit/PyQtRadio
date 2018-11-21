from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore, QtGui, QtWidgets

from functools import partial

import labelClickable


class selectMenu(QDialog):
    def __init__(self, dialog, items, nrDisplayItems, callBack):
        super().__init__()
        self.dialogParent  = dialog
        self.callback = callBack
        self.displayedMenuItems = []
        self.labelHandler = []
        self.items = items
        self.nrDisplayItems = nrDisplayItems
        self.offset = 0
        self.length = 0
        
        self.font = QtGui.QFont()
        self.font.setFamily("Droid Sans")
        self.font.setPointSize(17)
        self.font.setBold(True)
        self.font.setWeight(75)
        
        self.createItemsMenu(self.items)
  
    def setItems(self, items):
        self.offset = 0
        self.items = items
        self.updateItemsMenu(self.items, self.offset) 
  
        
    def createLabel(self, x, y, color, text, connect):
        label_hdl = labelClickable.QLabelClickable(self.dialogParent)
        label_hdl.setFont(self.font)
        label_hdl.setGeometry(x, y, 230, 30)
        label_hdl.setText("<font color="+color+">"+text+"</font>")
        if connect != None:
            label_hdl.clicked.connect(connect)
            return label_hdl    
      
    def changeLabel(self, handle, color, text):
        handle.setText("<font color="+color+">"+text+"</font>")
          
        
    def itemCallback(self, item):
        self.callback(item + self.offset)
        
    
    def createItemsMenu(self, items):
        self.upButton()
        self.downButton() 
        nrOfItems = len(items)
        self.displayedMenuItems = []
        self.labelHandler = []
        if nrOfItems > 6:
            self.downButton() 
            nrOfItems = 6
        y = 53
        index = 0
        for item in range(0, nrOfItems):
            self.displayedMenuItems.append(items[item].get("url"))
            self.labelHandler.append(self.createLabel(240, y, "white", 
                             items[item].get("name"), 
                             partial(self.itemCallback ,item)))
            index += 1
            y += 37
        # fill out to 6 if needed    
        if  nrOfItems < 6:
            for item in range(nrOfItems, 6 ):
                self.displayedMenuItems.append("")
                self.labelHandler.append(self.createLabel(240, y, "white", 
                             "", partial(self.itemCallback, item)))
                index += 1
                y += 37
            
            
    
    def updateItemsMenu(self, items, offset): 
        y = 53
        nrOfItems = len(items)
        if nrOfItems < 6:
            endItem = nrOfItems
            self.offset = 0
        else:     
            endItem = offset + 6    
        index = 0
        for item in range(offset, endItem):
            if item >=0:
                self.displayedMenuItems[index] = items[item].get("url")
                self.changeLabel(self.labelHandler[index], "white", 
                                 items[item].get("name"))
                y += 37
                index += 1
        # fill out to 6 if needed    
        if  nrOfItems < 6:
            for item in range(nrOfItems, 6 ):
                self.displayedMenuItems[index] = ""
                self.changeLabel(self.labelHandler[index], "white", "")
                
                y += 37
                index+=1    
    
        
    def upButton(self):
        self.pushButton = QtWidgets.QPushButton(self.dialogParent)
        self.pushButton.setFont(self.font)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);selection-color: rgb(0, 0, 0);")
        self.pushButton.setGeometry(QtCore.QRect(240, 10, 150, 30))
        self.pushButton.setObjectName("pushButton")  
        self.pushButton.pressed.connect(self.upPressed)   
        self.pushButton.setText("▲")  
    
    
    def upPressed(self):
        if self.offset > 0:
            self.offset-=1
        self.updateItemsMenu(self.items, self.offset)
    

    def downButton(self):
        self.pushButton = QtWidgets.QPushButton(self.dialogParent)
        self.pushButton.setFont(self.font)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);selection-color: rgb(0, 0, 0);")
        self.pushButton.setGeometry(QtCore.QRect(240, 280, 150, 30))
        self.pushButton.setObjectName("pushButton")   
        self.pushButton.pressed.connect(self.downPressed)   
        self.pushButton.setText("▼")  
    
 
    def downPressed(self):
        if self.offset < (len(self.items)-6):
            self.offset+=1
        self.updateItemsMenu(self.items, self.offset)
    