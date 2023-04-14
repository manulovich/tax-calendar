import sys
from os import path
from PySide6.QtWidgets import QApplication
from src.main_window import MainWindow

IS_DEV = True

if __name__ == '__main__':
    base_path = path.join('src') if IS_DEV else path.dirname(sys.executable)

    app = QApplication(sys.argv)
    main_window = MainWindow(base_path, is_dev=IS_DEV)

    main_window.show()
    sys.exit(app.exec())
