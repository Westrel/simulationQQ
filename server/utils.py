# coding: utf-8
# Utils on server
# Coding time 2020.02.06
# Coding by Westrel

def getAllUsersNum():
    users_stat_txt = "server/all_users_detail/all/users_stat.txt"
    with open(users_stat_txt, "r") as f:
        f.seek(0)
        allLines = f.readlines()
        for line in allLines:
            li = line.split("=")
            if li[0]=="allUsersNumber":
                return int(li[1])
        return 0


if __name__=="__main__":
    print(getAllUsersNum())

