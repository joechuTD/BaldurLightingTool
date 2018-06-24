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



class PopupWindow_RenameProject(PopupWindow):
    ''' This class controls all othe interface between the GUI and Maya'''
    def __init__(self, parent, Data1 = "", Data2 = "", Data3 = "", *args, **kwargs):
        '''Constructor for your GUI class'''
        super(PopupWindow_RenameProject, self).__init__(parent, Popup_Create_FileName, "Rename Project", Data1, Data2, Data3, *args, **kwargs)
        self.oDCCPathFunction = DCCPathFunction()
        self.bindMyButtons()                                      # Call the GUI configuration
        
    def bindMyButtons(self):
        ''' Here is the location where you should bind all of your buttons and events
        Since you will not need to generate a python Script to drive the UI '''
        self.groupBox.setTitle("New Project Name")
        self.btnOK.clicked.connect(self.fOK)
        #self.btnAdd.clicked.connect(self.AddPath)

        for DCC in self.oDCCPathFunction.DCCPathList:
            DCCName = self.oDCCPathFunction.DCCDict[DCC]
            self.comboBox.addItem(DCCName)
 
    def fOK(self):
        inputName = self.inputName.text()
        if inputName != "":
            os.rename(os.path.abspath(Config.RootFolder + Projects_Folder + "/" + self.Data1), os.path.abspath(Config.RootFolder + Projects_Folder + inputName.toUtf8()))
            configFile = open(os.path.abspath(Config.RootFolder + Projects_Folder + inputName.toUtf8() + "/" + config_Folder + "/" + "config.txt"),"w")
            DCCstring = (self.comboBox.currentText().toUtf8() + "Path").replace(".", "_")
            DCCPath = getattr(self.oDCCPathFunction, str(DCCstring))
            configFile.write(DCCPath)
            configFile.close()

            self.parent.refresh()
            self.close()
        else :
            QtGui.QMessageBox.warning(self, "Message", \
                    "Input name could not be empty!", \
                    QtGui.QMessageBox.Ok)

class PopupWindow_RenameScene(PopupWindow):
    ''' This class controls all othe interface between the GUI and Maya'''
    def __init__(self, parent, Data1 = "", Data2 = "", Data3 = "", *args, **kwargs):
        '''Constructor for your GUI class'''
        super(PopupWindow_RenameScene, self).__init__(parent, Popup_Rename_FileName, "Rename Scene", Data1, Data2, Data3, *args, **kwargs)
        self.bindMyButtons()                                      # Call the GUI configuration
        
    def bindMyButtons(self):
        """"""
        self.btnOK.clicked.connect(self.fOK)

    def fOK(self):
        """"""
        if self.inputName.text() != "":
            os.rename(os.path.abspath(Config.RootFolder + Projects_Folder + self.Data2 + "/" + self.Data1), os.path.abspath(Config.RootFolder + Projects_Folder + self.Data2 + "/" + self.inputName.text()))
            self.parent.refresh()
            self.close()

class PopupWindow_RenameLighting(PopupWindow):
    ''' This class controls all othe interface between the GUI and Maya'''
    def __init__(self, parent, Data1 = "", Data2 = "", Data3 = "", *args, **kwargs):
        '''Constructor for your GUI class'''
        super(PopupWindow_RenameLighting, self).__init__(parent, Popup_Rename_FileName, "Rename Lighting", Data1, Data2, Data3, *args, **kwargs)
        self.bindMyButtons()                                      # Call the GUI configuration
        
    def bindMyButtons(self):
        """"""
        self.btnOK.clicked.connect(self.fOK)

    def fOK(self):
        """"""
        if self.inputName.text() != "":
            os.rename(os.path.abspath(Config.RootFolder + Projects_Folder + self.Data2 + "/" + self.Data3 + "/" + self.Data1), os.path.abspath(Config.RootFolder + Projects_Folder + self.Data2 + "/" + self.Data3 + "/" + self.inputName.text()))
            self.parent.refresh()
            self.close()