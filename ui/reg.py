# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Reg(object):
    def setupUi(self, Reg):
        Reg.setObjectName("Reg")
        Reg.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(Reg)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_frame = QtWidgets.QFrame(self.centralwidget)
        self.left_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_frame.setObjectName("left_frame")
        self.nickName_text = QtWidgets.QLineEdit(self.left_frame)
        self.nickName_text.setGeometry(QtCore.QRect(40, 40, 161, 21))
        self.nickName_text.setText("")
        self.nickName_text.setObjectName("nickName_text")
        self.pwd1_text = QtWidgets.QLineEdit(self.left_frame)
        self.pwd1_text.setGeometry(QtCore.QRect(40, 90, 161, 21))
        self.pwd1_text.setText("")
        self.pwd1_text.setObjectName("pwd1_text")
        self.pwd2_text = QtWidgets.QLineEdit(self.left_frame)
        self.pwd2_text.setGeometry(QtCore.QRect(40, 140, 161, 21))
        self.pwd2_text.setText("")
        self.pwd2_text.setObjectName("pwd2_text")
        self.gender = QtWidgets.QGroupBox(self.left_frame)
        self.gender.setGeometry(QtCore.QRect(40, 180, 161, 39))
        self.gender.setTitle("")
        self.gender.setObjectName("gender")
        self.female_rb = QtWidgets.QRadioButton(self.gender)
        self.female_rb.setGeometry(QtCore.QRect(90, 10, 41, 19))
        self.female_rb.setToolTipDuration(2)
        self.female_rb.setObjectName("female_rb")
        self.male_rb = QtWidgets.QRadioButton(self.gender)
        self.male_rb.setGeometry(QtCore.QRect(30, 10, 41, 19))
        self.male_rb.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.male_rb.setToolTipDuration(1)
        self.male_rb.setChecked(True)
        self.male_rb.setObjectName("male_rb")
        self.birthday = QtWidgets.QGroupBox(self.left_frame)
        self.birthday.setGeometry(QtCore.QRect(30, 230, 186, 42))
        self.birthday.setTitle("")
        self.birthday.setObjectName("birthday")
        self.day = QtWidgets.QSpinBox(self.birthday)
        self.day.setGeometry(QtCore.QRect(130, 10, 46, 22))
        self.day.setMinimum(1)
        self.day.setMaximum(31)
        self.day.setObjectName("day")
        self.year = QtWidgets.QSpinBox(self.birthday)
        self.year.setGeometry(QtCore.QRect(10, 10, 71, 22))
        self.year.setMinimum(1900)
        self.year.setMaximum(2020)
        self.year.setObjectName("year")
        self.month = QtWidgets.QSpinBox(self.birthday)
        self.month.setGeometry(QtCore.QRect(80, 10, 46, 22))
        self.month.setMinimum(1)
        self.month.setMaximum(12)
        self.month.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.month.setObjectName("month")
        self.birthPlace_text = QtWidgets.QLineEdit(self.left_frame)
        self.birthPlace_text.setGeometry(QtCore.QRect(40, 280, 161, 51))
        self.birthPlace_text.setText("")
        self.birthPlace_text.setObjectName("birthPlace_text")
        self.livingPlace_text = QtWidgets.QLineEdit(self.left_frame)
        self.livingPlace_text.setGeometry(QtCore.QRect(40, 350, 161, 51))
        self.livingPlace_text.setText("")
        self.livingPlace_text.setObjectName("livingPlace_text")
        self.reg_btn = QtWidgets.QPushButton(self.left_frame)
        self.reg_btn.setGeometry(QtCore.QRect(310, 380, 93, 28))
        self.reg_btn.setObjectName("reg_btn")
        self.cancel_btn = QtWidgets.QPushButton(self.left_frame)
        self.cancel_btn.setGeometry(QtCore.QRect(450, 380, 93, 28))
        self.cancel_btn.setObjectName("cancel_btn")
        self.comment_text = QtWidgets.QTextEdit(self.left_frame)
        self.comment_text.setGeometry(QtCore.QRect(260, 20, 331, 341))
        self.comment_text.setReadOnly(True)
        self.comment_text.setObjectName("comment_text")
        self.horizontalLayout.addWidget(self.left_frame)
        Reg.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Reg)
        self.statusbar.setObjectName("statusbar")
        Reg.setStatusBar(self.statusbar)

        self.retranslateUi(Reg)
        QtCore.QMetaObject.connectSlotsByName(Reg)

    def retranslateUi(self, Reg):
        _translate = QtCore.QCoreApplication.translate
        Reg.setWindowTitle(_translate("Reg", "MainWindow"))
        self.nickName_text.setPlaceholderText(_translate("Reg", "昵称"))
        self.pwd1_text.setPlaceholderText(_translate("Reg", "密码"))
        self.pwd2_text.setPlaceholderText(_translate("Reg", "确认密码"))
        self.female_rb.setText(_translate("Reg", "女"))
        self.male_rb.setText(_translate("Reg", "男"))
        self.day.setSuffix(_translate("Reg", "日"))
        self.year.setSuffix(_translate("Reg", "年"))
        self.month.setSuffix(_translate("Reg", "月"))
        self.birthPlace_text.setPlaceholderText(_translate("Reg", "出生地"))
        self.livingPlace_text.setPlaceholderText(_translate("Reg", "现居地"))
        self.reg_btn.setText(_translate("Reg", "注册"))
        self.cancel_btn.setText(_translate("Reg", "取消"))
        self.comment_text.setHtml(_translate("Reg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">说明框</br>昵称只含有汉字、数字、字母、下划线, 不能以下划线开头和结尾, 1-24个字符为限</br>密码为6-14位, 由数字、字母和下划线组成, 6-14位</br></p></br>"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
