'''
类方法：
@classmothod
def test(cls):
    pass

特点：
1.定义需要依赖装饰器@classmothod
2.类方法中只能用类属性，不能用对象属性
3.类方法中不能调用对象方法，对象方法里能调用类方法
4.类方法中参数不是一个对象，而是类

类方法作用：
只能访问类属性和类方法，所以可以在对象创建之前，
如果需要完成一些动作(功能)，可使用类方法
(不依赖对象，独立于对象之外的方法)
'''
class Dog:
    def __init__(self,nickname):
        print('init')
        self.nickname = nickname

    def run(self):  #self  对象   || 对象方法
        print(self)    #打印是对象名和对象空间
        print('{}正在睡觉！'.format(self.nickname))
        Dog.test()   #对象方法里可通过类名或是对象(self)来调用类方法
        self.test()

    def eat(self):
        print('饿了么...')
        self.run()

    @classmethod  #装饰器
    def test(cls):   #cls  class   ||类方法
        print(cls)     #打印是类名
        # print(cls.nickname)   #类空间里没有nickname这个参数

print(Dog)
Dog.test()  #类方法不依赖对象，在对象出现之前也可调用
dog = Dog('旺财')
# dog.run()
dog.test()

# dog.eat()



'''
静态方法：(类似类方法)
1.需要装饰器  @staticmethod
2.静态方法无需传递参数(cls,self)
3.也只能访问类的属性和方法(使用类名来调用，也可以调用私有化)，对象的是无法访问的
4.加载时机同类方法一致

总结：
 类方法  静态方法
 不同：
    1.装饰器不同
    2.类方法有参数，静态方法无参数
相同：
   1.只能访问类的属性和方法，对象无法访问
   2.都可以通过类名调用访问
   3.都可以在创建对象之前使用，因为不依赖对象

普通(对象)方法与两者的区别：
不同：
   1.没有装饰器
   2.普通方法永远依赖对象，因为每个普通方法都有一个self
   3.只有创建了对象才能调用普通方法
'''
class Person:
    __age = 21  #属性私有化，外界无法通过类来访问该属性

    def __init__(self,name):
        self.name = name

    def show(self):
        print('年龄：{}'.format(self.__age))  #此时的__age可以通过(对象方法)self来访问，达到封装数据的目的

    @classmethod
    def update_age(cls):
        cls.__age = 18     #也可以(借助类方法)通过cls来访问
        print("类方法")

    @classmethod
    def show_age(cls):
        print(cls.__age)

    @staticmethod
    def test():  #没有自带参数，里面不能出现self,cls
        print('静态方法')
        print(Person.__age)


p = Person('Jack')
p.update_age()
p.show()
Person.update_age()
Person.show_age()
Person.test()




