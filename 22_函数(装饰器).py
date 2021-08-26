'''
装饰器：web里运用，面试会问
遵循 ’开发封闭‘ 原则： 对以实现功能代码块封闭
                                          对扩展开放

定义：
def  aaa(func):
      def  xxx(*args,**kwargs):
           ......
           func()
           ......
           return   yyy
      return  xxx
装饰：
@装饰器名   ---->  原函数 = 装饰(原函数)
def  原函数():
      pass
'''


# 前言函数
# def foo():
#     print('foo')
#
# def func():
#     print('func')
#
# foo = func #函数地址的改变
# foo()  #foo的地址指向为func，地址的改变


# 定义装饰器
def decorater(func):  # 必须有参数
    def wrapper():
        # func()  #调用func函数，该函数为house
        print('刷漆')
        print('装修房子')

    print('------------------>')
    wrapper()
    return wrapper  # 不加括号为返回函数的地址


# 使用装饰器
@decorater  # @decorater的底层动作： 变相执行装饰器decorater(house)     把该标识下面的函数house作为参数，接受装饰器的返回值
# 等价于 house = decorater (house)
def house():
    print('毛坯房...')


house()  # 此时house地址为wrapper的地址

'''
不改变原函数的前提下增加函数的功能。
装饰器功能：
1.引入日志
2.函数执行时间统计
3.执行函数前预备处理
4.执行函数后清理功能
5.权限校验等场景
6.缓存

带参数的装饰器
如果原函数有参数，则装饰器的内部函数也要有参数，两者参数名可不同；
当原函数传入多个参数时，在装饰器内部函数使用*args 
万能
'''


# 带参数的装饰器
def decorater(func):
    def weapper(*args, **kwargs):  # 此时为万能装饰器
        #  args 是一个元组  ('北京五环',1000)
        func(*args, **kwargs)  # 利用了  *  拆包
        print('刷漆')
        print('装修房子')

    return weapper


@decorater
def house(address):
    print('房子的地址是：{}，是一个毛坯房......'.format(address))


@decorater
def workspace(address, area, name):
    print('车间在{}，有{}平米,房主：{}'.format(address, area, name))


house('魏都大厦')  # house就是wrapper
workspace('北京五环', 1000, name='jsy')

'''
带返回值的装饰器：

'''


def decorater(func):
    def wrapper(*args, **kwargs):
        print('===========================')
        r = func(*args, **kwargs)  #执行people()，打印内容，返回值 785 给 r
        print('我是钢铁侠')
        return r

    return wrapper


@decorater
def people():
    print('I am IronMan...')
    return 785


r = people()  # 把people返回值赋给r，就是把wrapper返回值赋给r，此时要执行wrapper代码；由于wrapper里使用了func()，所以才会执行people里面的代码
print(r)

'''
如果装饰器是多层的，谁距离函数最近就优先使用哪个装饰器

'''


# 多层装饰器
def decorater1(func):
    print('第一个装饰器')

    def wrapper(*args, **kwargs):
        func()
        print('第一个wrapper')

    return wrapper


def decorater2(func):
    print('第二个装饰器')

    def wrapper(*args, **kwargs):
        func()
        print('第二个wrapper')

    return wrapper


@decorater1
@decorater2  # 执行装饰器内容时，按照就近原则，先执行离jsy()近的decorater2
def jsy():
    print('Hello World !')


jsy()


'''
带参数的装饰器是三层的
最外面的函数负责接收装饰器的参数
里面的内容还是原装饰器内容
'''
# 装饰器带参数
def outer(a):                        #第一层：负责接收装饰器参数
    def decorater(func):          #第二层：负责接收函数
        def wrapper(*args, **kwargs):     #第三层：负责接收函数参数
            func(*args, **kwargs)
            print('今年{}岁'.format(a))

        return wrapper
    return decorater  #注意装饰器的返回

@outer(a=10)
def house(name):
    print('我的名字是{}'.format(name))

house('jsy')