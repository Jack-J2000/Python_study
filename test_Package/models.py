class Model:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def login(self,username,password):
        if username == self.username and password == self.password:
            print('成功登录！')
        else:
            print('登录失败！')
    def show(self):
        print(self.username,self.password)

import calculate模块  #可以导入非包中的模块