import sys
import os.path
from PyQt4 import QtGui,QtCore,uic, Qt

import Config
from Config import *
from ImageViewer import ImageViewerWindow


class GalleryWindow(QtGui.QWidget):
    def __init__(self, MainWindow, Data1, Data2, Data3, *args, **kwargs):
        super(GalleryWindow, self).__init__(*args, **kwargs)
        self.MainWindow = MainWindow
        self.Data1 = Data1
        self.Data2 = Data2
        self.Data3 = Data3
        self.initUI()

    def initUI(self):     
        pointX = self.MainWindow.geometry().topLeft().x() + self.MainWindow.geometry().getRect()[2]
        pointY = self.MainWindow.geometry().topLeft().y()
        sizeX = self.MainWindow.geometry().getRect()[2]
        sizeY = self.MainWindow.geometry().getRect()[3]
        self.setGeometry(pointX, pointY, 400, sizeY)

        self.PictureList = QtGui.QListWidget(self)
        self.PictureList.setGeometry(0, 0, 400, sizeY)
        self.PictureList.setViewMode(QtGui.QListWidget.ListMode)
        self.PictureList.setIconSize(QtCore.QSize(256, 256))
        picture_path = Config.RootFolder + Projects_Folder + self.Data2 + "/" + self.Data3 + "/" + self.Data1 + "/" + picture_Folder
        for picture in os.listdir(picture_path):
            #image_item = Qt.QListWidgetItem(self.PictureList)
            #row = ImageItem(picture_path, picture)
            #self.PictureList.setItemWidget( image_item, row )
            image_item = QtGui.QListWidgetItem(QtGui.QIcon(picture_path + "/" + picture), picture)
            setattr(image_item, "picturePath", picture_path + "/" + picture)
            self.PictureList.addItem(image_item)

        self.PictureList.itemDoubleClicked.connect(self.LaunchImageViewer)

        self.setStyleSheet("background-color: rgb(140, 140, 140)")

    def LaunchImageViewer(self, item):
        self.ImageViewer = self.MainWindow.imageViewerWindow
        self.ImageViewer.addPicture(item.picturePath)
        self.ImageViewer.repaint_ViewMode()
        self.ImageViewer.show()

class ImageItem(QtGui.QWidget):
    def __init__(self, picture_path, picture):
        super(ImageItem, self).__init__()
        print picture_path + "/" + picture
        self.row = QtGui.QVBoxLayout()

        #self.image_item = QtGui.QListWidgetItem(QtGui.QIcon(picture_path + "/" + picture), picture)
        self.image_item = QtGui.QPushButton(QtGui.QIcon(os.path.abspath( picture_path + "/" + picture ) ), picture)
        #setattr(self, name,  QtGui.QPushButton())
        #icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap((Config.RootFolder + Icon_Folder + icon_name + ".png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #getattr(self, name).setIcon(icon)
        #getattr(self, name).setObjectName(_fromUtf8(name))
        #getattr(self, name).setToolTip(ToolTip)
        self.row.addWidget(self.image_item)


        self.textUpQLabel    = QtGui.QLabel("12345")
        self.textDownQLabel  = QtGui.QLabel("67890")
        self.row.addWidget(self.textUpQLabel)
        self.row.addWidget(self.textDownQLabel)


        self.setLayout(self.row)