# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(395, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.output_label = QtWidgets.QLabel(Dialog)
        self.output_label.setObjectName("output_label")
        self.gridLayout.addWidget(self.output_label, 2, 0, 1, 1)
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setObjectName("ok_btn")
        self.gridLayout.addWidget(self.ok_btn, 0, 2, 1, 1)
        self.input_text = QtWidgets.QLineEdit(Dialog)
        self.input_text.setObjectName("input_text")
        self.gridLayout.addWidget(self.input_text, 0, 1, 1, 1)
        self.input_label = QtWidgets.QLabel(Dialog)
        self.input_label.setObjectName("input_label")
        self.gridLayout.addWidget(self.input_label, 0, 0, 1, 1)
        self.output_text = QtWidgets.QTextBrowser(Dialog)
        self.output_text.setObjectName("output_text")
        self.gridLayout.addWidget(self.output_text, 2, 1, 1, 2)
        self.cancel_btn = QtWidgets.QPushButton(Dialog)
        self.cancel_btn.setObjectName("cancel_btn")
        self.gridLayout.addWidget(self.cancel_btn, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        self.cancel_btn.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.output_label.setText(_translate("Dialog", "Output :"))
        self.ok_btn.setText(_translate("Dialog", "OK"))
        self.input_label.setText(_translate("Dialog", "Input :"))
        self.cancel_btn.setText(_translate("Dialog", "Cancel"))
