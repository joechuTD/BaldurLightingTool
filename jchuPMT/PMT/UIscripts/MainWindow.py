import sys
import os
from PyQt4 import Qt,QtGui,QtCore,uic

import Config
from Config import *
from btnCreate import PopupWindow_actionCreateProject
from TreeWidget import RefreshTree
from ImageViewer import *

print sys.path
print os.path.abspath( sys.path[0] + "/" + "Data" + "/" + UI_Folder + MainWindowFile)
Ui_MainWindow, QtBaseClass = uic.loadUiType(os.path.abspath( sys.path[0] + "/" + "Data" + "/" + UI_Folder + MainWindowFile))

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    """ the main class of this calculator, used as a socket to connect to the other classes """

    def __init__(self):
        """ the constuctor for TriangleCalculator """
        #set up for Qt
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.imageViewerWindow = ImageViewerWindow()
        #set up tree widget
        self.RefreshTree = RefreshTree(self.treeWidget, self)
        self.refresh()
        #set up bindings for Qt
        self.setUpBindings()

    def setUpBindings(self):
        """ set up bindings for Qt """
        self.setWindowTitle(MainWindowTitle)
        #set up Main Button
        #self.actionCreateProject.triggered.connect(self.Popup_CreateProject_show)
        #self.actionRefresh.triggered.connect(self.refresh)
        self.btnCreateProject.clicked.connect(self.Popup_CreateProject_show)
        self.btnRefresh.clicked.connect(self.refresh)
        #set up exit action
        self.actionExit.triggered.connect(self.QuitButton)
        #set up icons for "create project" button and "refresh" button
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(Config.RootFolder + Icon_Folder + "create.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCreateProject.setIcon(icon)
        self.btnCreateProject.setToolTip(Tip_CreateProject)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(Config.RootFolder + Icon_Folder + "refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRefresh.setIcon(icon1)
        self.btnRefresh.setToolTip(Tip_Refresh)

    def Popup_CreateProject_show(self):
        self.Popup_CreateProject = PopupWindow_actionCreateProject(self)
        self.Popup_CreateProject.show()

    def refresh(self):
        self.RefreshTree.refresh()

    def QuitButton(self):
        reply = QtGui.QMessageBox.question(self, "Message", \
                "Are you sure you want to quit?", \
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, \
                QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            QtCore.QCoreApplication.quit()