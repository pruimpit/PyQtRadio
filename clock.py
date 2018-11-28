from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon, QPixmap

import clockDialog
import labelClickable
import random
import platform 



class Clock(QDialog):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.clock = clockDialog.Ui_Dialog()
        self.clock.setupUi(self)
        self.setStyleSheet("QWidget#Clock {background-color: rgb(0, 0, 0);}")
        self.exitArea = self.createLabel(0, 0, 800, 480, "White", "", self.hide)
        random.seed()

    
    def show(self):
        if "arm" in platform.machine(): 
            import rpi_backlight as bl
            bl.set_brightness(11)
        ypos = random.randint(0, 220)
        self.clock.labelTime.setGeometry(QtCore.QRect(190, ypos, 441, 181))
        self.clock.labelDate.setGeometry(QtCore.QRect(190, ypos+180, 481, 51))
        self.radio.sDialog.hideSelectStation()
        self.radio.stop()
        super().show()

    def hide(self):
        if "arm" in platform.machine(): 
            import rpi_backlight as bl
            bl.set_brightness(255)
        self.radio.play(0)
        super().hide()

    
    
    def createLabel(self, xpos, ypos, x, y, color, text, connect):
        label_hdl = labelClickable.QLabelClickable(self)
        label_hdl.setGeometry(xpos, ypos, x, y)
        label_hdl.setText("<font color="+color+">"+text+"</font>")
        if connect != None:
            label_hdl.clicked.connect(connect)
            return label_hdl            
