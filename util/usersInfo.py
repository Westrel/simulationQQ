# coding: utf-8
# 操作users目录的函数集合
# Coding time 2020.02.05
# Coding by Westrel

import re

def vali(info, string):
    '''
        验证是否写入内容是否合规
        Args:
            info:为下列参数之一
                "nick" : 用户名
                "pwd"  : 密码
            string
        Return:
            True, "": 合规
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
    else:
        return False, "Error!"
    
    return 