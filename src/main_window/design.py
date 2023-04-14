# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QScrollArea, QSizePolicy,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)
from src.assets import resources as resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(843, 383)
        icon = QIcon()
        icon.addFile(u":/icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.app = QAction(MainWindow)
        self.app.setObjectName(u"app")
        self.preference = QAction(MainWindow)
        self.preference.setObjectName(u"preference")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.content = QTabWidget(self.centralwidget)
        self.content.setObjectName(u"content")
        self.new_reminder = QWidget()
        self.new_reminder.setObjectName(u"new_reminder")
        self.verticalLayout_2 = QVBoxLayout(self.new_reminder)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.new_reminder_container = QVBoxLayout()
        self.new_reminder_container.setObjectName(u"new_reminder_container")

        self.verticalLayout_2.addLayout(self.new_reminder_container)

        self.quote = QLabel(self.new_reminder)
        self.quote.setObjectName(u"quote")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quote.sizePolicy().hasHeightForWidth())
        self.quote.setSizePolicy(sizePolicy)
        self.quote.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.quote)

        self.content.addTab(self.new_reminder, "")
        self.reminder_list = QWidget()
        self.reminder_list.setObjectName(u"reminder_list")
        self.verticalLayout_3 = QVBoxLayout(self.reminder_list)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.reminder_list_scroll = QScrollArea(self.reminder_list)
        self.reminder_list_scroll.setObjectName(u"reminder_list_scroll")
        self.reminder_list_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 817, 290))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.reminder_list_container = QVBoxLayout()
        self.reminder_list_container.setObjectName(u"reminder_list_container")

        self.horizontalLayout.addLayout(self.reminder_list_container)

        self.reminder_list_scroll.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.reminder_list_scroll)

        self.content.addTab(self.reminder_list, "")

        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 843, 21))
        self.settings = QMenu(self.menubar)
        self.settings.setObjectName(u"settings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.settings.menuAction())
        self.settings.addAction(self.app)

        self.retranslateUi(MainWindow)

        self.content.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043b\u043e\u0433\u043e\u0432\u044b\u0439 \u043a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c", None))
        self.app.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.preference.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u0435", None))
        self.quote.setText(QCoreApplication.translate("MainWindow", u"\"\u042d\u043a\u043e\u043d\u043e\u043c\u0438\u0441\u0442 \u2013 \u044d\u0442\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0437\u043d\u0430\u0435\u0442 \u043e \u0434\u0435\u043d\u044c\u0433\u0430\u0445 \u0431\u043e\u043b\u044c\u0448\u0435, \u0447\u0435\u043c \u043b\u044e\u0434\u0438, \u0443 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0435\u0441\u0442\u044c \u0434\u0435\u043d\u044c\u0433\u0438.\" -  \u0424\u0440\u044d\u043d\u043a \u041b\u043e\u0448", None))
        self.content.setTabText(self.content.indexOf(self.new_reminder), QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u043e\u0435 \u043d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u0435", None))
        self.content.setTabText(self.content.indexOf(self.reminder_list), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u0439", None))
        self.settings.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

