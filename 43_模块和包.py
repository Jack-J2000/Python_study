#模块
'''
在Python中，模块是代码组织的一种方式，把功能相近的函数放到一个文件中，
一个文件(.py)就是一个模块(module)，模块名就是文件名去掉后缀py。
好处：
1.提高代码的可复用性，可维护性，一个模块编写完成后，可以很方便的在其他项目中导入
2.解决了命名冲突，不同模块中相同的命名不会冲突

常用标准库：
builtins                   内建函数默认加载
math                      数学库
random                  生成随机数
time                        时间
datetime                日期和时间
hashlib                     加密算法
copy                        拷贝
functools               常用的工具
os                          操作系统接口
re                          字符串正则匹配
sys                         Python自身的运行环境
multiprocessing       多进程
threading                多线程
json                        编码和解码 JSON对象
logging                     记录日志，调试
'''
import calculate模块

'''
1.自定义模块
2.使用系统的模块

呼叫其他模块的方法：
1.import  模块名
   调用后使用时可能不太方便：
   使用模块中的函数  模块名.变量   模块名.函数   模块名.类
2.from 模块名  import 变量|函数|类   
    可调用模块中某一部分

3.from 模块名 import *
    调用该模块的所有内容
    但是如果想限制获取的内容，可以在模块中使用__all__ = [可被获取的内容]
    (__all__只针对带 * 时)
4.无论是import和from的形式，都会将模块的内容进行加载
   如果不希望其进行调用。就会用到__name__
   在自己的模块用__name__，叫__name__ = __main__
   在其他模块通过导入的方式调用，__name__ = 模块名
'''
#自定义模块 calculate模块
list1 = [9,8,7,6,5,4,0]

#第一种方法
import calculate模块


#使用模块中的函数  模块名.变量   模块名.函数   模块名.类
sum = calculate模块.add(*list1)  #拆包
print(sum)
#使用模块中的变量
print(calculate模块.name)

#使用模块中的类
cal = calculate模块.Calculate()
print(cal)   #对象的空间
cal.test()
calculate模块.Calculate.test1()  #类方法可直接调用
calculate模块.Calculate.test(cal)   #对象方法需创建一个对象，借助对象来调用

#第二种方法
from calculate模块 import *   #在被调用的模块中加入__all__可限制允许调用的内容
# from calculate包 import add,name  #加逗号表示导入同一个包的不同部分
result = add(*list1)
print(result)

test() #不在原模块执行__name__时，会打印原模块的名字


'''
包(Python Package)：存放py文件，一定要有__init__.py文件   (字母+下划线的文件夹形式)
文件夹(Directory)：存放非py文件，在文件夹里建一个__init__.py文件就可以将它变成包

一个包中可以放多个模块；项目 > 包 > 模块 > 类 函数 变量

导包的方法：
1.from 包名 import 模块名
2.from 包名.模块名 import 具体内容(类，属性，方法等)   #该方法使用最多
3.from 包名.模块名 import *
  在被导入的模块里，使用__all__ = [被导入的具体内容]
4.from .模块名 import 具体内容   #导入当前包下的模块里的某内容(易出现问题)
5.from 包名 import *  #表示该包中的内容不能完全访问，仅对在__init__中__all__允许的内容进行访问

当想要导入同级包下的模块时，也应该按照from *** import ** 的格式进行，不能直接import
'''
#导入包的模块
from test_Package import models
m = models.Model('lily',123)  #使用包中模块的内容
print(m)
m.show()


# from test_Package.models import Model   #导入包的同时，执行里面的__init__动作
# m = Model('Tom',321)
# print(m)
# m.show()

'''
包的__init__.py文件
当导入包的时候，默认调用__init__.py文件
作用：
1.当导入包的时候，把一些初始化的函数，变量，类定义在__init__.py文件中
2.此文件中函数，变量等的访问，只需要通过包名.函数...
3.结合__all__ = [通过* 可以访问的模块]
'''
# from test_Package import *  #表示不能访问此包



'''
模块的循环导入问题：
一般出现在大型的项目中，需要很多python文件，
而架构不当，可能会出现模块之间的互相导入问题

#两个模块里的函数出现了互相调用，程序出现了死循环
A(模块):
    def test():
       func()
B(模块):
    def func():
       test()

 如何避免循环导入？(解决问题)
 1.重构代码(需很大成本,工作量)
 2.将导入的语句放到函数里面
 3.将导入语句放在模块最后，用from 方式
 4.将导入语句放在模块顶部，用import方式
 
 
 
'''
def task():
    print('---task---')



