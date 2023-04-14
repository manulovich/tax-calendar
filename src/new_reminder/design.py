# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_new_reminder(object):
    def setupUi(self, new_reminder):
        if not new_reminder.objectName():
            new_reminder.setObjectName(u"new_reminder")
        new_reminder.resize(470, 43)
        self.verticalLayout = QVBoxLayout(new_reminder)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.new_reminder_title = QLineEdit(new_reminder)
        self.new_reminder_title.setObjectName(u"new_reminder_title")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_reminder_title.sizePolicy().hasHeightForWidth())
        self.new_reminder_title.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.new_reminder_title)

        self.new_reminder_date = QDateEdit(new_reminder)
        self.new_reminder_date.setObjectName(u"new_reminder_date")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.new_reminder_date.sizePolicy().hasHeightForWidth())
        self.new_reminder_date.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.new_reminder_date)

        self.btn_new_reminder_reset = QPushButton(new_reminder)
        self.btn_new_reminder_reset.setObjectName(u"btn_new_reminder_reset")
        sizePolicy1.setHeightForWidth(self.btn_new_reminder_reset.sizePolicy().hasHeightForWidth())
        self.btn_new_reminder_reset.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.btn_new_reminder_reset)

        self.btn_new_reminder_add = QPushButton(new_reminder)
        self.btn_new_reminder_add.setObjectName(u"btn_new_reminder_add")
        sizePolicy1.setHeightForWidth(self.btn_new_reminder_add.sizePolicy().hasHeightForWidth())
        self.btn_new_reminder_add.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.btn_new_reminder_add)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(new_reminder)

        QMetaObject.connectSlotsByName(new_reminder)
    # setupUi

    def retranslateUi(self, new_reminder):
        new_reminder.setWindowTitle(QCoreApplication.translate("new_reminder", u"Form", None))
        self.btn_new_reminder_reset.setText(QCoreApplication.translate("new_reminder", u"\u0421\u0431\u0440\u043e\u0441", None))
        self.btn_new_reminder_add.setText(QCoreApplication.translate("new_reminder", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

