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

class 类名[(父类)]:
             属性:
             方法:
'''
class car:  #自动继承了object
    brand = '红旗'

print(car)
#使用类创建对象 (利用一个模子来复刻)
jsy = car()  #对象的产生
print(jsy)
print(jsy.brand)
jsy.brand = '特斯拉'
print(jsy.brand)


'''
属性:
类属性，对象属性
'''
class Student:
    #类属性
    name = 'Jack'
    age = 18


