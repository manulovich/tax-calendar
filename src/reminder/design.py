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

class Ui_reminder(object):
    def setupUi(self, reminder):
        if not reminder.objectName():
            reminder.setObjectName(u"reminder")
        reminder.resize(548, 47)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(reminder.sizePolicy().hasHeightForWidth())
        reminder.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(reminder)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.reminder_title = QLineEdit(reminder)
        self.reminder_title.setObjectName(u"reminder_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.reminder_title.sizePolicy().hasHeightForWidth())
        self.reminder_title.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.reminder_title)

        self.reminder_date = QDateEdit(reminder)
        self.reminder_date.setObjectName(u"reminder_date")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.reminder_date.sizePolicy().hasHeightForWidth())
        self.reminder_date.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.reminder_date)

        self.btn_reset = QPushButton(reminder)
        self.btn_reset.setObjectName(u"btn_reset")
        sizePolicy2.setHeightForWidth(self.btn_reset.sizePolicy().hasHeightForWidth())
        self.btn_reset.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.btn_reset)

        self.btn_change = QPushButton(reminder)
        self.btn_change.setObjectName(u"btn_change")
        sizePolicy2.setHeightForWidth(self.btn_change.sizePolicy().hasHeightForWidth())
        self.btn_change.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.btn_change)

        self.btn_del = QPushButton(reminder)
        self.btn_del.setObjectName(u"btn_del")
        sizePolicy2.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.btn_del)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(reminder)

        QMetaObject.connectSlotsByName(reminder)
    # setupUi

    def retranslateUi(self, reminder):
        reminder.setWindowTitle(QCoreApplication.translate("reminder", u"Form", None))
        self.btn_reset.setText(QCoreApplication.translate("reminder", u"\u0421\u0431\u0440\u043e\u0441", None))
        self.btn_change.setText(QCoreApplication.translate("reminder", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.btn_del.setText(QCoreApplication.translate("reminder", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

