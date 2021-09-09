'''
Python：函数式编程与面向对象式编程都要使用
对象  ---> 具体事物(世间万物皆对象)
现实中事物--->转成电脑程序

面向对象：
     类
     对象
     属性
     方法
对象：
     A的汽车
     B的汽车
     C的汽车
     D的汽车
#对象的集合 ---->汽车类--->共同特征：(属性)价格，颜色，品牌，型号              (方法)起步，加速，转弯，停车

所有的类名要求首字母大写，多个单词使用驼峰式命名

1.定义类：
class 类名[(父类)]:
             属性:
             方法:
2.使用类
对象名 =  类名()

'''
class car:  #自动继承了object
    brand = '红旗'

print(car)
#使用类创建对象 (利用一个模子来复刻)
jsy = car()  #对象的产生
print(jsy)

print(jsy.brand)    #使用类中定义好了的属性
jsy.brand = '特斯拉'   #使用类中的属性并自己定义值
print(jsy.brand)


'''
属性:
类属性，对象属性
#当对象调用属性时，先在对象属性(自己的空间)里找，再在类属性(模型的空间)里找

'''
class Student:
    #类属性
    name = 'Jack'
    age = 18

JSY = Student()
JSY.gender = '男'
print(JSY.gender)

#修改类中的属性
Student.name = 'JackLove'
print(JSY.name)  #JSY对象里没有定义name，所以使用类中的属性name

'''
类中的方法：
方法种类：(对象方法)普通方法，类方法，静态方法，魔术方法
普通方法格式：
def 方法名(self,[参数，参数]):
        方法内容
'''
class Phone:
    brand = 'HuaWei'
    price = 3999
    type = 'nava 4'

    #Phone里面的方法：call
    def call (self):
        print(self)  #self是调用该函数的对象
        print('正在打电话...')
        print('主人：',self.name)

phone1 = Phone()
phone1.name = 'Jack'

print(phone1)
phone1.call()  #call方法中的self表示，谁调用call函数就会把自身作为参数传给call
Phone.call(phone1)

