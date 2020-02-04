### 模拟QQ
# 学生狗一只，最近其他项目碰上了瓶颈，无聊做做python的可视化，选用了PyQt5库，先做个模拟QQ软件练练手
# 暂时只有登录页面
# ./dist/loginCode/loginCode.exe在win10上面如果有python环境应该能打开



打包 pyinstaller -D -w xxx.py, 如果用这个打包的话要把./ui, ./config, ./users, ./util四个目录拷到打包后的./dist/xxx目录下, 不然跑不起来

