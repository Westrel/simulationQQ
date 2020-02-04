def checkAutoLogAndRmb(num=None):
    '''
        Args:
            num: 账号, 如果未提供则返回值为自动登录开启的账号和密码

        Returns:
            turple: 分别表示自动登录状态和记住密码状态, 0表示关, 1表示开
    '''

    from xml.etree import ElementTree as ET
    users_list = ET.parse("./users/all/users_list.xml")
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

a = [0, 0, 0]
b = [0, 0]
a = list(checkAutoLogAndRmb("000001"))
# a[1], b[1] = checkAutoLogAndRmb("000002")
print(a)
# print(b)
# checkAutoLogAndRmb()