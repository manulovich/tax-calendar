import os
from os import path

USER = os.path.expanduser('~').split('\\')[-1]
NAME_BAT_FILE = 'taxcalendar.bat'
PATH_TO_STARTUP = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER

# C:\Users\vladk\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
# C:\Users\vladk\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup


def is_in_autorun() -> bool:
    return path.isfile(path.join(PATH_TO_STARTUP, NAME_BAT_FILE))


def add_to_startup(path_to_script: str) -> None:
    with open(path.join(PATH_TO_STARTUP, NAME_BAT_FILE), 'w+') as file:
        file.write(f'@echo off \n start "Налоговый календарь" "{path_to_script}"')


def del_from_startup() -> None:
    os.remove(path.join(PATH_TO_STARTUP, NAME_BAT_FILE))
