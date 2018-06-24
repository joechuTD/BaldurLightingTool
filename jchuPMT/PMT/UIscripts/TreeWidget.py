import sys
import os.path
from PyQt4 import Qt,QtGui,QtCore,uic

import Config
from Config import *
from btnCore import *
from btnCreate import *
from btnDelete import *
from btnMoveAndCopy import *
from btnRename import *


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



class RefreshTree:
    def __init__(self, treeWidget, Parent):
        self.treeWidget = treeWidget
        self.parent = Parent

    def refresh(self):
        self.clearQTreeWidget(self.treeWidget)
        self.load_project_structure(Config.RootFolder + Projects_Folder, self.treeWidget)

    def clearQTreeWidget(self, tree):
        i = tree.topLevelItemCount()
        while i > -1:
            tree.takeTopLevelItem(i)
            i -= 1

    def load_project_structure(self, startpath, tree, layer = "Project"):
        """
        Load Project structure tree
        :param startpath: 
        :param tree: 
        :return: 
        """
        for element in os.listdir(startpath):
            path_info = startpath + "/" + element
            parent_itm = Qt.QTreeWidgetItem(tree, [os.path.basename(element)])
            parent_itm.setToolTip(0, os.path.abspath(Config.RootFolder + Projects_Folder + "/" + element))
            
            if element != "config" and element != "temp":
                row = TreeItem(layer, element)
                self.treeWidget.setItemWidget( parent_itm, 1, row )
                ### Signals
                setattr(self, "projectButtons_" + element, ProjectButtonFunctions(element, self.parent))
                self.treeWidget.connect( row.Launch, QtCore.SIGNAL("clicked()"), getattr(self, "projectButtons_" + element).Popup_Launch_show )
                self.treeWidget.connect( row.create, QtCore.SIGNAL("clicked()"), getattr(self, "projectButtons_" + element).Popup_CreateScene_show )
                self.treeWidget.connect( row.rename, QtCore.SIGNAL("clicked()"), getattr(self, "projectButtons_" + element).Popup_RenameProject_show )
                self.treeWidget.connect( row.delete, QtCore.SIGNAL("clicked()"), getattr(self, "projectButtons_" + element).Popup_DeleteProject_show )

            if os.path.isdir(path_info):
                self.load_scene_structure(path_info, parent_itm, Project = element)
                parent_itm.setIcon(0, QtGui.QIcon(Config.RootFolder + Icon_Folder + "ok.png"))
            else:
                parent_itm.setIcon(0, QtGui.QIcon(Config.RootFolder + Icon_Folder + "file.png"))
            self.treeWidget.expandAll()
            self.treeWidget.resizeColumnToContents(0)
            self.treeWidget.resizeColumnToContents(1)

    def load_scene_structure(self, startpath, tree, layer = "Scene", Project = ""):
        """
        Load Project structure tree
        :param startpath: 
        :param tree: 
        :return: 
        """
        for element in os.listdir(startpath):         
            if element != "config" and element != "temp":
                path_info = startpath + "/" + element
                parent_itm = Qt.QTreeWidgetItem(tree, [os.path.basename(element)])
                parent_itm.setToolTip(0, os.path.abspath(Config.RootFolder + Projects_Folder + "/" + Project + "/" + element))
                row = TreeItem(layer, element)
                self.treeWidget.setItemWidget( parent_itm, 1, row )
                ### Signals
                setattr(self, "sceneButtons_" + Project + "/" + element, SceneButtonFunctions(element, self.parent, Project))
                self.treeWidget.connect( row.create, QtCore.SIGNAL("clicked()"), getattr(self, "sceneButtons_" + Project + "/" + element).Popup_CreateLighting_show )
                self.treeWidget.connect( row.rename, QtCore.SIGNAL("clicked()"), getattr(self, "sceneButtons_" + Project + "/" + element).Popup_RenameScene_show )
                self.treeWidget.connect( row.move, QtCore.SIGNAL("clicked()"), getattr(self, "sceneButtons_" + Project + "/" + element).Popup_MoveScene_show )
                self.treeWidget.connect( row.delete, QtCore.SIGNAL("clicked()"), getattr(self, "sceneButtons_" + Project + "/" + element).Popup_DeleteScene_show )

                if os.path.isdir(path_info):
                    self.load_lighting_structure(path_info, parent_itm, "Lighting", Project, element)
                    parent_itm.setIcon(0, QtGui.QIcon(Config.RootFolder + Icon_Folder + "ok.png"))
                else:
                    parent_itm.setIcon(0, QtGui.QIcon(Config.RootFolder + Icon_Folder + "file.png"))

            self.treeWidget.expandAll()
            self.treeWidget.resizeColumnToContents(0)
            self.treeWidget.resizeColumnToContents(1)

    def load_lighting_structure(self, startpath, tree, layer = "Lighting", Project = "", Scene = ""):
        """
        Load Project structure tree
        :param startpath: 
        :param tree: 
        :return: 
        """
        for element in os.listdir(startpath):          
            if element != "config" and element != "temp":
                path_info = startpath + "/" + element
                parent_itm = Qt.QTreeWidgetItem(tree, [os.path.basename(element)])
                parent_itm.setToolTip(0, os.path.abspath(Config.RootFolder + Projects_Folder + "/" + Project + "/" + Scene + "/" + element))
                row = TreeItem(layer, element)
                self.treeWidget.setItemWidget( parent_itm, 1, row )
                ### Signals
                setattr(self, "LightingButtons_" + Project + "/" + Scene + "/" + element, LightingButtonFunctions(element, self.parent, Project, Scene))
                self.treeWidget.connect( row.info, QtCore.SIGNAL("clicked()"), getattr(self, "LightingButtons_" + Project + "/" + Scene + "/" + element).Popup_info_show )
                self.treeWidget.connect( row.rename, QtCore.SIGNAL("clicked()"), getattr(self, "LightingButtons_" + Project + "/" + Scene + "/" + element).Popup_RenameLighting_show )
                self.treeWidget.connect( row.move, QtCore.SIGNAL("clicked()"), getattr(self, "LightingButtons_" + Project + "/" + Scene + "/" + element).Popup_MoveLighting_show )
                self.treeWidget.connect( row.delete, QtCore.SIGNAL("clicked()"), getattr(self, "LightingButtons_" + Project + "/" + Scene + "/" + element).Popup_DeleteLighting_show )

                if os.path.isdir(path_info):
                    self.load_picture_structure(path_info, parent_itm, "Picture", Project, Scene, element)
                    parent_itm.setIcon(0, QtGui.QIcon(Config.RootFolder + Icon_Folder + "ok.png"))
                else:
                    parent_itm.setIcon(0, QtGui.QIcon(Config.RootFolder + Icon_Folder + "file.png")) 

            self.treeWidget.expandAll()
            self.treeWidget.resizeColumnToContents(0)
            self.treeWidget.resizeColumnToContents(1)

    def load_picture_structure(self, startpath, tree, layer = "Picture", Project = "", Scene = "", Lighting = ""):
        """
        Load Project structure tree
        :param startpath: 
        :param tree: 
        :return: 
        """
        for element in os.listdir(startpath):          
            if element != "config" and element != "temp":
                path_info = startpath + "/" + element
                parent_itm = Qt.QTreeWidgetItem(tree, [os.path.basename(element)])
                parent_itm.setToolTip(0, os.path.abspath(Config.RootFolder + Projects_Folder + "/" + Project + "/" + Scene + "/" + Lighting + "/" + element))
                row = TreeItem(layer, element)
                self.treeWidget.setItemWidget( parent_itm, 1, row )
                ### Signals
                setattr(self, "PictureButtons_" + Project + "/" + Scene + "/" + Lighting + "/" + element, PictureButtonFunctions(Lighting, self.parent, Project, Scene))
                self.treeWidget.connect( row.Lighting, QtCore.SIGNAL("clicked()"), getattr(self, "PictureButtons_" + Project + "/" + Scene + "/" + Lighting + "/" + element).Popup_Lighting_show )
                self.treeWidget.connect( row.AddByFolder, QtCore.SIGNAL("clicked()"), getattr(self, "PictureButtons_" + Project + "/" + Scene + "/" + Lighting + "/" + element).Popup_AddByFolder_show )
                self.treeWidget.connect( row.AddByFile, QtCore.SIGNAL("clicked()"), getattr(self, "PictureButtons_" + Project + "/" + Scene + "/" + Lighting + "/" + element).Popup_AddByFile_show )

                if os.path.isdir(path_info):
                    self.load_pictures(path_info, parent_itm, "Picture", Project, Scene, element)
                    parent_itm.setIcon(0, QtGui.QIcon(Config.RootFolder + Icon_Folder + "ok.png"))
                else:
                    parent_itm.setIcon(0, QtGui.QIcon(Config.RootFolder + Icon_Folder + "file.png")) 

            self.treeWidget.expandAll()
            self.treeWidget.resizeColumnToContents(0)
            self.treeWidget.resizeColumnToContents(1)

    def load_pictures(self, startpath, tree, layer = "Picture", Project = "", Scene = "", Lighting = ""):
        """
        Load Project structure tree
        :param startpath: 
        :param tree: 
        :return: 
        """
        for element in os.listdir(startpath):          
            if element != "config" and element != "temp":
                element = element.lower()
                if ".jpg" in element or ".png" in element:
                    element = element[:30]
                    path_info = startpath + "/" + element
                    parent_itm = Qt.QTreeWidgetItem(tree, [os.path.basename(element)])

                    if os.path.isdir(path_info):
                        parent_itm.setIcon(0, QtGui.QIcon(Config.RootFolder + Icon_Folder + "ok.png"))
                    else:
                        parent_itm.setIcon(0, QtGui.QIcon(Config.RootFolder + Icon_Folder + "file.jpg")) 

            self.treeWidget.expandAll()
            self.treeWidget.resizeColumnToContents(0)
            self.treeWidget.resizeColumnToContents(1)



