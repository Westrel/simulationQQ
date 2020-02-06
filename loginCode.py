# coding: utf-8
# For log in
# Coding time 2020.02.03
# Coding by Westrel

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLineEdit, QMessageBox
from ui.login import Ui_Login
from util.xmlUtils import saveXML

class loginWindow(QtWidgets.QMainWindow, Ui_Login):
    def __init__(self):
        super(loginWindow, self).__init__()
        self.initUi()
        return 
        

    def initUi(self):
        self.setupUi(self)
        self.pwd_text.setEchoMode(QLineEdit.Password)
        if self.checkAutoLogAndRmb() is not None:
            self.userName_text.setText(self.checkAutoLogAndRmb()[0])
            self.pwd_text.setText(self.checkAutoLogAndRmb()[1])
            self.pwd_text.setFocus()
            self.autoLog_cbx.setCheckState(QtCore.Qt.Checked)
            self.remenber_cbx.setCheckState(QtCore.Qt.Checked)
        else:
            self.userName_text.setFocus()
        self.pwd_text.returnPressed.connect(self.logIn)
        self.userName_text.returnPressed.connect(self.unPressed)
        self.login_btn.clicked.connect(self.logIn)
        self.userName_text.textEdited.connect(lambda : self.pwd_text.setText(""))
        self.autoLog_cbx.stateChanged.connect(self.changeCbxState)
        self.reg_btn.clicked.connect(self.reg)


    def reg(self):
        import regCode
        reg = regCode.regWindow()
        reg.show()
        return

    def changeCbxState(self):
        if self.autoLog_cbx.isChecked():
            self.remenber_cbx.setCheckState(QtCore.Qt.Checked) 
        return 


    def unPressed(self):
        '''
            用来判断在账号输入框按下回车时是否记住密码,
             如果记住密码则填充密码和记住密码复选框,
              并将焦点移到密码框
        '''
        user = self.userName_text.text()
        ret = self.checkAutoLogAndRmb(user)
        # QMessageBox.about(self, "提示", ret[1])
        if ret[1]=="1":
            self.pwd_text.setText(ret[2])
            self.remenber_cbx.setCheckState(QtCore.Qt.Checked)
        else:
            self.remenber_cbx.setCheckState(QtCore.Qt.UnChecked)
            self.autoLog_cbx.setCheckState(QtCore.Qt.UnChecked)
        self.pwd_text.setFocus()
        return


    def logIn(self):
        '''

        '''
        user = self.userName_text.text()
        pwd = self.pwd_text.text()
        autoLog_state = self.autoLog_cbx.isChecked()
        remenber_state = self.remenber_cbx.isChecked()

        logInState = self.checkLogIn(user, pwd)
        QMessageBox.about(self, "提示", logInState[1])
        if not logInState[0]:
            self.pwd_text.setText("")
        else:
            from xml.etree import ElementTree as ET
            users_list = ET.parse("./users/local_user/users_list.xml")
            users = users_list.getroot()
            if autoLog_state:
                users.remove(users.find("auto_log"))
                elem = ET.Element("auto_log")
                elem.text = user
                users.append(elem)
                ET.dump(users)
            else:
                if users.findtext("auto_log")==user:
                    users.remove(users.find("auto_log"))
                    elem = ET.Element("auto_log")
                    elem.text = ""
                    users.append(elem)
                    ET.dump(users)
            if remenber_state:
                for u in users_list.getroot().findall("user"):
                    if u.findtext("num")==user:
                        u.remove(u.find("rmb_flag"))
                        elem = ET.Element("rmb_flag")
                        elem.text = "1"
                        u.append(elem)
                        ET.dump(users)
                        break
            saveXML(users, "./users/local_user/users_list.xml")
        pass # 此处添加跳转代码
        return 


    def checkAutoLogAndRmb(self, num=None):
        '''
        Args:
            num: 可选参数, 账号

        Returns:
                str: 如果未输入num, 则返回自动登录账号
                turple: 如果输入num, 则返回一个元组,
                 记住密码为0则返回(自动登录状态, 记住密码状态)
                 记住密码为1则返回(自动登录状态, 记住密码状态, 密码)
        '''

        from xml.etree import ElementTree as ET
        users_list = ET.parse("./users/local_user/users_list.xml")
        users = users_list.getroot().findall("user")
        auto_log_num = users_list.getroot().findtext("auto_log")
        if num is not None:
            auto_log = 0
            rmb_flag = 0
            if auto_log_num==num:
                auto_log = 1
            else:
                auto_log = 0
            for user in users:
                if user.find("num").text==num:
                    rmb_flag = user.find("rmb_flag").text
                    if rmb_flag == "1":
                        return auto_log, rmb_flag, user.findtext("pwd")
                    else:
                        return auto_log, rmb_flag
        else:
            if auto_log_num is not None:
                for user in users:
                    if user.find("num").text==auto_log_num:
                        return auto_log_num, user.find('pwd').text
            else:
                return None


    def checkLogIn(self, num, pwd):
        '''
            Args:
                num: 账号
                pwd: 密码
            
            Returns:
                bool: 登陆成功或失败
                str: 提示信息
        '''
        if pwd=="":
            return False, "请输入密码"
        from xml.etree import ElementTree as ET
        users_list = ET.parse("./users/local_user/users_list.xml")
        users = users_list.getroot().findall("user")
        for user in users:
            if user.find("num").text==num:
                if user.find("pwd").text==pwd:
                    return True, "登录成功!"
        return False, "请核对账号密码"



if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = loginWindow()
    ui.show()
    sys.exit(app.exec_())