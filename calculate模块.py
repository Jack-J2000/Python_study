# __all__ = ['name']
name = 'JSY'  #变量


def add(*args):
    if len(args) > 1:
        sum = 0
        for i in args:
            sum += i
        return sum
    else:
        print('请至少传入两个参数')


def sub(*args):
    if len(args) > 1:
        n = 0
        for i in args:
            n -= i
            return n
    else:
        print('请至少传入两个参数')


class Calculate:
    def test(self):
        print('正在使用Calculate！')

    @classmethod
    def test1(cls):
        print('正在调用一个类方法')
def test():
    print('__name__：',__name__)
if __name__  =='__main__':
    print(__name__)  #__name__ ---> __main__

print('calculate方法')  #当调用该模块时，执行该语句