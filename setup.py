import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.

excludes = []
packages = []

zip_include_packages = []

build_options = {
    'excludes': excludes,
    'packages': packages,
    'include_files': ['src/assets/icon.png', 'src/quotes.json'],
    'zip_include_packages': zip_include_packages,
}

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable(
        './main.py',
        base=base,
        target_name='Налоговый каледарь',
        icon='./src/assets/icon.ico',
        shortcutName='Налоговый каледарь',
        shortcutDir='ProgramMenuFolder'
    ),
    Executable('./autostart.py', base=base, target_name='autostart')
]

setup(name='Налоговый календарь',
      version='0.5.0',
      description='Обычная напоминалка',
      options={'build_exe': build_options},
      executables=executables)
