import sys
import os.path
from PyQt4 import QtGui,QtCore,uic

import Config
from Config import *
from Gallery import GalleryWindow
import shutil



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



class PopupWindow(QtGui.QWidget):
    ''' This class controls all othe interface between the GUI and Maya'''
    def __init__(self, parent, WindowName, TitleName, Data1, Data2, Data3, *args, **kwargs):
        '''Constructor for your GUI class'''
        super(PopupWindow, self).__init__(*args, **kwargs)    # Initialize the class as a typical QWidget class
        self.setParent(parent)                        # Make this new Gui a child of the Maya manin window
        self.parent = parent
        self.Data1 = Data1
        self.Data2 = Data2
        self.Data3 = Data3
        self.setWindowFlags(QtCore.Qt.Window)
        self.initUI(WindowName, TitleName)                                        # Call the GUI configuration
        
    def initUI(self, WindowName, titleName):
        ''' Create the GUI and pass off the interface bindings '''

        #loader = QUiLoader()                                # A loader is a special device in QtUiTools
        currentDir = os.path.abspath(Config.RootFolder + UI_Folder)                # Get the unbiased path to your UI file
        uiFile = QtCore.QFile(currentDir + "/" + WindowName)        # A QfILE IS A SPECIAL qTio DEVICE for handling file streams
        uiFile.open(QtCore.QFile.ReadOnly)                        # Open the stream as read only
        self.ui = uic.loadUi(uiFile, self)   # Convert the UI file from xml to python and send the stream to the Class' UI
        uiFile.close()                                     # Close the File

        self.setWindowTitle(_fromUtf8(titleName))
        self.btnCancel.clicked.connect(self.close)



class PopupWindow_Info(PopupWindow):
    ''' This class controls all othe interface between the GUI and Maya'''
    def __init__(self, parent, Data1 = "", Data2 = "", Data3 = "", *args, **kwargs):
        '''Constructor for your GUI class'''
        super(PopupWindow_Info, self).__init__(parent, Popup_Info_FileName, "Project Info", Data1, Data2, Data3, *args, **kwargs)
        self.bindMyButtons()                                      # Call the GUI configuration

    def bindMyButtons(self):
        """"""
        self.btnOK.clicked.connect(self.fOK)
        self.groupBox.setTitle("To Do List")

    def fOK(self):
        """"""

        self.close()



class PopupWindow_Lighting(QtGui.QWidget):
    ''' This class controls all othe interface between the GUI and Maya'''
    def __init__(self, parent, WindowName, TitleName, Data1, Data2, Data3, *args, **kwargs):
        '''Constructor for your GUI class'''
        super(PopupWindow_Lighting, self).__init__(*args, **kwargs)    # Initialize the class as a typical QWidget class
        self.setParent(parent)                        # Make this new Gui a child of the Maya manin window
        self.parent = parent
        self.Data1 = Data1
        self.Data2 = Data2
        self.Data3 = Data3
        self.TitleName = TitleName
        self.setWindowFlags(QtCore.Qt.Window)

    def show(self):
        """"""
        self.Gallery = GalleryWindow(self.parent, self.Data1, self.Data2, self.Data3)
        self.Gallery.setWindowTitle(self.TitleName + " of " + self.Data2 + "/" + self.Data3 + "/" + self.Data1)
        self.Gallery.show()



