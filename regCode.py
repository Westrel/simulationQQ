# coding: utf-8
# For regist a account
# Coding time 2020.02.06
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
        self.year.setValue(2000)

        self.cancel_btn.clicked.connect(sys.exit)
        self.nickName_text.returnPressed.connect(lambda :self.val(self.nickName_text))
        self.pwd1_text.returnPressed.connect(lambda :self.val(self.pwd1_text))
        self.pwd2_text.returnPressed.connect(lambda :self.val(self.pwd2_text))
        self.male_rb.clicked.connect(self.year.setFocus)
        self.female_rb.clicked.connect(self.year.setFocus)
        self.email_text.returnPressed.connect(lambda :self.val(self.email_text))
        self.birthPlace_text.returnPressed.connect(lambda :self.val(self.birthPlace_text))
        self.livingPlace_text.returnPressed.connect(self.reg_btn.setFocus)
        self.year.editingFinished.connect(self.month.setFocus)
        self.month.editingFinished.connect(self.day.setFocus)
        self.day.editingFinished.connect(self.email_text.setFocus)
        self.year.valueChanged.connect(lambda :self.val("date"))
        self.month.valueChanged.connect(lambda :self.val("date"))
        # self.email_text.editingFinished.connect(lambda :self.val(self.email_text))
        self.reg_btn.clicked.connect(self.reg)


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
        elif s=="date":
            dayMax = vali("date", (self.year.value(), self.month.value()))
            if dayMax[0]:
                self.day.setMaximum(int(dayMax[1]))
                result = True, "时间校验无误"
            else:
                result = False, "请核查时间!"
        elif s==self.email_text:
            result = vali("email", self.email_text.text())
        else:
            result = True, ""
        if result[0]:
            self.comment_text.setTextColor(QColor(0, 0, 0))
            if s==self.nickName_text:
                self.pwd1_text.setFocus()
            elif s==self.pwd1_text:
                self.pwd2_text.setFocus()
            elif s==self.pwd2_text:
                self.year.setFocus()
            elif s==self.email_text:
                self.birthPlace_text.setFocus()
            elif s==self.birthPlace_text:
                self.livingPlace_text.setFocus()
            else:
                pass
        else: 
            self.comment_text.setTextColor(QColor(255, 0, 0))
        self.comment_text.setPlainText(result[1])
        return result


    def reg(self):
        mes = "注册提示\n"
        if not self.val(self.nickName_text)[0]:
            self.nickName_text.setFocus()
            mes += self.val(self.nickName_text)[1]
        elif not self.val(self.pwd1_text)[0]:
            self.pwd1_text.setFocus()
            mes += self.val(self.pwd1_text)[1]
        elif not self.val(self.pwd2_text)[0]:
            self.pwd2_text.setFocus()
            mes += self.val(self.pwd2_text)[1]
        elif not self.val(self.email_text)[0]:
            self.email_text.setFocus()
            mes += self.val(self.email_text)[1]
        else:
            gender = "male"
            if self.female_rb.isChecked():
                gender = "female"
            apply = {"nick": self.nickName_text.text(),
            "pwd": self.pwd1_text.text(),
            "gender": gender,
            "birthday": ""+self.year.value()+"."+self.month.value()+"."+self.day.value(),
            "email": self.email_text.text(),
            "birthplace": self.birthPlace_text.text(),
            "livingplace": self.livingPlace_text.text()
            }
            QMessageBox.about(self, "提示", "注册成功!")
            # pass
        self.comment_text.setTextColor(QColor(255, 0, 0))
        self.comment_text.setPlainText(mes)
        return 

    
    def writeIntoFile(self):

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = regWindow()
    ui.show()
    sys.exit(app.exec_())
    