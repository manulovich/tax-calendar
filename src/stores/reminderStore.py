import uuid
from os import path
from .store import Store


"""
[
    {
        date: str,
        id: str,
        title: str
    }
]
"""


class ReminderStore(Store):
    FILE_NAME = 'store.json'
    _reminders = list()

    def __init__(self, direct_path: str, on_change_callback=lambda: ()):
        super().__init__(path.join(direct_path, self.FILE_NAME))
        self.on_change_callback = on_change_callback

        self._reminders = self._read_or_create(list)

    def change_directory(self, new_direct_path) -> None:
        self._change_path_to_file(path.join(new_direct_path, self.FILE_NAME))
        self._reminders = self._read_or_create(list)

        self.on_change_callback()
        self._save(self._reminders)

    def get_all(self):
        return self._reminders.copy()

    def set_item(self, title: str, date: str) -> str:
        rid = str(uuid.uuid4())

        self._reminders.append({
            'id': rid,
            'title': title,
            'date': date
        })

        self.on_change_callback()
        self._save(self._reminders)

        return rid

    def eddit_item(self, rid: str, new_title: str | None, new_date: str | None) -> None:
        for i in range(len(self._reminders)):
            reminder = self._reminders[i]

            if reminder['id'] == rid:
                self._reminders[i] = {
                    'id': rid,
                    'title': new_title or reminder['title'],
                    'date': new_date or reminder['date'],
                }

                self.on_change_callback()
                self._save(self._reminders)
                return

    def del_item(self, rid: str) -> None:
        for i in range(len(self._reminders)):
            if self._reminders[i]['id'] == rid:
                self._reminders.pop(i)

                self.on_change_callback()
                self._save(self._reminders)
                return
