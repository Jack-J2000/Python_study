'''
开发：登录验证

'''
import time

islogin = False

#定义一个登录函数
def login():
    username = input('请输入用户名：')
    password = input('输入密码：')
    if username == 'jsy' and password=='123':
        return True
    else:
        return False


#定义装饰器，验证是否付款
def login_required(func):
    def wrapper(*args,**kwargs):
        #验证用户是否登录
        global islogin
        if islogin:
            func(*args,**kwargs)
        else:
            #跳转到登录页面
            print('用户没有登录！')
            islogin = login() #调用登录函数
            print('result',islogin)

    return wrapper

@login_required
def pay(money):
    print('付款金额{}，正在付款...'.format(money))
    time.sleep(2)
    print('付款成功！')


pay()  #由于默认没有登录，第一次执行函数是先登录
pay(200)  #第二次执行函数时，登录状态改为登录