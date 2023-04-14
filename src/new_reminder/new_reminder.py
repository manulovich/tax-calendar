from PySide6.QtCore import Slot, Signal, QDate
from PySide6.QtWidgets import QWidget
from .design import Ui_new_reminder


class NewReminder(QWidget):
    create = Signal(str, str) # title, date
    reset = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_new_reminder()

        self.ui.setupUi(self)
        self._clear_data()
        self.ui.new_reminder_date.setCalendarPopup(True)

        self.ui.btn_new_reminder_add.clicked.connect(self.on_create)
        self.ui.btn_new_reminder_reset.clicked.connect(self.on_reset)

    @Slot()
    def on_create(self):
        self.create.emit(
            self.ui.new_reminder_title.displayText(),
            self.ui.new_reminder_date.date().toString()
        )
        self._clear_data()

    @Slot()
    def on_reset(self):
        self._clear_data()
        self.reset.emit()

    def _clear_data(self):
        self.ui.new_reminder_title.clear(),
        self.ui.new_reminder_date.setDate(QDate.currentDate())
