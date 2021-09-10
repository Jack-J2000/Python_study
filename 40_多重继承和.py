class Person:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print('--->eat')

    def eat(self,food):    #同名的eat方法，会覆盖掉上面的(旧的)eat方法
        print('___>eat:',food)

p = Person('Jack')
p.eat('大碗菜')

'''
python允许多重继承：一个子类可以有多个父类(java不可以)  #开发中很少使用
    def 子类(父类1，父类2...)
        pass
多重继承的搜索顺序： 在Python2中，对于经典类(python2)和新式类(python3)有所不同
经典类：   #python2中是从左至右，深度优先
class Base:
    pass

class A(Base):
    pass
class B(Base):
    pass

新式类：
class Base(object): #区别在此，python2中是广度优先
    pass

class A(Base):
    pass
class B(Base):
    pass
    
注意：在python3里，无论经典类还是新式类都是广度优先
'''
#C继承了A和B，而A和B继承了Base
#Base-->A,B-->C
class Base:
    def test(self):
        print('--->Base')


class A(Base):
    def test1(self):
        print('--->A')

class B(Base):
    def test2(self):
        print('--->B')

class C(A,B):   #同时继承多个父类
    def test(self):
        print('--->C')

import inspect
print(inspect.getmro(C))  #显示的可理解为搜索顺序
print(C.__mro__)          #同上

c = C()
c.test1()  #可以使用多个父类提供的方法
c.test2()
# c.test3()
c.test()  #出现与父类同名方法时，搜索顺序为就近原则
