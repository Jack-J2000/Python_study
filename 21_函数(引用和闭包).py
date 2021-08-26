'''
函数注释：在函数体里的注释（源码里的函数便是如此）
def  函数名(参数1,...)
        基本注释   "注释内容"
        高级注释
        " " "
            函数的说明：

            参数说明：
             :param username:
             :param password:
            返回值说明：
             :return:
        " " "
'''


def login(username, password):  # 在函数里加 ''' 可显示函数注释并添加相应注释
    '''
    用户登录
    :param username:   用户名
    :param password:   用户登录密码
    :return:          是否登录成功
    '''
    if username == 'jsy' and password == '123':
        print('登录成功！')
        return True
    else:
        return False


login('jsy', '123')

'''
引用：
sys.getrefcount() 获取一块空间地址引用次数
                    当调取该函数时，即引用次数+1
                    del 表示删除了一个引用
函数参数引用：
                   函数参数是传递引用，也就是数据的内存地址
                   必须要分清除传递的值是可变类型还是不可变类型
                   可变：函数里面改变，外层也会改变
                   不可变：函数里面改变，外面不变
'''
import sys

a = 1
b = a  # 将a的引用地址赋给b
print(id(a))
print(id(b))

print(sys.getrefcount(a))

list1 = [1, 2, 3, 4, 5, 6]
list2 = list1
list3 = list1
print(sys.getrefcount(list1))
del list3  # 删去list3时，引用次数为3
print(sys.getrefcount(list1))


#
def test(n1):
    for i in range(n1):
        print(i)
    n1 += 1  # 不可变类型，不能修改外部的n


n = 9
test(n)
print(n)

list1 = [1, 2, 3]


def test1(l):
    if isinstance(l, list):
        for i in l:
            print('---->', i)
        l.insert(0, 8)  # 由于list是可变类型，地址相通
    else:
        print('不是列表类型！')


test1(list1)  # 把list地址给l

'''
嵌套：
nonlocal   在闭包内修改或使用外部函数变量
global     修改或使用全局变量
闭包(closure)：
1.嵌套函数
2.内部函数引用了外部函数的变量
3.返回值是内部函数
闭包是由函数及其相关的引用环境组合而成的实体：（即 闭包= 函数快+引用环境）。
如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包
'''


# 检索顺序：内层函数---->外层函数----->全局----->系统 builtins
def outer():
    a = 100  # 变量

    def inner():  # 变量
        b = 200
        # b += a  #内部函数可以使用外部函数的变量
        nonlocal a   #内部函数引用了外部函数的变量
        a += b  # 内部函数不能修改外部函数变量，想要修改需要加关键字nonlocal
        print('我是内部函数inner', b)

    result = locals()  # locals()表示查看函数中的局部变量
    print(result)
    print(a)
    inner()
    print(a)  # 调用inner后，a的值发生改变


outer()


#    闭包举例   以下情况称作闭包
def outer(n):
    a = 10

    def inner():
        b = a + n
        print('内部函数：', b)

    return inner

r = outer(5)  #r接住了inner的地址
print(r)
r()    #相当于执行inner