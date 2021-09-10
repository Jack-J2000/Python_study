# 继承  is a ，has a
'''
'''
import random


# 声明（Road）
class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


# 声明（Car）
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):  # 需注意：road与r指向同一地址空间
        ran_time = random.randint(1, 10)
        message = '{}品牌的车在{}上以{}速度行驶{}小时'.format(self.brand, road.name, self.speed, ran_time)
        print(message)

    def __str__(self):
        return '{}品牌，速度：{}'.format(self.brand, self.speed)


# 创建实例化对象
r = Road('魏州大道', 6666)

c = Car('凯迪拉克', 66)
print(c)

c.get_time(r)

'''
# 类与类之间的关系：
# has a
# is a

知识点：
1.has  a
   一个类中使用了另外一种自定义的类型(类似于包含关系)
2.类型：

   系统类型：
      str  int  float
      list  dict  tuple  set
   自定义类型：
      自定义的类，都可以将其当成一种类型
      s = Student()  #  s是对象类型(自定义类型)
      print(s)   
'''


class Computer:
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def online(self):
        print('正在玩LOL中！')

    def __str__(self):
        return self.brand + '---' + self.type + '---' + self.color


class Book:
    def __init__(self, book_name, author, number):
        self.book_name = book_name
        self.author = author
        self.number = number

    def __str__(self):
        return self.book_name + '---' + self.author + '---' + str(self.number)


class Student:
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        self.books = []
        self.books.append(book)

    def borrow_book(self, input_book):
        # print('书籍信息：')
        # print(book)  #相当与调用对象名book1
        for book in self.books:
            if book.book_name == input_book.book_name:
                print('已经借过此书！')
                break
            else:
                self.books.append(input_book)
                print('借书成功！')
                break
        print(self.books)

    def show_book(self):
        for book in self.books:
            print(book.book_name)

    def __str__(self):
        return self.name + '---' + str(self.computer) + '---' + str(self.books)  # 不能返回一个对象


# 创建对象
computer = Computer('hp', 'pro++', 'red')  # computer 对象类型
book = Book('武动乾坤', '天蚕土豆', 15)

stu = Student('JJ', computer, book)  # 此时出现了  包含关系  (stu对象包含了computer对象和book对象)
print(stu)

book1 = Book('斗破苍穹', '天蚕土豆', 20)

# stu.show_book()
stu.borrow_book(book1)

'''
is  a（继承关系）：如果A是B，那么B就是A的基类(base class / 父类)
比如：等边三角形是三角形，则三角形是等边三角形的基类

has  a：如果A中有B，那么，B就是A的组成部分

继承：
   Student，Employee，Doctor  --->都属于人类
   存在相同代码--->代码冗余，可读性不高
   
   将相同代码提取--->Person类
   Student，Employee，Doctor 继承Person类
格式：
   class Student(Person):
        pass
特点：
  1.如果类中不定义__init__，调用父类 super class的__init__
  2.如果类继承父类也需要定义自己的__init__，就需要在当前类的__init__调用一下父类的__init__，再初始化自己特有的属性
  3.调用父类的方法(下文中)
  4.如果父类有eat()，子类也定义一个eat()方法，按照就近原则：先找当前类，再去找父类
    如果子类出现父类同名的方法，可称之为 override--重写(覆盖)。
    此情况一般出现在：父类提供的方法不能满足子类的需求
  5.子类中可调用父类的同名方法
    使用super().方法名(参数)   #可调用父类的方法，再往下写新增的方法(内容)
'''


# 可以定义一个“总类”
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭！','年龄：'+str(self.age))


# 在定义这种相似的类时，可能会出现许多重复的属性或方法，此时需要使用到*继承*
class Student(Person):  # 此为继承的格式
    def __init__(self, name,age):
        print('--->Student的init')
        # 如果要定义自己的__init__，还需调用父类的__init__；可使用super来调用父类的方法
        # super(Student, self).__init__()  # super另一种使用方式
        super().__init__(name,age)  # super() == 父类Person ;调用父类的__init__方法



class Employee(Person):
    def __init__(self,name,age,work):  #新增的属性work，需要在本类中进行处理
        print('--->Employee的init')
        super().__init__(name,age) #调用父类的__init__先将self.name 和 self.age 获取
        self.work = work     #独有属性在本类的__init__里进行初始化
    def __str__(self):
        return '姓名：'+self.name+'年龄：'+str(self.age)+'职业：'+self.work
    
    def eat(self):
        super(Employee, self).eat()  #在子类中调用父类的同名方法，再向下写新增的内容
        print(self.name+'正在吃饭! ')


class Doctor(Person):
    def __init__(self,name,age,department):
        super(Doctor, self).__init__(name,age)  #super(类名，对象).__init__()；底层进行判断:判断该对象是否是以这个类构建出来的
        self.department = department
    def __str__(self):
        return '姓名：'+self.name+'年龄：'+str(self.age)+'部门：'+self.department

'''
对于super关键词的用法： （主要用于多重继承）
Python中的super()方法设计目的是用来解决多重继承时父类的查找问题，所以在单重继承中用不用 super 都没关系；
但是，使用 super() 是一个好的习惯。一般我们在子类中需要调用父类的方法时才会这么用。

1.super(cls,obj)    #即传入类名+对象名
obj对象必须是cls类的对象（cls子类的对象当然也是cls类的对象） ,记作 type(obj) <= cls

2.super(cls1,cls2)    #即传入两个类名
cls2必须是cls1的子类或本身，记作cls2<=cls1   (右的范围小于左)

3.super().__init__()     #等同于 super(A, self).__init__()
'''
# s = Student('JJ', 18)  # 进入父类的__init__进行初始化：从父到子依次创建，父类享有优先级
s = Student('Jack',16)
s.eat()
print(s.name)

e = Employee('Tom',29,'程序员')
print(e)
e.eat()    #此时由于Employee本类中就有eat方法，无需去调用父类(Person)里的eat方法，故此为就近原则

d = Doctor('华佗',88,'老中医')
print(d)
d.eat()



