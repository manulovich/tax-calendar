from PySide6.QtCore import Slot, Signal, QDate
from PySide6.QtWidgets import QWidget
from .design import Ui_reminder


class Reminder(QWidget):
    reset = Signal() 
    change = Signal(str, str, str) # rid, title, date
    delete = Signal(str) # rid
    events = Signal()

    def __init__(self, title: str, date: str, rid: str) -> None:
        super().__init__()
        self.ui = Ui_reminder()
        self.title = title
        self.date = date
        self.rid = rid
        
        self.ui.setupUi(self)
        self.ui.reminder_title.setText(title)
        self.ui.reminder_date.setDate(QDate.fromString(date))
        self.ui.reminder_date.setCalendarPopup(True)

        self.ui.btn_reset.clicked.connect(self.on_reset)
        self.ui.btn_change.clicked.connect(self.on_change)
        self.ui.btn_del.clicked.connect(self.on_delete)

    @Slot()
    def on_reset(self):
        self.ui.reminder_title.setText(self.title)
        self.ui.reminder_date.setDate(QDate.fromString(self.date))
        self.reset.emit()

    @Slot()
    def on_change(self):
        new_title = self.ui.reminder_title.displayText()
        new_date = self.ui.reminder_date.date()

        self.ui.reminder_title.setText(new_title)
        self.ui.reminder_date.setDate(new_date)
        self.change.emit(self.rid, new_title, new_date.toString())
        self.events.emit()

    @Slot()
    def on_delete(self):
        self.delete.emit(self.rid)
        self.events.emit()
