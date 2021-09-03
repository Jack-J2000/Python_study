'''
类方法：
@classmothod
def test(cls):
    pass

特点：
1.定义需要依赖装饰器@classmothod
2.类方法中只能用类属性，不能用对象属性
3.

'''
class Dog:
    def __init__(self,nickname):
        print('init')
        self.nickname = nickname

    def run(self):  #self  对象   || 对象方法
        print(self)    #打印是对象名和对象空间
        print('{}正在睡觉！'.format(self.nickname))

    @classmethod  #装饰器
    def test(cls):   #cls  class   ||类方法
        print(cls)     #打印是类名
        # print(cls.nickname)   #类空间里没有nickname这个参数

dog = Dog('旺财')
# dog.run()
dog.test()








