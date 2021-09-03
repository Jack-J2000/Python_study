'''
魔术方法：由于  _名字_() 的格式称魔术方法，故_init_()是一个魔术方法

p = Phone()语句解读：
1.先去找有没有一块空间是Phone
2.利用Phone类，向内存申请一块和Phone一样的空间(0x00000228EF0AB790)
3.去Phone中找有没有_init_ ，如果没有，则直接把申请到的内存(0x00000228EF0AB790) 给p (对象)
4.如果有就将地址(0x00000228EF0AB790)作为_int_的参数传过去，再执行_int_，最后把内存空间(0x00000228EF0AB790)给了p

###_init_()方法也是构造方法，使用_init_()方法后，就无法直接调用类里的属性，需要实例化对象才可调用
'''
class Phone:
    name = 'jsy'  #最好使用_init_来创建属性

    #魔术方法之一：  _名字_() 称为魔术方法
    def __init__(self): #系统带的初始化方法；用于初始化对象
        print('init')
        #动态添加属性
        self.color = 'red'  #注意用法   self.属性

    def call(self):
        print(self)
        print('价格：',self.price) #不能保证所有self，都存在price
        print('颜色：',self.color)

p = Phone()
print(p)
p.price = 1000
p.call()
print(p.name)

'''

##使用_init_()来统一对象属性，更方便快捷安全
当_init_() 含参数时
对象方法：

'''
class Person:
    # name = '法外狂徒张三'
    def __init__(self,name,age):  #构造器的精髓所在
        self.name = name
        self.age = age
    def eat(self):
        print('{}正在吃红烧肉!'.format(self.name))
        print('年龄：{}'.format(self.age))

p = Person('赵四',20)
# p.name = '赵四'
p.eat()

p1 = Person('张三',21)
p1.eat()