import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win64':
    base = 'Win64GUI'

#buildOptions = dict(include_files = ['Config/','UIscripts/', 'LightingManagerScripts/', 'Data/'])
options = {
    'build_exe': {
        'includes': 'atexit'
    }
}

executables = [
    Executable('Launcher.py', base=base)
]

setup(name='Baldur',
      version='0.1',
      description='Baldur - Lighting Manager v0.1',
      options=options,
      executables=executables
      )