class PopupWindow_AddByFolder(QtGui.QWidget):
    def __init__(self, parent, Data1 = "", Data2 = "", Data3 = "", *args, **kwargs):
        super(PopupWindow_AddByFolder, self).__init__(*args, **kwargs)
        self.parent = parent
        self.Data1 = Data1
        self.Data2 = Data2
        self.Data3 = Data3
        self.setupUI(self)

    def setupUI(self, Config):
        Config.setObjectName(_fromUtf8("Config"))
        Config.resize(414, 170)
        self.verticalLayoutWidget = QtGui.QWidget(Config)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(310, 10, 101, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnOK = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnOK.setObjectName(_fromUtf8("btnOK"))
        self.verticalLayout.addWidget(self.btnOK)
        self.btnCancel = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.verticalLayout.addWidget(self.btnCancel)
        self.groupBox = QtGui.QGroupBox(Config)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 291, 151))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.RootFolderPath = QtGui.QLineEdit(self.groupBox)
        self.RootFolderPath.setGeometry(QtCore.QRect(110, 20, 161, 20))
        self.RootFolderPath.setObjectName(_fromUtf8("RootFolderPath"))
        self.RootFolderPath_broswer = QtGui.QPushButton(self.groupBox)
        self.RootFolderPath_broswer.setGeometry(QtCore.QRect(270, 20, 21, 21))
        self.RootFolderPath_broswer.setText(_fromUtf8(""))        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(RootFolder + "Icon/" + "folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RootFolderPath_broswer.setIcon(icon)
        self.RootFolderPath_broswer.setObjectName(_fromUtf8("RootFolderPath_broswer"))


        self.retranslateUi(Config)
        QtCore.QMetaObject.connectSlotsByName(Config)

    def retranslateUi(self, Config):
        Config.setWindowTitle(_translate("Config", "Add Pictures from A Folder", None))
        self.btnOK.setText(_translate("Config", "OK", None))
        self.btnCancel.setText(_translate("Config", "Cancel", None))
        self.groupBox.setTitle(_translate("Config", "Select A Folder to Load from", None))
        self.label.setText(_translate("Config", "Folder Path", None))

        self.RootFolderPath.setText(os.path.abspath(RootFolder + Projects_Folder + self.Data2 + "/" + self.Data3 +  "/" + self.Data1 + "/" + picture_Folder))
        self.RootFolderPath_broswer.clicked.connect(self.fRootFolderPath_broswer)
        self.btnOK.clicked.connect(self.fOK)
        self.btnCancel.clicked.connect(self.fQuit)

    def fRootFolderPath_broswer(self):
        Directory = QtGui.QFileDialog.getExistingDirectory()
        if Directory != "":
            self.RootFolderPath.setText(Directory)

    def fOK(self):
        self.CopyFileFromFolder()
        self.close()

    def fQuit(self):
        QtCore.QCoreApplication.quit()

    def CopyFileFromFolder(self, surfix = ""):
        try:
            shutil.copytree(os.path.abspath(RootFolder + Projects_Folder + self.Data2 + "/" + self.Data1), os.path.abspath(RootFolder + Projects_Folder + self.comboBox.currentText() + "/" + self.Data1 + surfix))
        except:
            surfix = surfix + "_Copy"
            self.CopyFileFromFolder(surfix)



class PopupWindow_AddByFile(QtGui.QWidget):
    def __init__(self, parent, Data1 = "", Data2 = "", Data3 = "", *args, **kwargs):
        super(PopupWindow_AddByFile, self).__init__(*args, **kwargs)
        self.parent = parent
        self.Data1 = Data1
        self.Data2 = Data2
        self.Data3 = Data3
        self.setupUI(self)

    def setupUI(self, Config):
        Config.setObjectName(_fromUtf8("Config"))
        Config.resize(414, 170)
        self.verticalLayoutWidget = QtGui.QWidget(Config)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(310, 10, 101, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnOK = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnOK.setObjectName(_fromUtf8("btnOK"))
        self.verticalLayout.addWidget(self.btnOK)
        self.btnCancel = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.verticalLayout.addWidget(self.btnCancel)
        self.groupBox = QtGui.QGroupBox(Config)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 291, 151))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.RootFolderPath = QtGui.QLineEdit(self.groupBox)
        self.RootFolderPath.setGeometry(QtCore.QRect(110, 20, 161, 20))
        self.RootFolderPath.setObjectName(_fromUtf8("RootFolderPath"))
        self.RootFolderPath_broswer = QtGui.QPushButton(self.groupBox)
        self.RootFolderPath_broswer.setGeometry(QtCore.QRect(270, 20, 21, 21))
        self.RootFolderPath_broswer.setText(_fromUtf8(""))        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(RootFolder + "Icon/" + "folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RootFolderPath_broswer.setIcon(icon)
        self.RootFolderPath_broswer.setObjectName(_fromUtf8("RootFolderPath_broswer"))


        self.retranslateUi(Config)
        QtCore.QMetaObject.connectSlotsByName(Config)

    def retranslateUi(self, Config):
        Config.setWindowTitle(_translate("Config", "Config", None))
        self.btnOK.setText(_translate("Config", "OK", None))
        self.btnCancel.setText(_translate("Config", "Cancel", None))
        self.groupBox.setTitle(_translate("Config", "Folder Path", None))
        self.label.setText(_translate("Config", "Root Folder", None))

        self.RootFolderPath.setText(RootFolder)
        self.RootFolderPath_broswer.clicked.connect(self.fRootFolderPath_broswer)
        self.btnOK.clicked.connect(self.fOK)
        self.btnCancel.clicked.connect(self.fQuit)

    def fRootFolderPath_broswer(self):
        Directory = QtGui.QFileDialog.getExistingDirectory()
        if Directory != "":
            self.RootFolderPath.setText(Directory)

    def fOK(self):
        print self.RootFolderPath.text()
        RootFolder = self.RootFolderPath.text()
        self.parent = MainWindow()
        self.parent.show()
        self.close()

    def fQuit(self):
        QtCore.QCoreApplication.quit()