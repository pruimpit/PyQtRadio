from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog



import labelClickable
import selectStation


class SelectStation(QDialog):
    def __init__(self):
        super().__init__()
        self.selectStation = selectStation.Ui_SelectDialog()
        self.selectStation.setupUi(self)
        self.setStyleSheet("QWidget#SelectDialog {background-image: url(Music-Record-Vinyl.jpg);}")
        
      
        self.createLabel(15, 15, "lightGray", "Back", self.pushButton_clicked)
        self.fav_label = self.createLabel(15, 45, "yellow","Favorites", self.favorites_clicked)
        self.shout_label = self.createLabel(15, 75, "lightGray","Shoutcast", self.shoutcast_clicked())
    
        
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

    def shoutcast_clicked(self):
        self.changeLabel(self.fav_label, "lightGray", "Favorites")  
        self.changeLabel(self.shout_label, "Yellow", "Shoutcast")  
        
    



