# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(651, 404)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setMinimumSize(QtCore.QSize(651, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.inter_frame = QtWidgets.QFrame(self.centralwidget)
        self.inter_frame.setGeometry(QtCore.QRect(160, 120, 296, 188))
        self.inter_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inter_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inter_frame.setObjectName("inter_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.inter_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.options_frame = QtWidgets.QFrame(self.inter_frame)
        self.options_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.options_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.options_frame.setObjectName("options_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.options_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.autoLog_cbx = QtWidgets.QCheckBox(self.options_frame)
        self.autoLog_cbx.setObjectName("autoLog_cbx")
        self.gridLayout_2.addWidget(self.autoLog_cbx, 0, 0, 1, 1)
        self.findpwd_label = QtWidgets.QLabel(self.options_frame)
        self.findpwd_label.setObjectName("findpwd_label")
        self.gridLayout_2.addWidget(self.findpwd_label, 0, 2, 1, 1)
        self.remenber_cbx = QtWidgets.QCheckBox(self.options_frame)
        self.remenber_cbx.setObjectName("remenber_cbx")
        self.gridLayout_2.addWidget(self.remenber_cbx, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.options_frame, 1, 0, 1, 2)
        self.reg_btn = QtWidgets.QLabel(self.inter_frame)
        self.reg_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.reg_btn.setMouseTracking(True)
        self.reg_btn.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.reg_btn.setScaledContents(False)
        self.reg_btn.setObjectName("reg_btn")
        self.gridLayout_3.addWidget(self.reg_btn, 6, 0, 1, 1)
        self.login_btn = QtWidgets.QPushButton(self.inter_frame)
        self.login_btn.setObjectName("login_btn")
        self.gridLayout_3.addWidget(self.login_btn, 6, 1, 1, 1)
        self.input_frame = QtWidgets.QFrame(self.inter_frame)
        self.input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame.setObjectName("input_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.input_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.userName_label = QtWidgets.QLabel(self.input_frame)
        self.userName_label.setObjectName("userName_label")
        self.gridLayout.addWidget(self.userName_label, 0, 0, 1, 1)
        self.userName_text = QtWidgets.QLineEdit(self.input_frame)
        self.userName_text.setObjectName("userName_text")
        self.gridLayout.addWidget(self.userName_text, 0, 2, 1, 1)
        self.pwd_label = QtWidgets.QLabel(self.input_frame)
        self.pwd_label.setObjectName("pwd_label")
        self.gridLayout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.pwd_text = QtWidgets.QLineEdit(self.input_frame)
        self.pwd_text.setObjectName("pwd_text")
        self.gridLayout.addWidget(self.pwd_text, 1, 2, 1, 1)
        self.gridLayout_3.addWidget(self.input_frame, 0, 0, 1, 2)
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.autoLog_cbx.setText(_translate("Login", "自动登录"))
        self.findpwd_label.setText(_translate("Login", "找回密码"))
        self.remenber_cbx.setText(_translate("Login", "记住密码"))
        self.reg_btn.setText(_translate("Login", "注册账号"))
        self.login_btn.setText(_translate("Login", "登录"))
        self.userName_label.setText(_translate("Login", "账  号:"))
        self.pwd_label.setText(_translate("Login", "密  码:"))
