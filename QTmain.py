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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTextBrowser, QVBoxLayout,
    QWidget)

from colorled import ColorLed

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 650)
        MainWindow.setMinimumSize(QSize(1000, 650))
        MainWindow.setMaximumSize(QSize(1000, 650))
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
        self.portConfig.setStyleSheet(u"QLineEdit {\n"
"color: black;\n"
"border: 1px solid rgba(0, 0, 0, 100);\n"
"}")

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
        self.textBrowser.setStyleSheet(u"QTextBrowser {\n"
"color: black;\n"
"border: 1px solid rgba(0, 0, 0, 100);\n"
"}")

        self.verticalLayout.addWidget(self.textBrowser)

        self.verticalSpacer_2 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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
        self.select_mode = QSpinBox(self.centralwidget)
        self.select_mode.setObjectName(u"select_mode")
        self.select_mode.setMaximumSize(QSize(50, 16777215))
        self.select_mode.setFont(font1)
        self.select_mode.setMinimum(1)
        self.select_mode.setMaximum(3)

        self.horizontalLayout_6.addWidget(self.select_mode)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(50, 16777215))
        self.label_2.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(180, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

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

        self.time_data = QPushButton(self.centralwidget)
        self.time_data.setObjectName(u"time_data")
        self.time_data.setFont(font3)
        self.time_data.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.time_data)

        self.Reset_button = QPushButton(self.centralwidget)
        self.Reset_button.setObjectName(u"Reset_button")
        self.Reset_button.setFont(font3)
        self.Reset_button.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.Reset_button)

        self.SPI_button = QPushButton(self.centralwidget)
        self.SPI_button.setObjectName(u"SPI_button")
        self.SPI_button.setFont(font3)
        self.SPI_button.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.SPI_button)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.time_delay_box = QSpinBox(self.centralwidget)
        self.time_delay_box.setObjectName(u"time_delay_box")
        self.time_delay_box.setFont(font1)
        self.time_delay_box.setMinimum(-5000000)
        self.time_delay_box.setMaximum(5000000)

        self.horizontalLayout_7.addWidget(self.time_delay_box)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 16777215))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(False)
        self.label.setFont(font4)

        self.horizontalLayout_7.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.Layout_time1 = QHBoxLayout()
        self.Layout_time1.setObjectName(u"Layout_time1")
        self.Layout_time1.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.vertical_time1 = QVBoxLayout()
        self.vertical_time1.setObjectName(u"vertical_time1")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.vertical_time1.addWidget(self.label_5)

        self.time_period_1 = QSpinBox(self.centralwidget)
        self.time_period_1.setObjectName(u"time_period_1")
        self.time_period_1.setMaximum(5000)
        self.time_period_1.setSingleStep(10)
        self.time_period_1.setValue(0)

        self.vertical_time1.addWidget(self.time_period_1)


        self.Layout_time1.addLayout(self.vertical_time1)

        self.vertical_time2 = QVBoxLayout()
        self.vertical_time2.setObjectName(u"vertical_time2")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.vertical_time2.addWidget(self.label_6)

        self.time_period_2 = QSpinBox(self.centralwidget)
        self.time_period_2.setObjectName(u"time_period_2")
        self.time_period_2.setMaximum(5000)
        self.time_period_2.setSingleStep(10)
        self.time_period_2.setValue(330)

        self.vertical_time2.addWidget(self.time_period_2)


        self.Layout_time1.addLayout(self.vertical_time2)

        self.vertical_time3 = QVBoxLayout()
        self.vertical_time3.setObjectName(u"vertical_time3")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")

        self.vertical_time3.addWidget(self.label_15)

        self.time_period_3 = QSpinBox(self.centralwidget)
        self.time_period_3.setObjectName(u"time_period_3")
        self.time_period_3.setMaximum(5000)
        self.time_period_3.setSingleStep(10)
        self.time_period_3.setValue(830)

        self.vertical_time3.addWidget(self.time_period_3)


        self.Layout_time1.addLayout(self.vertical_time3)

        self.vertical_time4 = QVBoxLayout()
        self.vertical_time4.setObjectName(u"vertical_time4")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.vertical_time4.addWidget(self.label_16)

        self.time_period_4 = QSpinBox(self.centralwidget)
        self.time_period_4.setObjectName(u"time_period_4")
        self.time_period_4.setMaximum(5000)
        self.time_period_4.setSingleStep(10)
        self.time_period_4.setValue(1130)

        self.vertical_time4.addWidget(self.time_period_4)


        self.Layout_time1.addLayout(self.vertical_time4)


        self.verticalLayout.addLayout(self.Layout_time1)

        self.Layout_time2 = QHBoxLayout()
        self.Layout_time2.setObjectName(u"Layout_time2")
        self.Layout_time2.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.vertical_time5 = QVBoxLayout()
        self.vertical_time5.setObjectName(u"vertical_time5")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")

        self.vertical_time5.addWidget(self.label_17)

        self.time_period_5 = QSpinBox(self.centralwidget)
        self.time_period_5.setObjectName(u"time_period_5")
        self.time_period_5.setMaximum(5000)
        self.time_period_5.setSingleStep(10)
        self.time_period_5.setValue(3670)

        self.vertical_time5.addWidget(self.time_period_5)


        self.Layout_time2.addLayout(self.vertical_time5)

        self.vertical_time6 = QVBoxLayout()
        self.vertical_time6.setObjectName(u"vertical_time6")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")

        self.vertical_time6.addWidget(self.label_18)

        self.time_period_6 = QSpinBox(self.centralwidget)
        self.time_period_6.setObjectName(u"time_period_6")
        self.time_period_6.setMaximum(5000)
        self.time_period_6.setSingleStep(10)
        self.time_period_6.setValue(4170)

        self.vertical_time6.addWidget(self.time_period_6)


        self.Layout_time2.addLayout(self.vertical_time6)

        self.vertical_time7 = QVBoxLayout()
        self.vertical_time7.setObjectName(u"vertical_time7")
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")

        self.vertical_time7.addWidget(self.label_19)

        self.time_period_7 = QSpinBox(self.centralwidget)
        self.time_period_7.setObjectName(u"time_period_7")
        self.time_period_7.setMaximum(5000)
        self.time_period_7.setSingleStep(10)
        self.time_period_7.setValue(4670)

        self.vertical_time7.addWidget(self.time_period_7)


        self.Layout_time2.addLayout(self.vertical_time7)

        self.vertical_time8 = QVBoxLayout()
        self.vertical_time8.setObjectName(u"vertical_time8")
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")

        self.vertical_time8.addWidget(self.label_20)

        self.time_period_8 = QSpinBox(self.centralwidget)
        self.time_period_8.setObjectName(u"time_period_8")
        self.time_period_8.setMaximum(5000)
        self.time_period_8.setSingleStep(10)
        self.time_period_8.setValue(4970)

        self.vertical_time8.addWidget(self.time_period_8)


        self.Layout_time2.addLayout(self.vertical_time8)


        self.verticalLayout.addLayout(self.Layout_time2)

        self.time_period_button = QPushButton(self.centralwidget)
        self.time_period_button.setObjectName(u"time_period_button")
        self.time_period_button.setFont(font3)
        self.time_period_button.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.time_period_button)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setMinimumSize(QSize(500, 0))
        font5 = QFont()
        font5.setBold(False)
        self.widget.setFont(font5)
        self.widget.setStyleSheet(u"QWidget {\n"
"color: black;\n"
"background-color: rgba(0, 0, 0, 40);\n"
"border: 2px solid rgba(0, 0, 0, 50);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 50))
        font6 = QFont()
        font6.setPointSize(16)
        font6.setBold(False)
        self.label_7.setFont(font6)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(True)
        self.label_8.setFont(font7)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_8)

        self.groupBox_3 = QGroupBox(self.widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(16777215, 140))
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"color: black;\n"
"background-color: rgba(0, 0, 0, 10);\n"
"border: 2px solid rgba(0, 0, 0, 50);\n"
"}\n"
"\n"
"ColorLed {\n"
"color: white;\n"
"background-color: rgba(50, 50, 0, 10);\n"
"}")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.GMtext1 = QLabel(self.groupBox_3)
        self.GMtext1.setObjectName(u"GMtext1")
        self.GMtext1.setMaximumSize(QSize(45, 20))
        font8 = QFont()
        font8.setPointSize(9)
        font8.setBold(True)
        self.GMtext1.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext1, 0, 0, 1, 1)

        self.led1 = ColorLed(self.groupBox_3)
        self.led1.setObjectName(u"led1")
        self.led1.setMinimumSize(QSize(30, 30))
        self.led1.setMaximumSize(QSize(30, 30))
        self.led1.setSizeIncrement(QSize(30, 30))
        self.led1.setBaseSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.led1, 0, 1, 1, 1)

        self.GMtext2 = QLabel(self.groupBox_3)
        self.GMtext2.setObjectName(u"GMtext2")
        self.GMtext2.setMaximumSize(QSize(45, 20))
        self.GMtext2.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext2, 0, 2, 1, 1)

        self.led2 = ColorLed(self.groupBox_3)
        self.led2.setObjectName(u"led2")
        self.led2.setMinimumSize(QSize(30, 30))
        self.led2.setMaximumSize(QSize(30, 30))
        self.led2.setSizeIncrement(QSize(30, 30))
        self.led2.setBaseSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.led2, 0, 3, 1, 1)

        self.GMtext3 = QLabel(self.groupBox_3)
        self.GMtext3.setObjectName(u"GMtext3")
        self.GMtext3.setMaximumSize(QSize(45, 20))
        self.GMtext3.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext3, 0, 4, 1, 1)

        self.led3 = ColorLed(self.groupBox_3)
        self.led3.setObjectName(u"led3")
        self.led3.setMinimumSize(QSize(30, 30))
        self.led3.setMaximumSize(QSize(30, 30))
        self.led3.setSizeIncrement(QSize(30, 30))
        self.led3.setBaseSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.led3, 0, 5, 1, 1)

        self.GMtext4 = QLabel(self.groupBox_3)
        self.GMtext4.setObjectName(u"GMtext4")
        self.GMtext4.setMaximumSize(QSize(45, 20))
        self.GMtext4.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext4, 0, 6, 1, 1)

        self.led4 = ColorLed(self.groupBox_3)
        self.led4.setObjectName(u"led4")
        self.led4.setMinimumSize(QSize(30, 30))
        self.led4.setMaximumSize(QSize(30, 30))
        self.led4.setSizeIncrement(QSize(30, 30))
        self.led4.setBaseSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.led4, 0, 7, 1, 1)

        self.GMtext5 = QLabel(self.groupBox_3)
        self.GMtext5.setObjectName(u"GMtext5")
        self.GMtext5.setMaximumSize(QSize(45, 20))
        self.GMtext5.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext5, 0, 8, 1, 1)

        self.led5 = ColorLed(self.groupBox_3)
        self.led5.setObjectName(u"led5")
        self.led5.setMinimumSize(QSize(30, 30))
        self.led5.setMaximumSize(QSize(30, 30))
        self.led5.setSizeIncrement(QSize(30, 30))
        self.led5.setBaseSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.led5, 0, 9, 1, 1)

        self.GMtext6 = QLabel(self.groupBox_3)
        self.GMtext6.setObjectName(u"GMtext6")
        self.GMtext6.setMaximumSize(QSize(45, 20))
        self.GMtext6.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext6, 1, 0, 1, 1)

        self.led6 = ColorLed(self.groupBox_3)
        self.led6.setObjectName(u"led6")
        self.led6.setMinimumSize(QSize(30, 30))
        self.led6.setMaximumSize(QSize(30, 30))
        self.led6.setSizeIncrement(QSize(30, 30))
        self.led6.setBaseSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.led6, 1, 1, 1, 1)

        self.GMtext7 = QLabel(self.groupBox_3)
        self.GMtext7.setObjectName(u"GMtext7")
        self.GMtext7.setMaximumSize(QSize(45, 20))
        self.GMtext7.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext7, 1, 2, 1, 1)

        self.led7 = ColorLed(self.groupBox_3)
        self.led7.setObjectName(u"led7")
        self.led7.setMinimumSize(QSize(30, 30))
        self.led7.setMaximumSize(QSize(30, 30))
        self.led7.setSizeIncrement(QSize(30, 30))
        self.led7.setBaseSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.led7, 1, 3, 1, 1)

        self.GMtext8 = QLabel(self.groupBox_3)
        self.GMtext8.setObjectName(u"GMtext8")
        self.GMtext8.setMaximumSize(QSize(45, 20))
        self.GMtext8.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext8, 1, 4, 1, 1)

        self.led8 = ColorLed(self.groupBox_3)
        self.led8.setObjectName(u"led8")
        self.led8.setMinimumSize(QSize(30, 30))
        self.led8.setMaximumSize(QSize(30, 30))
        self.led8.setSizeIncrement(QSize(30, 30))
        self.led8.setBaseSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.led8, 1, 5, 1, 1)

        self.GMtext9 = QLabel(self.groupBox_3)
        self.GMtext9.setObjectName(u"GMtext9")
        self.GMtext9.setMaximumSize(QSize(45, 20))
        self.GMtext9.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext9, 1, 6, 1, 1)

        self.led9 = ColorLed(self.groupBox_3)
        self.led9.setObjectName(u"led9")
        self.led9.setMinimumSize(QSize(30, 30))
        self.led9.setMaximumSize(QSize(30, 30))
        self.led9.setSizeIncrement(QSize(30, 30))
        self.led9.setBaseSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.led9, 1, 7, 1, 1)

        self.GMtext10 = QLabel(self.groupBox_3)
        self.GMtext10.setObjectName(u"GMtext10")
        self.GMtext10.setMaximumSize(QSize(45, 20))
        self.GMtext10.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext10, 1, 8, 1, 1)

        self.led10 = ColorLed(self.groupBox_3)
        self.led10.setObjectName(u"led10")
        self.led10.setMinimumSize(QSize(30, 30))
        self.led10.setMaximumSize(QSize(30, 30))
        self.led10.setSizeIncrement(QSize(30, 30))
        self.led10.setBaseSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.led10, 1, 9, 1, 1)

        self.GMtext11 = QLabel(self.groupBox_3)
        self.GMtext11.setObjectName(u"GMtext11")
        self.GMtext11.setMaximumSize(QSize(45, 20))
        self.GMtext11.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext11, 2, 0, 1, 1)

        self.led11 = ColorLed(self.groupBox_3)
        self.led11.setObjectName(u"led11")
        self.led11.setMinimumSize(QSize(30, 30))
        self.led11.setMaximumSize(QSize(30, 30))
        self.led11.setSizeIncrement(QSize(30, 30))
        self.led11.setBaseSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.led11, 2, 1, 1, 1)

        self.GMtext12 = QLabel(self.groupBox_3)
        self.GMtext12.setObjectName(u"GMtext12")
        self.GMtext12.setMaximumSize(QSize(45, 20))
        self.GMtext12.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext12, 2, 2, 1, 1)

        self.led12 = ColorLed(self.groupBox_3)
        self.led12.setObjectName(u"led12")
        self.led12.setMinimumSize(QSize(30, 30))
        self.led12.setMaximumSize(QSize(30, 30))
        self.led12.setSizeIncrement(QSize(30, 30))
        self.led12.setBaseSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.led12, 2, 3, 1, 1)

        self.GMtext13 = QLabel(self.groupBox_3)
        self.GMtext13.setObjectName(u"GMtext13")
        self.GMtext13.setMaximumSize(QSize(45, 20))
        self.GMtext13.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext13, 2, 4, 1, 1)

        self.led13 = ColorLed(self.groupBox_3)
        self.led13.setObjectName(u"led13")
        self.led13.setMinimumSize(QSize(30, 30))
        self.led13.setMaximumSize(QSize(30, 30))
        self.led13.setSizeIncrement(QSize(30, 30))
        self.led13.setBaseSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.led13, 2, 5, 1, 1)

        self.GMtext14 = QLabel(self.groupBox_3)
        self.GMtext14.setObjectName(u"GMtext14")
        self.GMtext14.setMaximumSize(QSize(45, 20))
        self.GMtext14.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext14, 2, 6, 1, 1)

        self.led14 = ColorLed(self.groupBox_3)
        self.led14.setObjectName(u"led14")
        self.led14.setMinimumSize(QSize(30, 30))
        self.led14.setMaximumSize(QSize(30, 30))
        self.led14.setSizeIncrement(QSize(30, 30))
        self.led14.setBaseSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.led14, 2, 7, 1, 1)

        self.GMtext15 = QLabel(self.groupBox_3)
        self.GMtext15.setObjectName(u"GMtext15")
        self.GMtext15.setMaximumSize(QSize(45, 20))
        self.GMtext15.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext15, 2, 8, 1, 1)

        self.led15 = ColorLed(self.groupBox_3)
        self.led15.setObjectName(u"led15")
        self.led15.setMinimumSize(QSize(30, 30))
        self.led15.setMaximumSize(QSize(30, 30))
        self.led15.setSizeIncrement(QSize(30, 30))
        self.led15.setBaseSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.led15, 2, 9, 1, 1)

        self.GMtext16 = QLabel(self.groupBox_3)
        self.GMtext16.setObjectName(u"GMtext16")
        self.GMtext16.setMaximumSize(QSize(45, 20))
        self.GMtext16.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext16, 3, 0, 1, 1)

        self.led16 = ColorLed(self.groupBox_3)
        self.led16.setObjectName(u"led16")
        self.led16.setMinimumSize(QSize(30, 30))
        self.led16.setMaximumSize(QSize(30, 30))
        self.led16.setSizeIncrement(QSize(30, 30))
        self.led16.setBaseSize(QSize(30, 30))
        self.led16.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.led16, 3, 1, 1, 1)

        self.GMtext17 = QLabel(self.groupBox_3)
        self.GMtext17.setObjectName(u"GMtext17")
        self.GMtext17.setMaximumSize(QSize(45, 20))
        self.GMtext17.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext17, 3, 2, 1, 1)

        self.led17 = ColorLed(self.groupBox_3)
        self.led17.setObjectName(u"led17")
        self.led17.setMinimumSize(QSize(30, 30))
        self.led17.setMaximumSize(QSize(30, 30))
        self.led17.setSizeIncrement(QSize(30, 30))
        self.led17.setBaseSize(QSize(30, 30))
        self.led17.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.led17, 3, 3, 1, 1)

        self.GMtext18 = QLabel(self.groupBox_3)
        self.GMtext18.setObjectName(u"GMtext18")
        self.GMtext18.setMaximumSize(QSize(45, 20))
        self.GMtext18.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext18, 3, 4, 1, 1)

        self.led18 = ColorLed(self.groupBox_3)
        self.led18.setObjectName(u"led18")
        self.led18.setMinimumSize(QSize(30, 30))
        self.led18.setMaximumSize(QSize(30, 30))
        self.led18.setSizeIncrement(QSize(30, 30))
        self.led18.setBaseSize(QSize(30, 30))
        self.led18.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.led18, 3, 5, 1, 1)

        self.GMtext19 = QLabel(self.groupBox_3)
        self.GMtext19.setObjectName(u"GMtext19")
        self.GMtext19.setMaximumSize(QSize(45, 20))
        self.GMtext19.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext19, 3, 6, 1, 1)

        self.led19 = ColorLed(self.groupBox_3)
        self.led19.setObjectName(u"led19")
        self.led19.setMinimumSize(QSize(30, 30))
        self.led19.setMaximumSize(QSize(30, 30))
        self.led19.setSizeIncrement(QSize(30, 30))
        self.led19.setBaseSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.led19, 3, 7, 1, 1)

        self.GMtext20 = QLabel(self.groupBox_3)
        self.GMtext20.setObjectName(u"GMtext20")
        self.GMtext20.setMaximumSize(QSize(45, 20))
        self.GMtext20.setFont(font8)

        self.gridLayout_4.addWidget(self.GMtext20, 3, 8, 1, 1)

        self.led20 = ColorLed(self.groupBox_3)
        self.led20.setObjectName(u"led20")
        self.led20.setMinimumSize(QSize(30, 30))
        self.led20.setMaximumSize(QSize(30, 30))
        self.led20.setSizeIncrement(QSize(30, 30))
        self.led20.setBaseSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.led20, 3, 9, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font7)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_9)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 140))
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"color: black;\n"
"background-color: rgba(0, 0, 0, 10);\n"
"border: 2px solid rgba(0, 0, 0, 50);\n"
"}\n"
"\n"
"ColorLed {\n"
"color: white;\n"
"background-color: rgba(50, 50, 0, 10);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.led15_2 = ColorLed(self.groupBox)
        self.led15_2.setObjectName(u"led15_2")
        self.led15_2.setMinimumSize(QSize(30, 30))
        self.led15_2.setMaximumSize(QSize(30, 30))
        self.led15_2.setSizeIncrement(QSize(30, 30))
        self.led15_2.setBaseSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.led15_2, 2, 9, 1, 1)

        self.GMtext8_2 = QLabel(self.groupBox)
        self.GMtext8_2.setObjectName(u"GMtext8_2")
        self.GMtext8_2.setMaximumSize(QSize(45, 20))
        self.GMtext8_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext8_2, 1, 4, 1, 1)

        self.GMtext6_2 = QLabel(self.groupBox)
        self.GMtext6_2.setObjectName(u"GMtext6_2")
        self.GMtext6_2.setMaximumSize(QSize(45, 20))
        self.GMtext6_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext6_2, 1, 0, 1, 1)

        self.GMtext13_2 = QLabel(self.groupBox)
        self.GMtext13_2.setObjectName(u"GMtext13_2")
        self.GMtext13_2.setMaximumSize(QSize(45, 20))
        self.GMtext13_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext13_2, 2, 4, 1, 1)

        self.led11_2 = ColorLed(self.groupBox)
        self.led11_2.setObjectName(u"led11_2")
        self.led11_2.setMinimumSize(QSize(30, 30))
        self.led11_2.setMaximumSize(QSize(30, 30))
        self.led11_2.setSizeIncrement(QSize(30, 30))
        self.led11_2.setBaseSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.led11_2, 2, 1, 1, 1)

        self.GMtext1_2 = QLabel(self.groupBox)
        self.GMtext1_2.setObjectName(u"GMtext1_2")
        self.GMtext1_2.setMaximumSize(QSize(45, 20))
        self.GMtext1_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext1_2, 0, 0, 1, 1)

        self.led7_2 = ColorLed(self.groupBox)
        self.led7_2.setObjectName(u"led7_2")
        self.led7_2.setMinimumSize(QSize(30, 30))
        self.led7_2.setMaximumSize(QSize(30, 30))
        self.led7_2.setSizeIncrement(QSize(30, 30))
        self.led7_2.setBaseSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.led7_2, 1, 3, 1, 1)

        self.led12_2 = ColorLed(self.groupBox)
        self.led12_2.setObjectName(u"led12_2")
        self.led12_2.setMinimumSize(QSize(30, 30))
        self.led12_2.setMaximumSize(QSize(30, 30))
        self.led12_2.setSizeIncrement(QSize(30, 30))
        self.led12_2.setBaseSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.led12_2, 2, 3, 1, 1)

        self.GMtext7_2 = QLabel(self.groupBox)
        self.GMtext7_2.setObjectName(u"GMtext7_2")
        self.GMtext7_2.setMaximumSize(QSize(45, 20))
        self.GMtext7_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext7_2, 1, 2, 1, 1)

        self.GMtext4_2 = QLabel(self.groupBox)
        self.GMtext4_2.setObjectName(u"GMtext4_2")
        self.GMtext4_2.setMaximumSize(QSize(45, 20))
        self.GMtext4_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext4_2, 0, 6, 1, 1)

        self.led5_2 = ColorLed(self.groupBox)
        self.led5_2.setObjectName(u"led5_2")
        self.led5_2.setMinimumSize(QSize(30, 30))
        self.led5_2.setMaximumSize(QSize(30, 30))
        self.led5_2.setSizeIncrement(QSize(30, 30))
        self.led5_2.setBaseSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.led5_2, 0, 9, 1, 1)

        self.led14_2 = ColorLed(self.groupBox)
        self.led14_2.setObjectName(u"led14_2")
        self.led14_2.setMinimumSize(QSize(30, 30))
        self.led14_2.setMaximumSize(QSize(30, 30))
        self.led14_2.setSizeIncrement(QSize(30, 30))
        self.led14_2.setBaseSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.led14_2, 2, 7, 1, 1)

        self.GMtext20_2 = QLabel(self.groupBox)
        self.GMtext20_2.setObjectName(u"GMtext20_2")
        self.GMtext20_2.setMaximumSize(QSize(45, 20))
        self.GMtext20_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext20_2, 3, 8, 1, 1)

        self.GMtext5_2 = QLabel(self.groupBox)
        self.GMtext5_2.setObjectName(u"GMtext5_2")
        self.GMtext5_2.setMaximumSize(QSize(45, 20))
        self.GMtext5_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext5_2, 0, 8, 1, 1)

        self.led8_2 = ColorLed(self.groupBox)
        self.led8_2.setObjectName(u"led8_2")
        self.led8_2.setMinimumSize(QSize(30, 30))
        self.led8_2.setMaximumSize(QSize(30, 30))
        self.led8_2.setSizeIncrement(QSize(30, 30))
        self.led8_2.setBaseSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.led8_2, 1, 5, 1, 1)

        self.GMtext10_2 = QLabel(self.groupBox)
        self.GMtext10_2.setObjectName(u"GMtext10_2")
        self.GMtext10_2.setMaximumSize(QSize(45, 20))
        self.GMtext10_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext10_2, 1, 8, 1, 1)

        self.led18_2 = ColorLed(self.groupBox)
        self.led18_2.setObjectName(u"led18_2")
        self.led18_2.setMinimumSize(QSize(30, 30))
        self.led18_2.setMaximumSize(QSize(30, 30))
        self.led18_2.setSizeIncrement(QSize(30, 30))
        self.led18_2.setBaseSize(QSize(30, 30))
        self.led18_2.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.led18_2, 3, 5, 1, 1)

        self.GMtext3_2 = QLabel(self.groupBox)
        self.GMtext3_2.setObjectName(u"GMtext3_2")
        self.GMtext3_2.setMaximumSize(QSize(45, 20))
        self.GMtext3_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext3_2, 0, 4, 1, 1)

        self.GMtext9_2 = QLabel(self.groupBox)
        self.GMtext9_2.setObjectName(u"GMtext9_2")
        self.GMtext9_2.setMaximumSize(QSize(45, 20))
        self.GMtext9_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext9_2, 1, 6, 1, 1)

        self.GMtext2_2 = QLabel(self.groupBox)
        self.GMtext2_2.setObjectName(u"GMtext2_2")
        self.GMtext2_2.setMaximumSize(QSize(45, 20))
        self.GMtext2_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext2_2, 0, 2, 1, 1)

        self.led6_2 = ColorLed(self.groupBox)
        self.led6_2.setObjectName(u"led6_2")
        self.led6_2.setMinimumSize(QSize(30, 30))
        self.led6_2.setMaximumSize(QSize(30, 30))
        self.led6_2.setSizeIncrement(QSize(30, 30))
        self.led6_2.setBaseSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.led6_2, 1, 1, 1, 1)

        self.GMtext11_2 = QLabel(self.groupBox)
        self.GMtext11_2.setObjectName(u"GMtext11_2")
        self.GMtext11_2.setMaximumSize(QSize(45, 20))
        self.GMtext11_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext11_2, 2, 0, 1, 1)

        self.led19_2 = ColorLed(self.groupBox)
        self.led19_2.setObjectName(u"led19_2")
        self.led19_2.setMinimumSize(QSize(30, 30))
        self.led19_2.setMaximumSize(QSize(30, 30))
        self.led19_2.setSizeIncrement(QSize(30, 30))
        self.led19_2.setBaseSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.led19_2, 3, 7, 1, 1)

        self.led10_2 = ColorLed(self.groupBox)
        self.led10_2.setObjectName(u"led10_2")
        self.led10_2.setMinimumSize(QSize(30, 30))
        self.led10_2.setMaximumSize(QSize(30, 30))
        self.led10_2.setSizeIncrement(QSize(30, 30))
        self.led10_2.setBaseSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.led10_2, 1, 9, 1, 1)

        self.led20_2 = ColorLed(self.groupBox)
        self.led20_2.setObjectName(u"led20_2")
        self.led20_2.setMinimumSize(QSize(30, 30))
        self.led20_2.setMaximumSize(QSize(30, 30))
        self.led20_2.setSizeIncrement(QSize(30, 30))
        self.led20_2.setBaseSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.led20_2, 3, 9, 1, 1)

        self.GMtext14_2 = QLabel(self.groupBox)
        self.GMtext14_2.setObjectName(u"GMtext14_2")
        self.GMtext14_2.setMaximumSize(QSize(45, 20))
        self.GMtext14_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext14_2, 2, 6, 1, 1)

        self.led13_2 = ColorLed(self.groupBox)
        self.led13_2.setObjectName(u"led13_2")
        self.led13_2.setMinimumSize(QSize(30, 30))
        self.led13_2.setMaximumSize(QSize(30, 30))
        self.led13_2.setSizeIncrement(QSize(30, 30))
        self.led13_2.setBaseSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.led13_2, 2, 5, 1, 1)

        self.led3_2 = ColorLed(self.groupBox)
        self.led3_2.setObjectName(u"led3_2")
        self.led3_2.setMinimumSize(QSize(30, 30))
        self.led3_2.setMaximumSize(QSize(30, 30))
        self.led3_2.setSizeIncrement(QSize(30, 30))
        self.led3_2.setBaseSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.led3_2, 0, 5, 1, 1)

        self.led1_2 = ColorLed(self.groupBox)
        self.led1_2.setObjectName(u"led1_2")
        self.led1_2.setMinimumSize(QSize(30, 30))
        self.led1_2.setMaximumSize(QSize(30, 30))
        self.led1_2.setSizeIncrement(QSize(30, 30))
        self.led1_2.setBaseSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.led1_2, 0, 1, 1, 1)

        self.led4_2 = ColorLed(self.groupBox)
        self.led4_2.setObjectName(u"led4_2")
        self.led4_2.setMinimumSize(QSize(30, 30))
        self.led4_2.setMaximumSize(QSize(30, 30))
        self.led4_2.setSizeIncrement(QSize(30, 30))
        self.led4_2.setBaseSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.led4_2, 0, 7, 1, 1)

        self.led2_2 = ColorLed(self.groupBox)
        self.led2_2.setObjectName(u"led2_2")
        self.led2_2.setMinimumSize(QSize(30, 30))
        self.led2_2.setMaximumSize(QSize(30, 30))
        self.led2_2.setSizeIncrement(QSize(30, 30))
        self.led2_2.setBaseSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.led2_2, 0, 3, 1, 1)

        self.GMtext15_2 = QLabel(self.groupBox)
        self.GMtext15_2.setObjectName(u"GMtext15_2")
        self.GMtext15_2.setMaximumSize(QSize(45, 20))
        self.GMtext15_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext15_2, 2, 8, 1, 1)

        self.led16_2 = ColorLed(self.groupBox)
        self.led16_2.setObjectName(u"led16_2")
        self.led16_2.setMinimumSize(QSize(30, 30))
        self.led16_2.setMaximumSize(QSize(30, 30))
        self.led16_2.setSizeIncrement(QSize(30, 30))
        self.led16_2.setBaseSize(QSize(30, 30))
        self.led16_2.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.led16_2, 3, 1, 1, 1)

        self.GMtext18_2 = QLabel(self.groupBox)
        self.GMtext18_2.setObjectName(u"GMtext18_2")
        self.GMtext18_2.setMaximumSize(QSize(45, 20))
        self.GMtext18_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext18_2, 3, 4, 1, 1)

        self.GMtext17_2 = QLabel(self.groupBox)
        self.GMtext17_2.setObjectName(u"GMtext17_2")
        self.GMtext17_2.setMaximumSize(QSize(45, 20))
        self.GMtext17_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext17_2, 3, 2, 1, 1)

        self.GMtext16_2 = QLabel(self.groupBox)
        self.GMtext16_2.setObjectName(u"GMtext16_2")
        self.GMtext16_2.setMaximumSize(QSize(45, 20))
        self.GMtext16_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext16_2, 3, 0, 1, 1)

        self.GMtext19_2 = QLabel(self.groupBox)
        self.GMtext19_2.setObjectName(u"GMtext19_2")
        self.GMtext19_2.setMaximumSize(QSize(45, 20))
        self.GMtext19_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext19_2, 3, 6, 1, 1)

        self.GMtext12_2 = QLabel(self.groupBox)
        self.GMtext12_2.setObjectName(u"GMtext12_2")
        self.GMtext12_2.setMaximumSize(QSize(45, 20))
        self.GMtext12_2.setFont(font8)

        self.gridLayout_2.addWidget(self.GMtext12_2, 2, 2, 1, 1)

        self.led17_2 = ColorLed(self.groupBox)
        self.led17_2.setObjectName(u"led17_2")
        self.led17_2.setMinimumSize(QSize(30, 30))
        self.led17_2.setMaximumSize(QSize(30, 30))
        self.led17_2.setSizeIncrement(QSize(30, 30))
        self.led17_2.setBaseSize(QSize(30, 30))
        self.led17_2.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.led17_2, 3, 3, 1, 1)

        self.led9_2 = ColorLed(self.groupBox)
        self.led9_2.setObjectName(u"led9_2")
        self.led9_2.setMinimumSize(QSize(30, 30))
        self.led9_2.setMaximumSize(QSize(30, 30))
        self.led9_2.setSizeIncrement(QSize(30, 30))
        self.led9_2.setBaseSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.led9_2, 1, 7, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font7)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_10)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 140))
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"color: black;\n"
"background-color: rgba(0, 0, 0, 10);\n"
"border: 2px solid rgba(0, 0, 0, 50);\n"
"}\n"
"\n"
"ColorLed {\n"
"color: white;\n"
"background-color: rgba(50, 50, 0, 10);\n"
"}")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.GMtext1_3 = QLabel(self.groupBox_2)
        self.GMtext1_3.setObjectName(u"GMtext1_3")
        self.GMtext1_3.setMaximumSize(QSize(45, 20))
        self.GMtext1_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext1_3, 0, 0, 1, 1)

        self.led1_3 = ColorLed(self.groupBox_2)
        self.led1_3.setObjectName(u"led1_3")
        self.led1_3.setMinimumSize(QSize(30, 30))
        self.led1_3.setMaximumSize(QSize(30, 30))
        self.led1_3.setSizeIncrement(QSize(30, 30))
        self.led1_3.setBaseSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.led1_3, 0, 1, 1, 1)

        self.GMtext2_3 = QLabel(self.groupBox_2)
        self.GMtext2_3.setObjectName(u"GMtext2_3")
        self.GMtext2_3.setMaximumSize(QSize(45, 20))
        self.GMtext2_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext2_3, 0, 2, 1, 1)

        self.led2_3 = ColorLed(self.groupBox_2)
        self.led2_3.setObjectName(u"led2_3")
        self.led2_3.setMinimumSize(QSize(30, 30))
        self.led2_3.setMaximumSize(QSize(30, 30))
        self.led2_3.setSizeIncrement(QSize(30, 30))
        self.led2_3.setBaseSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.led2_3, 0, 3, 1, 1)

        self.GMtext3_3 = QLabel(self.groupBox_2)
        self.GMtext3_3.setObjectName(u"GMtext3_3")
        self.GMtext3_3.setMaximumSize(QSize(45, 20))
        self.GMtext3_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext3_3, 0, 4, 1, 1)

        self.led3_3 = ColorLed(self.groupBox_2)
        self.led3_3.setObjectName(u"led3_3")
        self.led3_3.setMinimumSize(QSize(30, 30))
        self.led3_3.setMaximumSize(QSize(30, 30))
        self.led3_3.setSizeIncrement(QSize(30, 30))
        self.led3_3.setBaseSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.led3_3, 0, 5, 1, 1)

        self.GMtext4_3 = QLabel(self.groupBox_2)
        self.GMtext4_3.setObjectName(u"GMtext4_3")
        self.GMtext4_3.setMaximumSize(QSize(45, 20))
        self.GMtext4_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext4_3, 0, 6, 1, 1)

        self.led4_3 = ColorLed(self.groupBox_2)
        self.led4_3.setObjectName(u"led4_3")
        self.led4_3.setMinimumSize(QSize(30, 30))
        self.led4_3.setMaximumSize(QSize(30, 30))
        self.led4_3.setSizeIncrement(QSize(30, 30))
        self.led4_3.setBaseSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.led4_3, 0, 7, 1, 1)

        self.GMtext5_3 = QLabel(self.groupBox_2)
        self.GMtext5_3.setObjectName(u"GMtext5_3")
        self.GMtext5_3.setMaximumSize(QSize(45, 20))
        self.GMtext5_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext5_3, 0, 8, 1, 1)

        self.led5_3 = ColorLed(self.groupBox_2)
        self.led5_3.setObjectName(u"led5_3")
        self.led5_3.setMinimumSize(QSize(30, 30))
        self.led5_3.setMaximumSize(QSize(30, 30))
        self.led5_3.setSizeIncrement(QSize(30, 30))
        self.led5_3.setBaseSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.led5_3, 0, 9, 1, 1)

        self.GMtext6_3 = QLabel(self.groupBox_2)
        self.GMtext6_3.setObjectName(u"GMtext6_3")
        self.GMtext6_3.setMaximumSize(QSize(45, 20))
        self.GMtext6_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext6_3, 1, 0, 1, 1)

        self.led6_3 = ColorLed(self.groupBox_2)
        self.led6_3.setObjectName(u"led6_3")
        self.led6_3.setMinimumSize(QSize(30, 30))
        self.led6_3.setMaximumSize(QSize(30, 30))
        self.led6_3.setSizeIncrement(QSize(30, 30))
        self.led6_3.setBaseSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.led6_3, 1, 1, 1, 1)

        self.GMtext7_3 = QLabel(self.groupBox_2)
        self.GMtext7_3.setObjectName(u"GMtext7_3")
        self.GMtext7_3.setMaximumSize(QSize(45, 20))
        self.GMtext7_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext7_3, 1, 2, 1, 1)

        self.led7_3 = ColorLed(self.groupBox_2)
        self.led7_3.setObjectName(u"led7_3")
        self.led7_3.setMinimumSize(QSize(30, 30))
        self.led7_3.setMaximumSize(QSize(30, 30))
        self.led7_3.setSizeIncrement(QSize(30, 30))
        self.led7_3.setBaseSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.led7_3, 1, 3, 1, 1)

        self.GMtext8_3 = QLabel(self.groupBox_2)
        self.GMtext8_3.setObjectName(u"GMtext8_3")
        self.GMtext8_3.setMaximumSize(QSize(45, 20))
        self.GMtext8_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext8_3, 1, 4, 1, 1)

        self.led8_3 = ColorLed(self.groupBox_2)
        self.led8_3.setObjectName(u"led8_3")
        self.led8_3.setMinimumSize(QSize(30, 30))
        self.led8_3.setMaximumSize(QSize(30, 30))
        self.led8_3.setSizeIncrement(QSize(30, 30))
        self.led8_3.setBaseSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.led8_3, 1, 5, 1, 1)

        self.GMtext9_3 = QLabel(self.groupBox_2)
        self.GMtext9_3.setObjectName(u"GMtext9_3")
        self.GMtext9_3.setMaximumSize(QSize(45, 20))
        self.GMtext9_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext9_3, 1, 6, 1, 1)

        self.led9_3 = ColorLed(self.groupBox_2)
        self.led9_3.setObjectName(u"led9_3")
        self.led9_3.setMinimumSize(QSize(30, 30))
        self.led9_3.setMaximumSize(QSize(30, 30))
        self.led9_3.setSizeIncrement(QSize(30, 30))
        self.led9_3.setBaseSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.led9_3, 1, 7, 1, 1)

        self.GMtext10_3 = QLabel(self.groupBox_2)
        self.GMtext10_3.setObjectName(u"GMtext10_3")
        self.GMtext10_3.setMaximumSize(QSize(45, 20))
        self.GMtext10_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext10_3, 1, 8, 1, 1)

        self.led10_3 = ColorLed(self.groupBox_2)
        self.led10_3.setObjectName(u"led10_3")
        self.led10_3.setMinimumSize(QSize(30, 30))
        self.led10_3.setMaximumSize(QSize(30, 30))
        self.led10_3.setSizeIncrement(QSize(30, 30))
        self.led10_3.setBaseSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.led10_3, 1, 9, 1, 1)

        self.GMtext11_3 = QLabel(self.groupBox_2)
        self.GMtext11_3.setObjectName(u"GMtext11_3")
        self.GMtext11_3.setMaximumSize(QSize(45, 20))
        self.GMtext11_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext11_3, 2, 0, 1, 1)

        self.led11_3 = ColorLed(self.groupBox_2)
        self.led11_3.setObjectName(u"led11_3")
        self.led11_3.setMinimumSize(QSize(30, 30))
        self.led11_3.setMaximumSize(QSize(30, 30))
        self.led11_3.setSizeIncrement(QSize(30, 30))
        self.led11_3.setBaseSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.led11_3, 2, 1, 1, 1)

        self.GMtext12_3 = QLabel(self.groupBox_2)
        self.GMtext12_3.setObjectName(u"GMtext12_3")
        self.GMtext12_3.setMaximumSize(QSize(45, 20))
        self.GMtext12_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext12_3, 2, 2, 1, 1)

        self.led12_3 = ColorLed(self.groupBox_2)
        self.led12_3.setObjectName(u"led12_3")
        self.led12_3.setMinimumSize(QSize(30, 30))
        self.led12_3.setMaximumSize(QSize(30, 30))
        self.led12_3.setSizeIncrement(QSize(30, 30))
        self.led12_3.setBaseSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.led12_3, 2, 3, 1, 1)

        self.GMtext13_3 = QLabel(self.groupBox_2)
        self.GMtext13_3.setObjectName(u"GMtext13_3")
        self.GMtext13_3.setMaximumSize(QSize(45, 20))
        self.GMtext13_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext13_3, 2, 4, 1, 1)

        self.led13_3 = ColorLed(self.groupBox_2)
        self.led13_3.setObjectName(u"led13_3")
        self.led13_3.setMinimumSize(QSize(30, 30))
        self.led13_3.setMaximumSize(QSize(30, 30))
        self.led13_3.setSizeIncrement(QSize(30, 30))
        self.led13_3.setBaseSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.led13_3, 2, 5, 1, 1)

        self.GMtext14_3 = QLabel(self.groupBox_2)
        self.GMtext14_3.setObjectName(u"GMtext14_3")
        self.GMtext14_3.setMaximumSize(QSize(45, 20))
        self.GMtext14_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext14_3, 2, 6, 1, 1)

        self.led14_3 = ColorLed(self.groupBox_2)
        self.led14_3.setObjectName(u"led14_3")
        self.led14_3.setMinimumSize(QSize(30, 30))
        self.led14_3.setMaximumSize(QSize(30, 30))
        self.led14_3.setSizeIncrement(QSize(30, 30))
        self.led14_3.setBaseSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.led14_3, 2, 7, 1, 1)

        self.GMtext15_3 = QLabel(self.groupBox_2)
        self.GMtext15_3.setObjectName(u"GMtext15_3")
        self.GMtext15_3.setMaximumSize(QSize(45, 20))
        self.GMtext15_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext15_3, 2, 8, 1, 1)

        self.led15_3 = ColorLed(self.groupBox_2)
        self.led15_3.setObjectName(u"led15_3")
        self.led15_3.setMinimumSize(QSize(30, 30))
        self.led15_3.setMaximumSize(QSize(30, 30))
        self.led15_3.setSizeIncrement(QSize(30, 30))
        self.led15_3.setBaseSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.led15_3, 2, 9, 1, 1)

        self.GMtext16_3 = QLabel(self.groupBox_2)
        self.GMtext16_3.setObjectName(u"GMtext16_3")
        self.GMtext16_3.setMaximumSize(QSize(45, 20))
        self.GMtext16_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext16_3, 3, 0, 1, 1)

        self.led16_3 = ColorLed(self.groupBox_2)
        self.led16_3.setObjectName(u"led16_3")
        self.led16_3.setMinimumSize(QSize(30, 30))
        self.led16_3.setMaximumSize(QSize(30, 30))
        self.led16_3.setSizeIncrement(QSize(30, 30))
        self.led16_3.setBaseSize(QSize(30, 30))
        self.led16_3.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.led16_3, 3, 1, 1, 1)

        self.GMtext17_3 = QLabel(self.groupBox_2)
        self.GMtext17_3.setObjectName(u"GMtext17_3")
        self.GMtext17_3.setMaximumSize(QSize(45, 20))
        self.GMtext17_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext17_3, 3, 2, 1, 1)

        self.led17_3 = ColorLed(self.groupBox_2)
        self.led17_3.setObjectName(u"led17_3")
        self.led17_3.setMinimumSize(QSize(30, 30))
        self.led17_3.setMaximumSize(QSize(30, 30))
        self.led17_3.setSizeIncrement(QSize(30, 30))
        self.led17_3.setBaseSize(QSize(30, 30))
        self.led17_3.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.led17_3, 3, 3, 1, 1)

        self.GMtext18_3 = QLabel(self.groupBox_2)
        self.GMtext18_3.setObjectName(u"GMtext18_3")
        self.GMtext18_3.setMaximumSize(QSize(45, 20))
        self.GMtext18_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext18_3, 3, 4, 1, 1)

        self.led18_3 = ColorLed(self.groupBox_2)
        self.led18_3.setObjectName(u"led18_3")
        self.led18_3.setMinimumSize(QSize(30, 30))
        self.led18_3.setMaximumSize(QSize(30, 30))
        self.led18_3.setSizeIncrement(QSize(30, 30))
        self.led18_3.setBaseSize(QSize(30, 30))
        self.led18_3.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.led18_3, 3, 5, 1, 1)

        self.GMtext19_3 = QLabel(self.groupBox_2)
        self.GMtext19_3.setObjectName(u"GMtext19_3")
        self.GMtext19_3.setMaximumSize(QSize(45, 20))
        self.GMtext19_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext19_3, 3, 6, 1, 1)

        self.led19_3 = ColorLed(self.groupBox_2)
        self.led19_3.setObjectName(u"led19_3")
        self.led19_3.setMinimumSize(QSize(30, 30))
        self.led19_3.setMaximumSize(QSize(30, 30))
        self.led19_3.setSizeIncrement(QSize(30, 30))
        self.led19_3.setBaseSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.led19_3, 3, 7, 1, 1)

        self.GMtext20_3 = QLabel(self.groupBox_2)
        self.GMtext20_3.setObjectName(u"GMtext20_3")
        self.GMtext20_3.setMaximumSize(QSize(45, 20))
        self.GMtext20_3.setFont(font8)

        self.gridLayout_3.addWidget(self.GMtext20_3, 3, 8, 1, 1)

        self.led20_3 = ColorLed(self.groupBox_2)
        self.led20_3.setObjectName(u"led20_3")
        self.led20_3.setMinimumSize(QSize(30, 30))
        self.led20_3.setMaximumSize(QSize(30, 30))
        self.led20_3.setSizeIncrement(QSize(30, 30))
        self.led20_3.setBaseSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.led20_3, 3, 9, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_2)


        self.horizontalLayout_4.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 24))
        self.menubar.setMaximumSize(QSize(16777215, 40))
        font9 = QFont()
        font9.setPointSize(10)
        self.menubar.setFont(font9)
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"mode", None))
        self.pushAmplitude.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0430\u043c\u043f\u043b\u0438\u0442\u0443\u0434\u0443", None))
        self.time_data.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u044b \u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.Reset_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0438\u0439 \u0441\u0431\u0440\u043e\u0441", None))
        self.SPI_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 SPI", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0430, \u043d\u0441", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Time1, \u043d\u0441", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Time2, \u043d\u0441", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Time3 \u043d\u0441", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Time4, \u043d\u0441", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Time5, \u043d\u0441", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Time6, \u043d\u0441", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Time7, \u043d\u0441", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Time8, \u043d\u0441", None))
        self.time_period_button.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0443 \u043f\u043e\u043b\u0443\u043f\u0435\u0440\u0438\u043e\u0434\u0430", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u0433\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440\u043e\u0432 \u043c\u043e\u0441\u0442\u043e\u0432\u044b\u0445", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0412\u0418 1", None))
        self.groupBox_3.setTitle("")
        self.GMtext1.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c1", None))
        self.GMtext2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c2", None))
        self.GMtext3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c3", None))
        self.GMtext4.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c4", None))
        self.GMtext5.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c5", None))
        self.GMtext6.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c6", None))
        self.GMtext7.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c7", None))
        self.GMtext8.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c8", None))
        self.GMtext9.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c9", None))
        self.GMtext10.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c10", None))
        self.GMtext11.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c11", None))
        self.GMtext12.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c12", None))
        self.GMtext13.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c13", None))
        self.GMtext14.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c14", None))
        self.GMtext15.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c15", None))
        self.GMtext16.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c16", None))
        self.GMtext17.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c17", None))
        self.GMtext18.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c18", None))
        self.GMtext19.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c19", None))
        self.GMtext20.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c20", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0412\u0418 2", None))
        self.groupBox.setTitle("")
        self.GMtext8_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c8", None))
        self.GMtext6_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c6", None))
        self.GMtext13_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c13", None))
        self.GMtext1_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c1", None))
        self.GMtext7_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c7", None))
        self.GMtext4_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c4", None))
        self.GMtext20_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c20", None))
        self.GMtext5_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c5", None))
        self.GMtext10_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c10", None))
        self.GMtext3_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c3", None))
        self.GMtext9_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c9", None))
        self.GMtext2_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c2", None))
        self.GMtext11_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c11", None))
        self.GMtext14_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c14", None))
        self.GMtext15_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c15", None))
        self.GMtext18_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c18", None))
        self.GMtext17_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c17", None))
        self.GMtext16_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c16", None))
        self.GMtext19_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c19", None))
        self.GMtext12_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c12", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0412\u0418 3", None))
        self.groupBox_2.setTitle("")
        self.GMtext1_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c1", None))
        self.GMtext2_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c2", None))
        self.GMtext3_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c3", None))
        self.GMtext4_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c4", None))
        self.GMtext5_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c5", None))
        self.GMtext6_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c6", None))
        self.GMtext7_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c7", None))
        self.GMtext8_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c8", None))
        self.GMtext9_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c9", None))
        self.GMtext10_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c10", None))
        self.GMtext11_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c11", None))
        self.GMtext12_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c12", None))
        self.GMtext13_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c13", None))
        self.GMtext14_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c14", None))
        self.GMtext15_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c15", None))
        self.GMtext16_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c16", None))
        self.GMtext17_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c17", None))
        self.GMtext18_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c18", None))
        self.GMtext19_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c19", None))
        self.GMtext20_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041c20", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

