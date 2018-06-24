import sys
import os.path
from PyQt4 import QtGui,QtCore,uic

import Config
from Config import *
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



class PopupWindow_MoveScene(PopupWindow):
    ''' This class controls all othe interface between the GUI and Maya'''
    def __init__(self, parent, Data1 = "", Data2 = "", Data3 = "", *args, **kwargs):
        '''Constructor for your GUI class'''
        super(PopupWindow_MoveScene, self).__init__(parent, Popup_Move_FileName, "Move", Data1, Data2, Data3, *args, **kwargs)
        self.bindMyButtons()                                      # Call the GUI configuration

    def bindMyButtons(self):
        """"""
        self.btnOK.clicked.connect(self.fOK)
        self.Type.setText("To")
        for element in os.listdir(Config.RootFolder + Projects_Folder):
            self.comboBox.addItem(element)
        
    def fOK(self):
        """"""
        if self.A_Option1.isChecked() != True:
            self.CustomCopy()
        else:
            shutil.move(os.path.abspath(Config.RootFolder + Projects_Folder + self.Data2 + "/" + self.Data1), os.path.abspath(Config.RootFolder + Projects_Folder + self.comboBox.currentText() + "/" + self.Data1))
        self.parent.refresh()
        self.close()

    def CustomCopy(self, surfix = ""):
            try:
                shutil.copytree(os.path.abspath(Config.RootFolder + Projects_Folder + self.Data2 + "/" + self.Data1), os.path.abspath(Config.RootFolder + Projects_Folder + self.comboBox.currentText() + "/" + self.Data1 + surfix))
            except:
                surfix = surfix + "_Copy"
                self.CustomCopy(surfix)

class PopupWindow_MoveLighting(PopupWindow):
    ''' This class controls all othe interface between the GUI and Maya'''
    def __init__(self, parent, Data1 = "", Data2 = "", Data3 = "", *args, **kwargs):
        '''Constructor for your GUI class'''
        super(PopupWindow_MoveLighting, self).__init__(parent, Popup_Move_FileName, "Move", Data1, Data2, Data3, *args, **kwargs)
        self.bindMyButtons()                                      # Call the GUI configuration
        
    def bindMyButtons(self):
        """"""
        self.btnOK.clicked.connect(self.fOK)
        self.Type.setText("To")
        for element in os.listdir(Config.RootFolder + Projects_Folder ):
            path_info = Config.RootFolder + Projects_Folder + "/" + element
            if os.path.isdir(path_info):
                for scene in os.listdir(path_info):
                    if scene != "config" and scene != "temp":
                        self.comboBox.addItem(element + "/" + scene)
        
    def fOK(self):
        """"""
        if self.A_Option1.isChecked() != True:
            self.CustomCopy()
        else:
            shutil.move(os.path.abspath(Config.RootFolder + Projects_Folder + self.Data2 + "/" + self.Data3 + "/" + self.Data1), os.path.abspath(Config.RootFolder + Projects_Folder + self.comboBox.currentText() + "/" + self.Data1))
        self.parent.refresh()
        self.close()

    def CustomCopy(self, surfix = ""):
            try:
                shutil.copytree(os.path.abspath(Config.RootFolder + Projects_Folder + self.Data2 + "/" + self.Data3 + "/" + self.Data1), os.path.abspath(Config.RootFolder + Projects_Folder + self.comboBox.currentText() + "/" + self.Data1 + surfix))
            except:
                surfix = surfix + "_Copy"
                self.CustomCopy(surfix)