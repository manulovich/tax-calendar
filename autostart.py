import sys
from os import path
from src.stores import SettingsStore, ReminderStore
from src.utils import send_reminder_notifications
import time

IS_DEV = True

base_path = path.join('src') if IS_DEV else path.dirname(sys.executable)


settings = SettingsStore(path.join(base_path, 'settings.json'))
reminders = ReminderStore(
    settings.get_by_key(
        'path_to_reminders', base_path
    )
)

time.sleep(5)

send_reminder_notifications(reminders, settings, path.join(base_path, 'icon.png'))
