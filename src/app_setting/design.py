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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_app_setting(object):
    def setupUi(self, app_setting):
        if not app_setting.objectName():
            app_setting.setObjectName(u"app_setting")
        app_setting.setEnabled(True)
        app_setting.resize(713, 486)
        self.verticalLayout_2 = QVBoxLayout(app_setting)
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_select_directory = QLabel(app_setting)
        self.label_select_directory.setObjectName(u"label_select_directory")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_select_directory.sizePolicy().hasHeightForWidth())
        self.label_select_directory.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_select_directory)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_select_directory = QPushButton(app_setting)
        self.btn_select_directory.setObjectName(u"btn_select_directory")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_select_directory.sizePolicy().hasHeightForWidth())
        self.btn_select_directory.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.btn_select_directory)

        self.label_selected_directory = QLabel(app_setting)
        self.label_selected_directory.setObjectName(u"label_selected_directory")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_selected_directory.sizePolicy().hasHeightForWidth())
        self.label_selected_directory.setSizePolicy(sizePolicy2)
        self.label_selected_directory.setStyleSheet(u"border: 1px solid #000;\n"
"border-radius: 4px;")

        self.horizontalLayout.addWidget(self.label_selected_directory)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(app_setting)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.label)

        self.select_delay = QSpinBox(app_setting)
        self.select_delay.setObjectName(u"select_delay")
        sizePolicy1.setHeightForWidth(self.select_delay.sizePolicy().hasHeightForWidth())
        self.select_delay.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.select_delay)

        self.label_2 = QLabel(app_setting)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.check_autostart = QCheckBox(app_setting)
        self.check_autostart.setObjectName(u"check_autostart")

        self.horizontalLayout_2.addWidget(self.check_autostart)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(app_setting)

        QMetaObject.connectSlotsByName(app_setting)
    # setupUi

    def retranslateUi(self, app_setting):
        app_setting.setWindowTitle(QCoreApplication.translate("app_setting", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
        self.label_select_directory.setText(QCoreApplication.translate("app_setting", u"\u041f\u0430\u043f\u043a\u0430 \u0434\u043b\u044f \u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0434\u0430\u043d\u043d\u044b\u0445:", None))
        self.btn_select_directory.setText(QCoreApplication.translate("app_setting", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label_selected_directory.setText(QCoreApplication.translate("app_setting", u"\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u044b\u0439 \u043f\u0443\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("app_setting", u"\u0423\u0432\u0435\u0434\u043e\u043c\u043b\u044f\u0442\u044c \u0437\u0430", None))
        self.label_2.setText(QCoreApplication.translate("app_setting", u"\u0447\u0430\u0441 (\u0430/\u043e\u0432)", None))
        self.check_autostart.setText(QCoreApplication.translate("app_setting", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u0430\u0432\u0442\u043e\u0437\u0430\u043f\u0443\u0441\u043a", None))
    # retranslateUi

