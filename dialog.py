# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet("")
        self.labelArtist = QtWidgets.QLabel(Dialog)
        self.labelArtist.setGeometry(QtCore.QRect(30, 20, 751, 51))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.labelArtist.setFont(font)
        self.labelArtist.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.labelArtist.setAutoFillBackground(False)
        self.labelArtist.setObjectName("labelArtist")
        self.labelTime = QtWidgets.QLabel(Dialog)
        self.labelTime.setGeometry(QtCore.QRect(350, 150, 441, 181))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(120)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.labelTime.setFont(font)
        self.labelTime.setObjectName("labelTime")
        self.labelSong = QtWidgets.QLabel(Dialog)
        self.labelSong.setGeometry(QtCore.QRect(30, 90, 751, 51))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.labelSong.setFont(font)
        self.labelSong.setObjectName("labelSong")
        self.labelPic = QtWidgets.QLabel(Dialog)
        self.labelPic.setGeometry(QtCore.QRect(30, 160, 59, 14))
        self.labelPic.setObjectName("labelPic")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelArtist.setText(_translate("Dialog", "Artist"))
        self.labelTime.setText(_translate("Dialog", "22:22"))
        self.labelSong.setText(_translate("Dialog", "Song"))
        self.labelPic.setText(_translate("Dialog", "Pic"))

