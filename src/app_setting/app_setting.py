from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtCore import Slot, Signal, Qt
from .design import Ui_app_setting

class AppSetting(QDialog):
    selected_path_to_directory = Signal(str)
    selected_delay = Signal(int)
    check_autostart = Signal(bool)

    def __init__(self, parent=None, path_to_directory='', delay_value=0, is_in_startup=False) -> None:
        super().__init__(parent)
        self.ui = Ui_app_setting()
        self.path_to_directory = path_to_directory
        self.delay_value = delay_value
        self.is_in_startup = is_in_startup
        
        self.ui.setupUi(self)
        self.ui.label_selected_directory.setText(path_to_directory)
        self.ui.select_delay.setValue(delay_value)
        self.ui.check_autostart.setChecked(is_in_startup)


        self.ui.btn_select_directory.clicked.connect(self._onSelectDirectory)
        self.ui.select_delay.valueChanged.connect(self._onSelectDelay)
        self.ui.check_autostart.stateChanged.connect(self._onCheckAutostart)

    @Slot()
    def _onSelectDirectory(self):
        self.path_to_directory = QFileDialog.getExistingDirectory()
        self.ui.label_selected_directory.setText(self.path_to_directory)
        self.selected_path_to_directory.emit(self.path_to_directory)

    @Slot()
    def _onSelectDelay(self):
        self.selected_delay.emit(self.ui.select_delay.value())

    @Slot()
    def _onCheckAutostart(self):
        state = True if Qt.CheckState.Checked == self.ui.check_autostart.checkState() else False
        self.check_autostart.emit(state)


