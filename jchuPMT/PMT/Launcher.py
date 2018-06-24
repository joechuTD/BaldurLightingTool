import sys,os

def AddSysPath(new_path):  
      if not os.path.exists(new_path): 
          return -1  
      new_path = os.path.abspath(new_path)
      if sys.platform == 'win32' or sys.platform == 'win64':
            new_pathnew_path = new_path.lower( )
      for x in sys.path:  
            x = os.path.abspath(x)
            if sys.platform == 'win32' or sys.platform == 'win64':
                   xx = x.lower( )
            if new_path in (x, x + os.sep):  
                   return 0  
      sys.path.append(new_path)  
      return 1

AddSysPath(   os.path.abspath( sys.path[0] + "/" + "Config" )   )
AddSysPath(   os.path.abspath( sys.path[0] + "/" + "LightingManagerScripts" )   )
AddSysPath(   os.path.abspath( sys.path[0] + "/" + "UIscripts" )   )

from ConfigWindow import *

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    configWindow = ConfigWindow()
    configWindow.show()
    sys.exit(app.exec_())