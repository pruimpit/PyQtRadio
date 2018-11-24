from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore, QtGui, QtWidgets

from functools import partial

import labelClickable
import selectStation
import selectmenu
import json
import openradio
import urllib
from urllib.request import Request
from urllib.request import urlopen
import soma
import plparser

selectXpos = 180

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
        self.tuneIn_label = self.createLabel(15, 75, "lightGray","TuneIn", self.tuneIn_clicked)
        self.somafm_label = self.createLabel(15, 105, "lightGray","SomaFm", self.somafm_clicked)
        self.shout_label = self.createLabel(15, 135, "lightGray","Shoutcast", self.shoutcast_clicked)
        self.readFavorites()
        self.items = self.favorites
        self.tuneIn = openradio.openRadio()
        self.sMenu = selectmenu.selectMenu(self, self.items, 6, selectXpos, self.itemSelected)
        self.menu = "Favorites"      
        
        
        
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
        if self.items[item].get("type") == "audio":
            print("Item selected: " + str(item))
            print("Name: " + self.items[item].get("name") + " url: " + self.items[item].get("url") )
            if self.menu == "tuneIn":
                print("new url:" + self.items[item].get("url"))
                url = self.tuneIn.getStreamUrl(self.items[item].get("url")).splitlines()[0]
                print("URRLL")
                print(url)
            else:
                url = self.items[item].get("url")
            if (".pls" in url) or (".m3u" in url):
                try:
                    print("playlist detected")
                    req = urllib.request.urlopen(url)
                    file = req.read()
                    url = plparser.parse(filename=url, filedata=file).Tracks[0].File
                except Exception as msg:
                    print(msg)    
            print("going to play:")        
            self.radio.playNew(url, self.items[item].get("name"))
            print("playing:") 
            self.hide()
        else:
            self.items = self.tuneIn.getNextLayer(self.items[item].get("url"))
            self.sMenu.setItems(self.items)
              
    
        
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
        self.changeLabel(self.tuneIn_label, "lightGray", "TuneIn") 
        self.changeLabel(self.shout_label, "lightGray", "Shoutcast") 
        self.changeLabel(self.somafm_label,"lightGray","SomaFm") 
        self.items = self.favorites
        self.menu = "Favorites"
        self.sMenu.setItems(self.items)

        
    def shoutcast_clicked(self):
        self.changeLabel(self.fav_label, "lightGray", "Favorites")  
        self.changeLabel(self.tuneIn_label, "Yellow", "TuneIn") 
        self.changeLabel(self.shout_label, "lightGray", "Shoutcast") 
        self.changeLabel(self.somafm_label,"lightGray","SomaFm")
        self.items = SHOUTLIST
        self.menu = "Shoutcast"
        self.sMenu.setItems(self.items)
        
     
    def tuneIn_clicked(self):
        self.changeLabel(self.fav_label, "lightGray", "Favorites") 
        self.changeLabel(self.tuneIn_label, "Yellow", "TuneIn")  
        self.changeLabel(self.shout_label, "lightGray", "Shoutcast")
        self.changeLabel(self.somafm_label,"lightGray","SomaFm") 
        self.items = self.tuneIn.getOverview()
        self.menu = "tuneIn"
        self.sMenu.setItems(self.items)
            
    def somafm_clicked(self):
        self.changeLabel(self.fav_label, "lightGray", "Favorites")  
        self.changeLabel(self.tuneIn_label, "lightGray", "TuneIn") 
        self.changeLabel(self.shout_label, "lightGray", "Shoutcast") 
        self.changeLabel(self.somafm_label,"Yellow","SomaFm")
        self.items = soma.get_stations()
        self.menu = "Somafm"
        self.sMenu.setItems(self.items)
        
        
        
        
        
