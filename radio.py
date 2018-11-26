from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QMessageBox


import mpd
import station
import labelClickable
import urllib


import time

HOST = "localhost"
PORT = 6600



class radio():
    def __init__(self, gui, dia):
        self.gui = gui
        self.dia = dia
        self.sDialog = station.SelectStation()
        dia.setStyleSheet("QWidget#Dialog {background-image: url(Music-Record-Vinyl-800-480.jpg);}")
        
        self.infoTimer = QtCore.QTimer()
        self.infoTimer.timeout.connect(self.timercall)
        self.infoTimer.start(5000)
        
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        
        self.labelStation = labelClickable.QLabelClickable(self.dia)
        self.labelStation.setFont(font)
        self.labelStation.setGeometry(28, 415, 750, 60)
        self.labelStation.setText("<font color='lightGray'> Back </font>")
        self.labelStation.clicked.connect(self.selectStation_clicked)
        self.showArtist("")
        self.showSong("")
        self.showStation("Pinguin radio")
        self.showTime()
        self.showPicture("https://pbs.twimg.com/profile_images/1011919547555868672/r-BPzuFQ_400x400.jpg")
        
        self.client = mpd.MPDClient()       # create client object
        self.client.timeout = 2             # network timeout in seconds (floats allowed), default: None
        self.client.idletimeout = None      # timeout for fetching the result of the idle command is handled seperately, default: None
        
        self.number = 0
        self.clear()
        self.addStation("https://streams.pinguinradio.com/PinguinRadio320.mp3")
        print("Starting")
        self.play(self.number)
        self.getShowInfo()
       
       
    def show(self):
        self.dia.show()  
        
    def hide(self):
        self.dia.hide()   
    
       
    def timercall(self):
        self.getShowInfo()
        self.showTime()
  
     
    def selectStation_clicked(self):
        self.sDialog.showSelectStation(self)
        self.hide()
  
    
    def connect(self):
        try:
            self.client.connect(HOST, PORT)
        except:
            print("could not connect")
            
                
    def disconnect(self): 
        try:       
            self.client.close()
            self.client.disconnect()
        except:
            print("could not disconnect")
        
    
    def addStation(self, station):
        self.connect()
        try:
            self.client.add(station)
            print(self.client.playlist())
        except mpd.CommandError:
            print("Station not added")
        self.disconnect()    
    
    
    def clear(self):
        self.connect()
        try:
            self.client.clear()
        except: 
            print("could not play")
        self.disconnect()    
    
    
    def play(self, number):
        self.connect()
        try:
            self.client.play(number)
        except: 
            print("could not play")
        self.disconnect()    
    
    
    def playNew(self, url, name):
        self.clear()
        self.addStation(url)
        self.showStation(name)
        time.sleep(0.5)
        self.connect()
        try:
            self.client.play(0)
        except: 
            print("could not play")
        self.disconnect()    
            
                     
    def getInfo(self):
        self.connect()
        try:
            info = self.client.currentsong()
        except:
            return ""
        print(info)
        self.disconnect()
        return info


    def stop(self):
        self.connect()
        try:
            print("stopping")
            self.client.stop()
        except:
            pass
        
       
    def getShowInfo(self):
        info = self.getInfo()
        song = info.get("title")
        if song != None:
            song = song.split('-')
            self.showArtist(song[0])
            self.showSong(song[1])
           
        
    #################################################################################################
    
    def showStation(self, station):
        self.labelStation.setText("<font color='lightGray'>" + station + "</font>")
 
    
    def showSong(self, song):
        self.gui.labelSong.setText("<font color='white'>" + song + "</font>")
        
        
    def showArtist(self, artist):
        self.gui.labelArtist.setText("<font color='white'>" + artist + "</font>")
        
    
    def showTime(self):
        self.timeString = time.strftime('%H:%M', time.localtime())
        self.gui.labelTime.setText("<font color='white'>" +self.timeString+ "</font>")
        self.dateString = time.strftime("%A %d %B", time.localtime())
        self.gui.labelDate.setText("<font color='white'>" +self.dateString+ "</font>")
        


    def showPicture(self, url):
        try: 
            data = urllib.request.urlopen(url).read()
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(data)
            self.gui.labelPic.resize(200, 200)
            self.gui.labelPic.setPixmap(pixmap.scaled(self.gui.labelPic.size(), QtCore.Qt.IgnoreAspectRatio))
        except:
            pass        

        