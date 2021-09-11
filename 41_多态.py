'''
私有化(封装)：将属性私有化，定义公有set和get方法
def setAge(self,age):    #使用set和get的方式进行封装
    判断
def getAge(self):
    return self.__age

s.setAge(20)
s.getAge()

#使用@property的方式进行赋值
class Student:
    def __init__(self,age):
        self.__age=age

    @property
    def age(self):
        return self.__age

    @age.setter   #age是接上面的方法名
    def age(self,age):
        self.__age=age

s = Student()
s.age = 10
print(s.age)
'''
'''
继承：
#has a(包含关系)，可直接使用另一个类中的属性方法
    class Student:
      def __init__(self,name,book):  #初始化时，加入了另一个类book
        pass

#is a(真正的继承)    父类和子类
    class Person:
      pass
    
    class Student(Person):
      pass
      

'''
#------------------------------------------
'''
多态：Python并无严格多态概念

'''
class Person:
    def __init__(self,name):
        self.name = name

    def feed_pet(self,pet):  #此时出现了多态；参数pet既可以接收cat，也可以接收dog，还可以接收tiger(不是Pet的子类)或其他对象
        if isinstance(pet,Pet): #判断了pet是否是Pet或Pet子类的对象
            print('{}喜欢养宠物：{}，昵称是：{}'.format(self.name,pet.role,pet.nickname))
        else:
            print('这个不是宠物！可能有危险！！！')
class Pet:
    role = 'Pet'
    def __init__(self,nickanme,age):
        self.nickname = nickanme
        self.age = age

    def show(self):
        print('昵称：{}，年龄：{}'.format(self.nickname,self.age))

class Cat(Pet):
    role = '猫'
    def catch_mouse(self):
        print('抓老鼠...')

class Dog(Pet):
    role = '狗'
    def watch_house(self):
        print('看家...')

class Tiger:
    def eat(self):
        print('凶猛东北虎！')

cat = Cat('妙妙',3)
dog = Dog('旺财',2)
tiger = Tiger()
p = Pet('山竹',1)
person = Person('JJ')

person.feed_pet(cat)  #此时涉及到了多态
person.feed_pet(tiger)
person.feed_pet(p)