from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore, QtGui, QtWidgets

from functools import partial

import labelClickable
import selectStation
import selectmenu
import json
"""
FAVLIST = [{"name":"Radio 1","url":"https://url1.mp3"},
            {"name":"Radio 2","url":"https://url2.mp3"},
            {"name":"Radio 3","url":"https://url3.mp3"},
            {"name":"Radio 4","url":"https://url4.mp3"},
            {"name":"Radio 5","url":"https://url5.mp3"},
            {"name":"Radio 6","url":"https://url6.mp3"},
            {"name":"Radio 7","url":"https://url7.mp3"},
            {"name":"Radio 8","url":"https://url8.mp3"},
            {"name":"Radio 9","url":"https://url9.mp3"},
            {"name":"Radio 10","url":"https://url10.mp3"}]
"""
SHOUTLIST = [{"name":"Shout 1","url":"https://url1.mp3"},
            {"name":"Shout 2","url":"https://url2.mp3"},
            {"name":"Shout 3","url":"https://url3.mp3"},
            {"name":"Shout 4","url":"https://url4.mp3"},
            {"name":"Shout 5","url":"https://url5.mp3"},
            {"name":"Shout 6","url":"https://url6.mp3"},
            {"name":"Shout 7","url":"https://url7.mp3"},
            {"name":"Shout 8","url":"https://url8.mp3"},
            {"name":"Shout 9","url":"https://url9.mp3"},
            {"name":"Shout 10","url":"https://url10.mp3"}]



class SelectStation(QDialog):
    def __init__(self):
        super().__init__()
        self.selectStation = selectStation.Ui_SelectDialog()
        self.selectStation.setupUi(self)
        self.setStyleSheet("QWidget#SelectDialog {background-image: url(Music-Record-Vinyl.jpg);}")
        self.createLabel(15, 15, "lightGray", "Back", self.backButton_clicked)
        self.fav_label = self.createLabel(15, 45, "yellow","Favorites", self.favorites_clicked)
        self.shout_label = self.createLabel(15, 75, "lightGray","Shoutcast", self.shoutcast_clicked)
        self.readFavorites()
        self.items = self.favorites
        self.sMenu = selectmenu.selectMenu(self, self.items, 6, self.itemSelected)
        
        
        
    def readFavorites(self):
        try:
            with open("favorites.json") as json_data:
                self.favorites = json.load(json_data)
                print(self.favorites)
        except Exception as msg:
            print("file problem:" + str(msg))
        return           

    def show(self):
        self.favorites_clicked()
        super().show()
        
    def itemSelected(self, item):
        print("Item selected: " + str(item))
        print("Name: " + self.items[item].get("name") + " url: " + self.items[item].get("url") )
        self.radio.playNew(self.items[item].get("url") ,self.items[item].get("name"))
        self.hide()  
    
        
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
    
        
    def showSelectStation(self, radio):
        self.items = self.favorites
        self.radio = radio
        self.sMenu.setItems(self.items)
        self.show()
 
        
    def hideSelectStation(self):
        self.hide()
        

    def backButton_clicked(self):
        self.hide()    


    def favorites_clicked(self):
        self.changeLabel(self.fav_label, "Yellow", "Favorites")
        self.changeLabel(self.shout_label, "lightGray", "Shoutcast")  
        self.items = self.favorites
        self.sMenu.setItems(self.items)

        
    def shoutcast_clicked(self):
        self.changeLabel(self.fav_label, "lightGray", "Favorites")  
        self.changeLabel(self.shout_label, "Yellow", "Shoutcast") 
        self.items = SHOUTLIST
        self.sMenu.setItems(self.items)
