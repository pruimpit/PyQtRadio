from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog

import labelClickable
import selectStation
import selectmenu
import json
import tunein
import urllib
import soma
import plparser

selectXpos = 250
normalcolor = "#b1b1b1"
highlight = "White" 

class SelectStation(QDialog):
    def __init__(self):
        super().__init__()
        self.selectStation = selectStation.Ui_SelectDialog()
        self.selectStation.setupUi(self)
        self.setStyleSheet("QWidget#SelectDialog {background-image: url(Music-Record-Vinyl-800-480.jpg);}")
        self.createLabel(15, 15, normalcolor, "Back", self.backButton_clicked)
        self.fav_label = self.createLabel(15, 65, highlight, "Favorites", self.favorites_clicked)
        self.tuneIn_label = self.createLabel(15, 115, normalcolor,"TuneIn", self.tuneIn_clicked)
        self.somafm_label = self.createLabel(15, 165, normalcolor,"SomaFm", self.somafm_clicked)
        self.readFavorites()
        self.items = self.favorites
        self.tuneIn = tunein.openRadio()
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
            image = self.items[item].get("image")
            print(image)
            if image != None:
                self.radio.showPicture(image)
            self.radio.showArtist("")
            self.radio.showSong("")
            self.radio.show()    
            self.hide()
        else:
            self.items = self.tuneIn.getNextLayer(self.items[item].get("url"))
            self.sMenu.setItems(self.items)
              
        
    def createLabel(self, x, y, color, text, connect):
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        label_hdl = labelClickable.QLabelClickable(self)
        label_hdl.setFont(font)
        label_hdl.setGeometry(x, y, 300, 50)
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
        self.radio.show()
        self.hide()
        

    def backButton_clicked(self):
        self.radio.show()
        self.hide()    


    def favorites_clicked(self):
        self.changeLabel(self.fav_label, highlight, "Favorites")
        self.changeLabel(self.tuneIn_label, normalcolor, "TuneIn") 
        self.changeLabel(self.somafm_label, normalcolor, "SomaFm") 
        self.items = self.favorites
        self.menu = "Favorites"
        self.sMenu.setItems(self.items)
    
     
    def tuneIn_clicked(self):
        self.changeLabel(self.fav_label, normalcolor, "Favorites") 
        self.changeLabel(self.tuneIn_label, highlight, "TuneIn")  
        self.changeLabel(self.somafm_label, normalcolor, "SomaFm") 
        self.items = self.tuneIn.getOverview()
        self.menu = "tuneIn"
        self.sMenu.setItems(self.items)
    
            
    def somafm_clicked(self):
        self.changeLabel(self.fav_label, normalcolor, "Favorites")  
        self.changeLabel(self.tuneIn_label, normalcolor, "TuneIn") 
        self.changeLabel(self.somafm_label, highlight, "SomaFm")
        self.items = soma.get_stations()
        self.menu = "Somafm"
        self.sMenu.setItems(self.items)
        
        
        
        
        
