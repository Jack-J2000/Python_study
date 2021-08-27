#持久化保存：文件
#list ，元组，字典 ---->内存里，不属于持久化保存
#存储数据  D:\测试(test)文件夹\Test1
#用户注册
def login():
    username = input('输入用户名：')
    password = input('输入密码：')
    repassword = input('确认输入密码：')

    if password == repassword:
        #保存信息
        with open(r'D:\测试(test)文件夹\Test1\user.txt','a') as wstream:
            wstream.write('{} {}'.format(username,password))

