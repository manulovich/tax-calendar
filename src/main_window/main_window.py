from os import path
from PySide6.QtWidgets import QMainWindow

from .design import Ui_MainWindow
from src.stores import ReminderStore, QuotesStore, SettingsStore
from src.reminder import Reminder
from src.new_reminder import NewReminder
from src.app_setting import AppSetting
from src.utils import send_reminder_notifications, clear_layout, add_to_startup, del_from_startup


class MainWindow(QMainWindow):
    def __init__(self, base_path: str, is_dev) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.base_path = base_path
        self.is_dev = is_dev

        self._preload()
        self._set_quote()

    def _preload(self) -> None:
        self.settings = SettingsStore(
            path.join(self.base_path, 'settings.json'))
        self.quotes = QuotesStore(path.join(self.base_path, 'quotes.json'))
        self.new_reminder = NewReminder()

        path_to_reminders = self.settings.get_by_key(
            'path_to_reminders', self.base_path
        )

        if not path.isdir(path_to_reminders):
            self.settings.set_by_key(
                'path_to_reminders', self.base_path
            )
            path_to_reminders = self.base_path

        self.reminders = ReminderStore(
            path_to_reminders,
            self._render_all_reminder
        )
        self.new_reminder.create.connect(self.reminders.set_item)

        self.ui.new_reminder_container.addWidget(self.new_reminder)
        self.ui.app.triggered.connect(self._open_setting_app)

        self._render_all_reminder()
        send_reminder_notifications(
            self.reminders,
            self.settings,
            path.join(
                self.base_path, 'icon.png'
            )
        )

    def _open_setting_app(self):
        dialog = AppSetting(
            self,
            path_to_directory=self.settings.get_by_key(
                'path_to_reminders',
                path.abspath(path.curdir)
            ),
            delay_value=self.settings.get_by_key(
                'delay_value',
                0
            ),
            is_in_startup=self.settings.get_by_key(
                'is_in_startup',
                False
            ),
        )

        def on_selected_path(new_path_to_file: str):
            self.reminders.change_directory(new_path_to_file)
            self.settings.set_by_key('path_to_reminders', new_path_to_file)

        def on_selected_delay(delay_value: int):
            self.settings.set_by_key('delay_value', delay_value)

        def on_check_autostart(is_in_startup: bool):
            self.settings.set_by_key('is_in_startup', is_in_startup)

            if is_in_startup:
                file_extension = 'py' if self.is_dev else 'exe';
                add_to_startup(path.join(self.base_path, f'autostart.{file_extension}'))
            else:
                del_from_startup()

        dialog.selected_path_to_directory.connect(on_selected_path)
        dialog.selected_delay.connect(on_selected_delay)
        dialog.check_autostart.connect(on_check_autostart)

        dialog.exec()

    def _set_quote(self) -> None:
        quote = self.quotes.get_random_quote()
        self.ui.quote.setText(quote)

    def _render_all_reminder(self) -> None:
        clear_layout(self.ui.reminder_list_container)

        for reminder in self.reminders.get_all():
            title = reminder['title']
            date = reminder['date']
            rid = reminder['id']

            reminder_widget = Reminder(title, date, rid)
            reminder_widget.change.connect(self.reminders.eddit_item)
            reminder_widget.delete.connect(self.reminders.del_item)
            reminder_widget.events.connect(self._render_all_reminder)

            self.ui.reminder_list_container.addWidget(reminder_widget)
