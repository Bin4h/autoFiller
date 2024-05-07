# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_new.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(566, 237)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.newStudent_btn = QPushButton(self.centralwidget)
        self.newStudent_btn.setObjectName(u"newStudent_btn")
        self.newStudent_btn.setGeometry(QRect(30, 30, 181, 51))
        self.newStudent_btn.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 11pt \"Open Sans\";\n"
"border-radius: 5px;\n"
"background-color: #006D4C;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #207E62;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #00A876;\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 30, 231, 21))
        self.label.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font: 11pt \"Open Sans\";\n"
"background-color: none;\n"
"border: none;")
        self.chooseStudent_combobox = QComboBox(self.centralwidget)
        self.chooseStudent_combobox.setObjectName(u"chooseStudent_combobox")
        self.chooseStudent_combobox.setGeometry(QRect(320, 70, 201, 31))
        self.chooseStudent_combobox.setStyleSheet(u"diplay: none;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 130, 231, 21))
        self.label_2.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font: 11pt \"Open Sans\";\n"
"background-color: none;\n"
"border: none;")
        self.chooseForm_combobox = QComboBox(self.centralwidget)
        self.chooseForm_combobox.addItem("")
        self.chooseForm_combobox.setObjectName(u"chooseForm_combobox")
        self.chooseForm_combobox.setGeometry(QRect(320, 170, 201, 31))
        self.savePDF_btn = QPushButton(self.centralwidget)
        self.savePDF_btn.setObjectName(u"savePDF_btn")
        self.savePDF_btn.setGeometry(QRect(30, 90, 181, 51))
        self.savePDF_btn.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 11pt \"Open Sans\";\n"
"border-radius: 5px;\n"
"background-color: #006D4C;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #207E62;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #00A876;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.newStudent_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0444\u043e\u0440\u043c\u044b", None))
        self.chooseForm_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0435 \u0441\u043e\u0446. \u0441\u0442\u0438\u043f\u0435\u043d\u0434\u0438\u0438", None))

        self.savePDF_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0444\u043e\u0440\u043c\u0443", None))
    # retranslateUi

