# coding: utf-8
# For regist a account
# Coding time 2020.02.05
# Coding by Westrel

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit
from PyQt5.QtGui import QColor
from ui.reg import Ui_Reg
from util.usersInfo import vali

class regWindow(QtWidgets.QMainWindow, Ui_Reg):
    def __init__(self):
        super(regWindow, self).__init__()
        self.initUi()
        return 


    def initUi(self):
        import sys
        self.setupUi(self)
        self.pwd1_text.setEchoMode(QLineEdit.Password)
        self.pwd2_text.setEchoMode(QLineEdit.Password)

        self.cancel_btn.clicked.connect(sys.exit)
        self.nickName_text.returnPressed.connect(lambda :self.val(self.nickName_text))
        self.pwd1_text.returnPressed.connect(lambda :self.val(self.pwd1_text))
        self.pwd2_text.returnPressed.connect(lambda :self.val(self.pwd2_text))


    def val(self, s):
        # QMessageBox.about(self, "提示", s.text())
        result = (True, "说明框\n昵称只含有汉字、数字、字母、下划线, 不能以下划线开头和结尾, 1-24个字符为限\n密码为6-14位, 由数字、字母和下划线组成, 6-14位\n")
        if s==self.nickName_text:
            result = vali("nick", s.text())
        elif s==self.pwd1_text:
            result = vali("pwd", s.text())
        elif s==self.pwd2_text:
            result = vali("pwd", self.pwd1_text.text())
            if result[0]:
                if s.text()==self.pwd1_text.text():
                    result = (True, "密码验证无误")
                else:
                    result = (False, "两次输入密码不一致")
            else:
                pass
        if result[0]:
            self.comment_text.setTextColor(QColor(0, 0, 0))
            if s==self.nickName_text:
                self.pwd1_text.setFocus()
            elif s==self.pwd1_text:
                self.pwd2_text.setFocus()
            else:
                pass
        else: 
            self.comment_text.setTextColor(QColor(255, 0, 0))
        self.comment_text.setPlainText(result[1])
        return



if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = regWindow()
    ui.show()
    sys.exit(app.exec_())