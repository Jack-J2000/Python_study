'''
私有化
#封装：
1.私有化属性
2.定义公有set方法和get方法
3.私有化属性不能被继承

#__属性：将属性私有化，访问范围仅仅限于类中
好处：
1.隐藏属性不被外界随意修改
2.也可以修改，需通过函数来修改
     def setXXX(self,xxx):
        #筛选赋值的内容
        if xxx是否符合条件：
            赋值
        else:
            不赋值
3.如果想要获取具体某一个私有化属性，使用getxxx函数
    def getxxx(self):
       return self.__xxx

###python中的dir()函数：
dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；
带参数时，返回参数的属性、方法列表。
如果参数包含方法__dir__()，该方法将被调用。
如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
'''


class Student:
    __age = 18  # 私有化的类属性

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__score = 60  # 外部无法访问，无法修改

    # 定义公有set和get方法

    # set是为了赋值
    def setAge(self, age):  # 可以改变私有化属性的值
        if age > 0 and age <= 100:
            self.__age = age
        else:
            print('年龄不符合规定值！')

    # get是为了取值
    def getAge(self):
        return self.__age

    def __str__(self):
        return '姓名：{}，年龄：{}，分数：{}'.format(self.__name, self.__age, self.__score)

one = Student('JSY', 20)
print(one)

one.age = 21
one.name = 99
print(one)

one.setAge(28)
print(one)

# dir(对象名/类名) 或者  (对象名/类名).__dir__()
print(dir(one))
print(dir(Student))
print(one._Student__age)  # 其实它就是__age，只是系统自动改名了，由此可见，私有化也是伪私有的
print(Student._Student__age)  # 通过该方法访问到了类的私有化属性
print(one.__dir__())

print(__name__)  # 表示当前程序运行在哪一个模块中

'''
在开发中看到一些私有化处理： 装饰器
使用@property，可以代替getxxx():
来获取属性
'''

class Student:
    __age = 18  # 私有化的类属性

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__score = 60  # 外部无法访问，无法修改

    # def setAge(self,age):  #可以改变私有化属性的值
    #     if age>0 and age<=100:
    #         self.__age = age
    #     else:
    #         print('年龄不符合规定值！')
    # def getAge(self):
    #     return self.__age

    #先有getxxx
    @property
    def acquire_age(self):
        return self.__age
    #再有setxxx，因为get依赖set
    @acquire_age.setter
    def assignment_age(self, age):
        if age > 0 and age < 100:
            self.__age = age
        else:
            print('年龄不符合规定值 !')

    def __str__(self):
        return '姓名：{}，年龄：{}，分数：{}'.format(self.__name, self.__age, self.__score)


s = Student('Tom', 99)

s.assignment_age = 98  #给__age赋值
print(s.acquire_age)     #获取__age的值
