# 文件结构

- /SQQ
   - /ui                     // 存放ui源文件和.py文件
   - /util                   // 存放工具函数
   - /config              // 系统配置文件
   - /users               // 用户信息, 是后期服务器承载的信息
      - /all                       // 存放所有用户信息
         - user_list.xml            // 所有账号和密码(后期可能要对密码进行加密)以及自动登录信息
      - /xxx                     // 存放所有本地用户信息
         - personal.ini             // 个人信息
         - friends.ini                // 好友信息

***

***

# 文件格式

## /users

***

### /users/all/user_list.xml

<users>

​	<user>

​		<num>xxx</num>

​		<pwd>xxx</pwd>

​		<remenber_flag>0/1</remenber_flag>

​	</user>

​	<user>

​		<num>xxx</num>

​		<pwd>xxx</pwd>

​		<remenber_flag>0/1</remenber_flag>

​	</user>

​	<auto_log>num</auto_log>

</users>

***

## /users/xxx/personal.ini

[info]

num = xxx						; 账号

name = xxx

level = xxx

exp = xxx

sign = xxx

gender = M/F

birthday = XXXX.XX.XX

email = xxxxxx@xxx.xx

birth_place = xxx

living_place = xxx				; 居住地

reg_day = XXXX.XX.XX	; 注册时间

***

## /users/xxx/friend.json

// 在线功能需等到服务器版本再添加

{

​	"Groups" : [

​		"0" : ["groupName" : "xxx", "allNum" : xxx, "onlinenum" : xxx]     

​		"1" : {

​				"nickName" : "xxx",

​				"account" : "xxxxxxx",

​				"inWhichGroup" : "xxx",

​				"comment" : "xxx",

​				"shield" : T/F

​			}

​		"2" : {

​				"nickName" : "xxx",

​				"account" : "xxxxxxx",

​				"inWhichGroup" : "xxx",

​				"comment" : "xxx",

​				"shield" : T/F

​			}

​	]

}