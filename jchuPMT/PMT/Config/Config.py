IsConfiged = False

RootFolder = "C:/Users/jchu/Desktop/TechArtSemester3/ProjectManagmentTools/PMT/PMT/Data/"

UI_Folder = "UI/"
Icon_Folder = "Icon/"
Projects_Folder = "Projects/"

config_Folder = "config/"
temp_Folder = "temp/"
picture_Folder = "picture/"

config_FileName = "config.txt"

MainWindowFile = "MainWindow.ui"
Popup_Create_FileName = "Create.ui"
Popup_Delete_FileName = "Confirm.ui"
Popup_Rename_FileName = "Rename.ui"
Popup_Search_FileName = "Search.ui"
Popup_Move_FileName = "MoveAndCopy.ui"
Popup_Info_FileName = "info.ui"

class DCCPathFunction:
    def __init__(self):
        self.maya2018Path = r"C:\Program Files\Autodesk\Maya2018\bin\maya.exe"
        self.UE4_18Path = r"C:\Program Files\Epic Games\UE_4.18\Engine\Binaries\Win64\UE4Editor.exe"
        self.Unity2017Path = r"C:\Program Files\Unity2017\Editor\Unity.exe"

        self.DCCPathList = [self.maya2018Path, self.UE4_18Path, self.Unity2017Path]

        self.DCCDict = {self.maya2018Path : 'maya2018'  , \
                        self.UE4_18Path   : 'UE4.18'    , \
                        self.Unity2017Path: 'Unity2017' }

MainWindowTitle = "Baldur - Lighting Manager v0.1"
GalleryWindowTitle = "Gallery"
ImageViewerWindowTitle = "Loki Image Viewer"

Warning_Delete = "WARNING: You are going to delete "

Tip_CreateProject = "Create Project Folder"
Tip_CreateScene = "Create Scene - create a scene folder"
Tip_CreateLighting = "Create Lighting - create a lighting folder that contains different version of lighting in a scene"
Tip_RenameProject = "Rename Project Folder"
Tip_RenameScene = "Rename Scene Folder"
Tip_RenameLighting = "Rename Lighting Folder"
Tip_DeleteProject = "Delete Project Folder"
Tip_DeleteScene = "Delete Scene Folder"
Tip_DeleteLighting = "Delete Lighting Folder"
Tip_MoveScene = "Move Scene Folder"
Tip_MoveLighting = "Move Lighting Folder"
Tip_Launch = "Launch the specific DCC that is bounded to this project, the DCC that is launched could be changed in setting"
Tip_Info = "Show the tips of lighting and give you check box to make sure you won't forget"
Tip_Refresh = "Refresh the treewidget down below"
Tip_Gallery = "Launch the image gallery of this lighting scene, pictures is loaded through the other two buttons"
Tip_AddByFolder = "Unfinished button: Add pictures(.jpg, .png) into this Lighting folder by a folder base"
Tip_AddByFile = "Unfinished button: Add pictures(.jpg, .png) into this Lighting folder by a file base"