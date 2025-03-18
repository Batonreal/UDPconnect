# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QTmain.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 420)
        MainWindow.setMinimumSize(QSize(500, 420))
        MainWindow.setMaximumSize(QSize(500, 420))
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ipConfig = QLineEdit(self.centralwidget)
        self.ipConfig.setObjectName(u"ipConfig")
        font1 = QFont()
        font1.setPointSize(11)
        self.ipConfig.setFont(font1)

        self.horizontalLayout_2.addWidget(self.ipConfig)

        self.portConfig = QLineEdit(self.centralwidget)
        self.portConfig.setObjectName(u"portConfig")
        self.portConfig.setFont(font1)

        self.horizontalLayout_2.addWidget(self.portConfig)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(12, 0, -1, -1)
        self.ipInfo = QLabel(self.centralwidget)
        self.ipInfo.setObjectName(u"ipInfo")
        self.ipInfo.setMinimumSize(QSize(0, 0))
        self.ipInfo.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_3.addWidget(self.ipInfo)

        self.portInfo = QLabel(self.centralwidget)
        self.portInfo.setObjectName(u"portInfo")
        self.portInfo.setMinimumSize(QSize(0, 0))
        self.portInfo.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_3.addWidget(self.portInfo)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.textMessage = QLineEdit(self.centralwidget)
        self.textMessage.setObjectName(u"textMessage")
        self.textMessage.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textMessage.sizePolicy().hasHeightForWidth())
        self.textMessage.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(15)
        self.textMessage.setFont(font2)

        self.verticalLayout.addWidget(self.textMessage)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.verticalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.k_value = QSpinBox(self.centralwidget)
        self.k_value.setObjectName(u"k_value")
        self.k_value.setMaximumSize(QSize(90, 16777215))
        self.k_value.setFont(font1)
        self.k_value.setStyleSheet(u"")
        self.k_value.setValue(1)

        self.horizontalLayout_5.addWidget(self.k_value)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font3 = QFont()
        font3.setPointSize(13)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgba(0, 0, 0, 40);\n"
"border: 2px solid rgba(0, 0, 0, 50);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 80);\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgba(0, 0, 0, 40);\n"
"border: 2px solid rgba(0, 0, 0, 50);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 80);\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(96, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.pushAmplitude = QPushButton(self.centralwidget)
        self.pushAmplitude.setObjectName(u"pushAmplitude")
        self.pushAmplitude.setFont(font3)
        self.pushAmplitude.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgba(0, 0, 0, 40);\n"
"border: 2px solid rgba(0, 0, 0, 50);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 80);\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushAmplitude)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 24))
        self.menubar.setMaximumSize(QSize(16777215, 40))
        font4 = QFont()
        font4.setPointSize(10)
        self.menubar.setFont(font4)
        self.menubar.setStyleSheet(u"            QMenuBar {\n"
"                border-bottom: 1px solid rgb(179, 179, 179); /* \u0422\u043e\u043b\u0449\u0438\u043d\u0430, \u0441\u0442\u0438\u043b\u044c \u0438 \u0446\u0432\u0435\u0442 \u043b\u0438\u043d\u0438\u0438 */\n"
"                background-color: #f0f0f0; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 (\u043e\u043f\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e) */\n"
"            }\n"
"\n"
"            QMenuBar::item {\n"
"                background-color: #f0f0f0; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0443\u043d\u043a\u0442\u043e\u0432 \u043c\u0435\u043d\u044e (\u043e\u043f\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e) */\n"
"            }\n"
"\n"
"            QMenuBar::item:selected {\n"
"                background-color: #d0d0d0; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0445 \u043f\u0443\u043d\u043a\u0442\u043e\u0432 \u043c\u0435\u043d\u044e (\u043e\u043f\u0446\u0438\u043e\u043d"
                        "\u0430\u043b\u044c\u043d\u043e) */\n"
"            }")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_2.setMaximumSize(QSize(16777215, 25))
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_save)
        self.menu.addSeparator()
        self.menu.addAction(self.action_exit)
        self.menu_2.addAction(self.action_about)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"UDPmaster", None))
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 ip \u0430\u0434\u0440\u0435\u0441", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u043e\u0440\u0442", None))
        self.ipConfig.setText(QCoreApplication.translate("MainWindow", u"192.168.0.15", None))
        self.portConfig.setText(QCoreApplication.translate("MainWindow", u"6868", None))
        self.ipInfo.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0448 ip:", None))
        self.portInfo.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u044b\u0439 \u043f\u043e\u0440\u0442:", None))
        self.textMessage.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0431\u0430\u0439\u0442\u044b", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.pushAmplitude.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0430\u043c\u043f\u043b\u0438\u0442\u0443\u0434\u0443", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

