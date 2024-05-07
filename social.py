# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'social_new.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(549, 366)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 71, 31))
        self.label_5.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font: 11pt \"Open Sans\";\n"
"background-color: none;\n"
"border: none;")
        self.secondName_data = QLineEdit(Dialog)
        self.secondName_data.setObjectName(u"secondName_data")
        self.secondName_data.setGeometry(QRect(10, 40, 241, 31))
        self.secondName_data.setStyleSheet(u"QLineEdit{\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 80, 71, 31))
        self.label_6.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font: 11pt \"Open Sans\";\n"
"background-color: none;\n"
"border: none;")
        self.firstName_data = QLineEdit(Dialog)
        self.firstName_data.setObjectName(u"firstName_data")
        self.firstName_data.setGeometry(QRect(10, 110, 241, 31))
        self.firstName_data.setStyleSheet(u"QLineEdit{\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.middleName_data = QLineEdit(Dialog)
        self.middleName_data.setObjectName(u"middleName_data")
        self.middleName_data.setGeometry(QRect(10, 180, 241, 31))
        self.middleName_data.setStyleSheet(u"QLineEdit{\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 150, 71, 31))
        self.label_7.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font: 11pt \"Open Sans\";\n"
"background-color: none;\n"
"border: none;")
        self.course_data = QLineEdit(Dialog)
        self.course_data.setObjectName(u"course_data")
        self.course_data.setGeometry(QRect(310, 40, 91, 31))
        self.course_data.setStyleSheet(u"QLineEdit{\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(310, 10, 71, 31))
        self.label_8.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font: 11pt \"Open Sans\";\n"
"background-color: none;\n"
"border: none;")
        self.group_data = QLineEdit(Dialog)
        self.group_data.setObjectName(u"group_data")
        self.group_data.setGeometry(QRect(430, 40, 101, 31))
        self.group_data.setStyleSheet(u"QLineEdit{\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(430, 10, 101, 31))
        self.label_9.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font: 11pt \"Open Sans\";\n"
"background-color: none;\n"
"border: none;")
        self.certNum_data = QLineEdit(Dialog)
        self.certNum_data.setObjectName(u"certNum_data")
        self.certNum_data.setGeometry(QRect(310, 110, 221, 31))
        self.certNum_data.setStyleSheet(u"QLineEdit{\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(310, 80, 111, 31))
        self.label_10.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font: 11pt \"Open Sans\";\n"
"background-color: none;\n"
"border: none;")
        self.certDate_data = QLineEdit(Dialog)
        self.certDate_data.setObjectName(u"certDate_data")
        self.certDate_data.setGeometry(QRect(310, 180, 221, 31))
        self.certDate_data.setStyleSheet(u"QLineEdit{\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(310, 150, 111, 31))
        self.label_11.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font: 11pt \"Open Sans\";\n"
"background-color: none;\n"
"border: none;")
        self.curDate_data = QLineEdit(Dialog)
        self.curDate_data.setObjectName(u"curDate_data")
        self.curDate_data.setGeometry(QRect(10, 250, 241, 31))
        self.curDate_data.setStyleSheet(u"QLineEdit{\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 220, 181, 31))
        self.label_12.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font: 11pt \"Open Sans\";\n"
"background-color: none;\n"
"border: none;")
        self.saveData_btn = QPushButton(Dialog)
        self.saveData_btn.setObjectName(u"saveData_btn")
        self.saveData_btn.setGeometry(QRect(10, 300, 241, 41))
        self.saveData_btn.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u041a\u0443\u0440\u0441", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u043c\u0435\u0440 \u0433\u0440\u0443\u043f\u043f\u044b", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u043c\u0435\u0440 \u0441\u043f\u0440\u0430\u0432\u043a\u0438", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u043a\u0430\u0437\u0430", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u0434\u043f\u0438\u0441\u0438 \u0437\u0430\u044f\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.saveData_btn.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
    # retranslateUi

