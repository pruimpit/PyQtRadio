from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore, QtGui, QtWidgets

from functools import partial

import labelClickable
import selectStation


ITEMLIST = [{"name":"Radio 1","url":"https://url1.mp3"},
            {"name":"Radio 2","url":"https://url2.mp3"},
            {"name":"Radio 3","url":"https://url3.mp3"},
            {"name":"Radio 4","url":"https://url4.mp3"},
            {"name":"Radio 5","url":"https://url5.mp3"},
            {"name":"Radio 6","url":"https://url6.mp3"},
            {"name":"Radio 7","url":"https://url7.mp3"},
            {"name":"Radio 8","url":"https://url8.mp3"},
            {"name":"Radio 9","url":"https://url9.mp3"},
            {"name":"Radio 10","url":"https://url10.mp3"}]


class SelectStation(QDialog):
    def __init__(self):
        super().__init__()
        self.selectStation = selectStation.Ui_SelectDialog()
        self.selectStation.setupUi(self)
        self.setStyleSheet("QWidget#SelectDialog {background-image: url(Music-Record-Vinyl.jpg);}")
        self.createLabel(15, 15, "lightGray", "Back", self.pushButton_clicked)
        self.fav_label = self.createLabel(15, 45, "yellow","Favorites", self.favorites_clicked)
        self.shout_label = self.createLabel(15, 75, "lightGray","Shoutcast", self.shoutcast_clicked)
        
        self.displayedMenuItems = []
        self.labelHandler = []
        self.items = ITEMLIST
        
        self.offset = 0
        self.length = 0
        
        
        
    
    def displayMenu(self, offset):
        self.displayedMenuItems = []
        self.labelHandler = []
        length = len(self.items)
        if self.offset > 0:
            self.upButton()
        if (length - offset) > 6:
            self.downButton() 
            nrOfItems = 6
        else:
            nrOfItems = length - offset
        y = 53
        for item in range(offset, nrOfItems):
            self.displayedMenuItems.append(self.items[item].get("url"))
            self.createLabel(240, y, "white", 
                             self.items[item].get("name"), 
                             partial(self.itemCallback ,item))
            y += 37     
        
        
        

    def show(self):
        self.createItemsMenu(self.items)
        super().show()
        
            
    
        
    def createLabel(self, x, y, color, text, connect):
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        label_hdl = labelClickable.QLabelClickable(self)
        label_hdl.setFont(font)
        label_hdl.setGeometry(x, y, 200, 30)
        label_hdl.setText("<font color="+color+">"+text+"</font>")
        if connect != None:
            label_hdl.clicked.connect(connect)
            print("Connect: " + str(connect))
        return label_hdl    
      
    def changeLabel(self, handle, color, text):
        handle.setText("<font color="+color+">"+text+"</font>")
          
        
        
    def showSelectStation(self):
        self.show()
        
    def hideSelectStation(self):
        self.hide()
        

    def pushButton_clicked(self):
        self.hide()    

    def favorites_clicked(self):
        self.changeLabel(self.fav_label, "Yellow", "Favorites")
        self.changeLabel(self.shout_label, "lightGray", "Shoutcast")  
        print("Fav clicked")

    def shoutcast_clicked(self):
        self.changeLabel(self.fav_label, "lightGray", "Favorites")  
        self.changeLabel(self.shout_label, "Yellow", "Shoutcast") 
        print("Fav clicked") 
        
        
    def itemCallback(self, item):
        print(self.displayedMenuItems[item])    
        
    
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
    
    def updateItemsMenu(self, items, offset): 
        y = 53
        endItem = offset + 6    
        index = 0
        print("Offset:" + str(offset))
        for item in range(offset, endItem):
            if item >=0:
                print("item: " + str(item))
                print("index: " + str(index))
                self.displayedMenuItems[index] = items[item].get("url")
                self.changeLabel(self.labelHandler[index], "white", 
                                 items[item].get("name"))
                y += 37
                index += 1
    
        
    def upButton(self):
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setFont(font)
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
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setFont(font)
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
    