class TreeItem(QtGui.QWidget):
    def __init__(self, layer, name):
        super(TreeItem, self).__init__()

        self.row = QtGui.QHBoxLayout()

        if layer == "Project":
            self.AddButton("Launch", self.row, icon_name = "", layer_name = name, isLaunch = True, ToolTip = Tip_Launch)
            self.AddButton("create", self.row, ToolTip = Tip_CreateScene)
            self.AddButton("rename", self.row, ToolTip = Tip_RenameProject)
            self.AddButton("delete", self.row, ToolTip = Tip_DeleteProject)

        elif layer == "Scene":
            self.AddButton("create", self.row, ToolTip = Tip_CreateLighting)
            self.AddButton("rename", self.row, ToolTip = Tip_RenameScene)
            self.AddButton("move", self.row, ToolTip = Tip_MoveScene)
            self.AddButton("delete", self.row, ToolTip = Tip_DeleteScene)

        elif layer == "Lighting":
            self.AddButton("info", self.row, ToolTip = Tip_Info)
            self.AddButton("rename", self.row, ToolTip = Tip_RenameLighting)
            self.AddButton("move", self.row, ToolTip = Tip_MoveLighting)
            self.AddButton("delete", self.row, ToolTip = Tip_DeleteLighting)

        elif layer == "Picture":
            self.AddButton("Lighting", self.row, "L", Text = "Gallery", ToolTip = Tip_Gallery)
            #self.Lighting.setStyleSheet("background-color: rgb(87,183,133)")
            self.AddButton("AddByFolder", self.row, Text = "AddByFolder", ToolTip = Tip_AddByFolder)
            self.AddButton("AddByFile", self.row, Text = "AddByFile", ToolTip = Tip_AddByFile)
            self.AddByFolder.setEnabled(False)
            self.AddByFile.setEnabled(False)

        self.setLayout(self.row)

    def AddButton(self, name, row, icon_name = "", layer_name = "", isLaunch = False, Text = "", ToolTip = ""):
        setattr(self, name,  QtGui.QPushButton())
        if icon_name == "":
            icon_name = name
        getattr(self, name).setText(Text)
        if isLaunch:
            DCCName = self.ReadDCCName(layer_name)
            getattr(self, name).setText(DCCName)
            icon_name = str(DCCName)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap((Config.RootFolder + Icon_Folder + icon_name + ".png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        getattr(self, name).setIcon(icon)
        getattr(self, name).setObjectName(_fromUtf8(name))
        getattr(self, name).setToolTip(ToolTip)
        row.addWidget(getattr(self, name))

        getattr(self, name).setStyleSheet("color: rgb(220, 220, 220)")
        getattr(self, name).setStyleSheet("background-color: rgb(120, 120, 120)")

    def ReadDCCName(self, layer_name):
        f = open(os.path.abspath(Config.RootFolder + Projects_Folder + layer_name + "/" + config_Folder + "/" + config_FileName))
        Path = f.read()
        f.close()
        oDCCPathFunction = DCCPathFunction()
        DCCName = oDCCPathFunction.DCCDict[Path].replace(".", "_")
        return DCCName



class ProjectButtonFunctions:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def Popup_Launch_show(self):
        f = open(os.path.abspath(Config.RootFolder + Projects_Folder + self.name + "/" + config_Folder + "/" + "config.txt"))
        Path = f.read()
        f.close()
        self.launchSoftware(Path)

    def Popup_CreateScene_show(self):
        self.Popup_CreateScene = PopupWindow_actionCreateScene(self.parent, self.name)
        self.Popup_CreateScene.show()

    def Popup_DeleteProject_show(self):
        self.Popup_DeleteProject = PopupWindow_DeleteProject(self.parent, self.name)
        self.Popup_DeleteProject.show()

    def Popup_RenameProject_show(self):
        self.Popup_RenameProject = PopupWindow_RenameProject(self.parent, self.name)
        self.Popup_RenameProject.show()

    def launchSoftware(self, Path):
        os.startfile(Path)

class SceneButtonFunctions:
    def __init__(self, name, parent, Project):
        self.name = name
        self.parent = parent
        self.project = Project

    def Popup_CreateLighting_show(self):
        self.Popup_CreateLighting = PopupWindow_actionCreateLighting(self.parent, self.name, self.project)
        self.Popup_CreateLighting.show()

    def Popup_DeleteScene_show(self):
        self.Popup_DeleteScene = PopupWindow_DeleteScene(self.parent, self.name, self.project)
        self.Popup_DeleteScene.show()

    def Popup_MoveScene_show(self):
        self.Popup_DeleteScene = PopupWindow_MoveScene(self.parent, self.name, self.project)
        self.Popup_DeleteScene.show()

    def Popup_RenameScene_show(self):
        self.Popup_RenameScene = PopupWindow_RenameScene(self.parent, self.name, self.project)
        self.Popup_RenameScene.show()

class LightingButtonFunctions:
    def __init__(self, name, parent, Project, Scene):
        self.name = name
        self.parent = parent
        self.project = Project
        self.scene = Scene

    def Popup_info_show(self):
        self.Popup_Lighting = PopupWindow_Info(self.parent, self.name, self.project, self.scene)
        self.Popup_Lighting.show()

    def Popup_DeleteLighting_show(self):
        self.Popup_DeleteLighting = PopupWindow_DeleteLighting(self.parent, self.name, self.project, self.scene)
        self.Popup_DeleteLighting.show()

    def Popup_MoveLighting_show(self):
        self.Popup_DeleteLighting = PopupWindow_MoveLighting(self.parent, self.name, self.project, self.scene)
        self.Popup_DeleteLighting.show()

    def Popup_RenameLighting_show(self):
        self.Popup_RenameLighting = PopupWindow_RenameLighting(self.parent, self.name, self.project, self.scene)
        self.Popup_RenameLighting.show()

class PictureButtonFunctions:
    def __init__(self, name, parent, Project, Scene):
        self.name = name
        self.parent = parent
        self.project = Project
        self.scene = Scene

    def Popup_Lighting_show(self):
        self.Popup_Lighting = PopupWindow_Lighting(self.parent, "", GalleryWindowTitle, self.name, self.project, self.scene)
        self.Popup_Lighting.show()

    def Popup_AddByFolder_show(self):
        self.Popup_DeleteLighting = PopupWindow_AddByFolder(self.parent, self.name, self.project, self.scene)
        self.Popup_DeleteLighting.show()

    def Popup_AddByFile_show(self):
        self.Popup_DeleteLighting = PopupWindow_AddByFile(self.parent, self.name, self.project, self.scene)
        self.Popup_DeleteLighting.show()
