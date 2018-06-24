import sys
import os.path
from PyQt4 import QtGui,QtCore,uic

import Config
from Config import *
from MainWindow import MainWindow



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



class ConfigWindow(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(ConfigWindow, self).__init__(*args, **kwargs)
        self.setupUI(self)

    def setupUI(self, Form):
        Form.setObjectName(_fromUtf8("Config"))
        Form.resize(414, 170)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
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
        self.groupBox = QtGui.QGroupBox(Form)
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
        icon.addPixmap(QtGui.QPixmap(os.path.abspath( sys.path[0] + "/" + "Data" + "/" + "Icon/" + "folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RootFolderPath_broswer.setIcon(icon)
        self.RootFolderPath_broswer.setObjectName(_fromUtf8("RootFolderPath_broswer"))


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Config):
        Config.setWindowTitle(_translate("Config", "Config", None))
        self.btnOK.setText(_translate("Config", "OK", None))
        self.btnCancel.setText(_translate("Config", "Cancel", None))
        self.groupBox.setTitle(_translate("Config", "Folder Path", None))
        self.label.setText(_translate("Config", "Root Folder", None))

        self.RootFolderPath.setText(os.path.abspath( sys.path[0] + "/" + "Data") )
        self.RootFolderPath_broswer.clicked.connect(self.fRootFolderPath_broswer)
        self.btnOK.clicked.connect(self.fOK)
        self.btnCancel.clicked.connect(self.fQuit)

    def fRootFolderPath_broswer(self):
        Directory = QtGui.QFileDialog.getExistingDirectory()
        if Directory != "":
            self.RootFolderPath.setText(Directory)

    def fOK(self):
        print self.RootFolderPath.text()
        Config.RootFolder = os.path.abspath(self.RootFolderPath.text()) + "/"
        self.parent = MainWindow()
        self.parent.show()
        self.close()

    def fQuit(self):
        QtCore.QCoreApplication.quit()