from PySide6.QtWidgets import QBoxLayout


# Source: https://josbalcaen.com/maya-python-pyqt-delete-all-widgets-in-a-layout/
def clear_layout(layout: QBoxLayout) -> None:
    for i in range(layout.count()):
        children = layout.itemAt(i)

        if children.widget() is not None:
            children.widget().deleteLater()
        elif children.layout() is not None:
            clear_layout(children.layout())
