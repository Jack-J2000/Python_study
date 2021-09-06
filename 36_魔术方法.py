# 魔术方法  Magic Method :所有以“__”双下划线包起来的方法，满足一定条件下自动执行
'''
__init__：初始化魔术方法
触发时机：初始化对象时触发(不是实例化触发，但是和实例化在一个操作中)
__new__：实例化的魔术方法，开辟内存空间，返回对象实例(空间地址)
触发时机：在实例化时触发
__call__：调用对象方法
触发时机：将对象作为函数调用时触发 (p())时，会默认调用该函数里的内容

__del__：析构魔术方法；垃圾回收机制，
触发时机：当对象没有用(没有任何变量引用)的时候触发

__str__：必须要有返回值(return)，将返回值传给对象
触发时机：打印对象名 自动触发去调用__str__
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

#析构 __del__
# （多变量指向同一对象地址空间） 类似 del
'''
1.对象赋值
    p = Person()
    p1 = p    #p和p1共同指向同一个地址
2.删除地址的引用
    del p1 删除p1对地址的引用
3.查看对象的引用次数
    import sys
    sys.getrefcount(p)
4. 当一块空间没有了任何的引用，默认执行__del__
    (Python自带垃圾回收机制，每执行完程序自动释放资源，
    故在程序结束后会执行__del__)
      
'''
import sys
class Man:
    def __init__(self,name):
        self.name=name

    def __del__(self): #在删除完引用之后，并执行剩余代码后，才去执行_del_
        print('魔术方法：del')
p = Man('J')
p1 = p
p2 = p
print(p,p1)
print(p1.name)
print(sys.getrefcount(p1))

p1.name = 'Tom'
print(p1.name,p.name)  #修改其中一个的值，其他指向该地址的变量也随之而变

print(p2)
del p2  #在删除引用时会调用魔术方法__init__
print('删除p2后打印：',p1.name)

#__str__
'''
对于开发者来说，单纯的打印对象名，结果是地址空间(无太大意义)
所以使用__str__来给对象传入有用的信息
'''
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return '姓名：'+self.name+'年龄：'+self.age  #将返回值给对象

p = Human('JSY','22')  #此时的对象p值为__str__的返回值
print(p)



'''
重点：
__init__(构造方法)
__str__ 
了解：
__new__  开辟空间
__del__  无指针引用时调用
__call__  将对象当作函数用

方法：
普通(对象)方法：调用时 对象.方法() 
方法之间的调用：
             class A:
               def a(self):
                  pass
               def b(self):
                  #在b方法里调用a方法
                  self.a()

类方法：        调用时 类名.方法()
                          对象.方法()

静态方法：      调用时 类名.方法()
                          对象.方法()
'''