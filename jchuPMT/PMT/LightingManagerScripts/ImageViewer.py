import sys
import os.path
from PyQt4 import QtGui, QtCore, uic

from Config import *
from PIL import Image, ImageQt
import math


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

"""
This is the viewer
"""
class ImageViewerWindow(QtGui.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ImageViewerWindow, self).__init__(*args, **kwargs)
        self.setGeometry(50, 150, 1280, 720)
        self.setWindowTitle(ImageViewerWindowTitle)
        self.value = 50
        self.pictureList = []

        self.horizontalSlider = QtGui.QSlider(self)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 670, 1260, 22))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setProperty("value", 50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalSlider.valueChanged.connect(self.refresh_ViewMode)

        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.setMenuBar(self.menubar)
        self.actionExit = QtGui.QAction(self)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSave = QtGui.QAction(self)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionClear = QtGui.QAction(self)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionAlbum_Mode = QtGui.QAction(self)
        self.actionAlbum_Mode.setObjectName(_fromUtf8("actionAlbum_Mode"))
        self.actionCompare_Mode = QtGui.QAction(self)
        self.actionCompare_Mode.setObjectName(_fromUtf8("actionCompare_Mode"))
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionClear)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionAlbum_Mode)
        self.menuEdit.addAction(self.actionCompare_Mode)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "View", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionClear.setText(_translate("MainWindow", "Clear", None))
        self.actionAlbum_Mode.setText(_translate("MainWindow", "Album Mode", None))
        self.actionCompare_Mode.setText(_translate("MainWindow", "Compare Mode", None))
        
    def addPicture(self, picturePath):
        self.pictureList.append(picturePath)
        if len(self.pictureList) > 2:
            self.pictureList.remove(self.pictureList[0])

    def repaint_ViewMode(self):
        print self.value
        if len(self.pictureList) > 1:
            self.horizontalSlider.setVisible(True)
        else:
            self.horizontalSlider.setVisible(False)
            
        count = 0
        self.centralwidget = QtGui.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        for picture in self.pictureList:
            pixmap = QtGui.QPixmap(picture)
            pixmap = pixmap.scaled(4096, 720, QtCore.Qt.KeepAspectRatio)
            setattr(self, "label" + str(count), QtGui.QLabel('', self.centralwidget))
            getattr(self, "label" + str(count)).setGeometry(0, 0, 1280, 720)
            getattr(self, "label" + str(count)).setPixmap(pixmap)
            if count == 1:
                positionX = 1280 * self.value * 0.01
                sizeX = 1280 - positionX
                getattr(self, "label" + str(count)).setGeometry(positionX, 0, sizeX, 720)
                getattr(self, "label" + str(count)).setPixmap(pixmap)

                getattr(self, "label" + str(count)).setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

            count += 1
        self.horizontalSlider.raise_()

    def refresh_ViewMode(self, value):
        self.value = value
        count = 0
        for picture in self.pictureList:
            getattr(self, "label" + str(count)).setGeometry(0, 0, 1280, 720)
            if count == 1:
                positionX = 1280 * self.value * 0.01
                sizeX = 1280 - positionX
                getattr(self, "label" + str(count)).setGeometry(positionX, 0, sizeX, 720)

                getattr(self, "label" + str(count)).setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

            count += 1
        self.horizontalSlider.raise_()