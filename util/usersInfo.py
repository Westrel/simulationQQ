# coding: utf-8
# 操作users目录的函数集合
# Coding time 2020.02.06
# Coding by Westrel

import re

def vali(info, string):
    '''
        验证是否写入内容是否合规
        Args:
            info:为下列参数之一
                "nick" : 用户名
                "pwd"  : 密码
                "date" : 日期
                "email": 邮箱
            string
                info="nick" : str
                info="pwd"  : str
                info="date" : (year, month)
                info="email": str
        Return:
            True, "": 合规
            True, "int": 当月有多少天
            False, str: 不合规及理由
            False, "ERROR": info错误
    '''
    if info=="nick":
        # 昵称只含有汉字、数字、字母、下划线, 不能以下划线开头和结尾, 1-24个字符为限
        p = r"^(?!_)(?!.*?_$)[a-zA-Z0-9_\u4e00-\u9fa5]{1,24}$"
        if re.match(p, string):
            return True, "昵称合规"
        else:
            return False, "昵称只含有汉字、数字、字母、下划线, 不能以下划线开头和结尾, 1-24个字符为限"
    elif info=="pwd":
        # 密码为6-14位, 由数字、字母和下划线组成, 6-14位
        p = r"^[a-zA-Z0-9_]{6,14}$"
        if re.match(p, string):
            return True, "密码合规"
        else:
            return False, "密码为6-14位, 由数字、字母和下划线组成, 6-14位"
    elif info=="date":
        # 返回当月有多少日
        year = int(string[0])
        month = str(string[1])
        day = 31
        if month in ["1", "3", "5", "7", "8", "10", "12"]:
            pass
        elif month in ["4", "6", "9", "11"]:
            day = 30
        elif month=="2":
            day = 28
            isLeapYear = False
            if year%4==0:
                if year%100==0:
                    if year%400==0:
                        isLeapYear = True
                    else:
                        pass
                else:
                    isLeapYear = True
            else:
                pass
            if isLeapYear:
                day = 29
        else:
            return False, "Date Error!"
        return True, day
    elif info=="email":
        # 邮箱形式为name@domin
        p = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$"
        if re.match(p, string):
            return True, "邮箱格式正确"
        else:
            return False, "请按照正确的邮箱格式填写: name@domin"
    else:
        return False, "Error!"
    
    return


if __name__=="__main__":
    print(vali("date", (1900, 2)))
    