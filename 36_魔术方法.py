# 魔术方法  Magic Method :所有以“__”双下划线包起来的方法
'''
__init__：初始化魔术方法
触发时机：初始化对象时触发(不是实例化触发，但是和实例化在一个操作中)
__new__：实例化的魔术方法，开辟内存空间，返回对象实例(空间地址)
触发时机：在实例化时触发
__call__：调用对象方法
触发时机：将对象作为函数调用时触发 (p())时，会默认调用该函数里的内容
__del__：析构魔术方法
触发时机：当对象没有用(没有任何变量引用)的时候触发
'''

#创建对象时，先执行_new_(必须有返回值—地址空间)，再执行_init_(收到_new_的返回值-->self)，
# 最后把self空间地址，给了对象p
class Person:
    def __init__(self, name): #初始化实例
        print('init')
        print(self)
        self.name = name
        print(name)

    def __new__(cls,*args,**kwargs): #创建并返回这个类的实例，必须要有返回值
        print('魔术方法：_new_',args)
        # return super(Person, cls).__new__(cls)  #返回值给了_init_里的self
        space = object.__new__(cls)   #作用同上
        print(space)
        return space

    def __call__(self, name):
        print('魔术方法：__call__')
        print('执行对象传入的参数是：',name)

p = Person('Jack')  # 先触发_new_方法，实例化一个对象；再触发_init_方法
print(type(p))
print(p)

p('jsy')  #把对象当成函数调用

#析构
# （多变量指向同一对象地址空间）
import sys
class Man:
    def __init__(self,name):
        self.name=name

    def __del__(self):
        pass
p = Man('J')
p1 = p
p2 = p
print(p1.name)
print(sys.getrefcount(p))
