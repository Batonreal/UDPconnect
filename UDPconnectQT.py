# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UDPconnectQT.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(460, 371)
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ipConfig = QLineEdit(Dialog)
        self.ipConfig.setObjectName(u"ipConfig")
        font1 = QFont()
        font1.setPointSize(11)
        self.ipConfig.setFont(font1)

        self.horizontalLayout_2.addWidget(self.ipConfig)

        self.portConfig = QLineEdit(Dialog)
        self.portConfig.setObjectName(u"portConfig")
        self.portConfig.setFont(font1)

        self.horizontalLayout_2.addWidget(self.portConfig)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(12, 0, -1, -1)
        self.ipInfo = QLabel(Dialog)
        self.ipInfo.setObjectName(u"ipInfo")
        self.ipInfo.setMinimumSize(QSize(0, 0))
        self.ipInfo.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_3.addWidget(self.ipInfo)

        self.portInfo = QLabel(Dialog)
        self.portInfo.setObjectName(u"portInfo")
        self.portInfo.setMinimumSize(QSize(0, 0))
        self.portInfo.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_3.addWidget(self.portInfo)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.textMessage = QLineEdit(Dialog)
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

        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.verticalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_2 = QPushButton(Dialog)
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

        self.pushButton = QPushButton(Dialog)
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


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"UDPconnect", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 ip \u0430\u0434\u0440\u0435\u0441", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u043e\u0440\u0442", None))
        self.ipConfig.setText(QCoreApplication.translate("Dialog", u"192.168.0.15", None))
        self.portConfig.setText(QCoreApplication.translate("Dialog", u"6868", None))
        self.ipInfo.setText(QCoreApplication.translate("Dialog", u"\u0412\u0430\u0448 ip:", None))
        self.portInfo.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u044b\u0439 \u043f\u043e\u0440\u0442:", None))
        self.textMessage.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0431\u0430\u0439\u0442\u044b", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
    # retranslateUi

