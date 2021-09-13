#单例模式是一种开发模式
'''
对于同一个类，每创建一个对象便多占用一个地址空间，容易造成资源浪费
'''
class Student:
    pass

s = Student()
s1 = Student()
print(s)  #两者地址不同表示每创建一个对象就占用一块地址空间
print(s1)

'''
###单例模式的构建
对内存的优化，保证创建出的对象使用同一地址，节省空间
但并不是所有类都适合单例，仅存在特殊情况下
在__new__方法里完成单例模式的构建操作
'''
class Single:
    #私有化  一个类属性；单例地址存在于此
    __instance = None
    name = 'Jack'

    def show(self):
        print('___>show',Single.name)

    #重写__new__
    def __new__(cls):
        print('————>__new__')
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)  #新建对象
        return cls.__instance    #返回之前定义的对象给__init__

s = Single()
s1 = Single()
print(s)       #调用的是同一个空间
print(s1)
print(dir(Single))
# print(Single._Single__instance)
s.show()


'''
#使用装饰器构建单例模式
'''
# def Single1(cls):
#     __instance = {}
#     def __single