'''
递归函数：（套娃）
较少使用，文件操作可运用，且递归次数太多会报错
1.递归必须要有出口
2.每次递归都要向出口靠近
定义：一个函数在内部不调用其他函数，而是调用自己本身
'''


# 函数举例
# def test():
#     print("test")
#     a()
#
# def a():
#     print('a')
#     #调用a()
#     a()

# 打印数字  1~10
def test(i):
    if i == 10:
        print('10')  # 此情况递归结束.  需先考虑递归结束的情况
    else:
        print(i)
        i += 1
        test(i)  # 否则的情况下，调用递归


test(1)


# 实现1~10的累加
def test1(i):
    if i == 10:
        return 10
    else:
        return i + test1(i + 1)


r = test1(10)
print(r)


# 函数间的调用
def test(a, b):
    print('-------->test')
    return a + b


def func():
    c = 10
    return c + test(5, 7)  # 此时应先调用test()函数，再返回值，故会打印-------->test


r = func()
print(r)


# 斐波那契数列
def fbnq(i):  # i为斐波那契数列数字顺序
    if i > 2:
        return fbnq(i - 1) + fbnq(i - 2)
    else:
        return 1


r = fbnq(8)
print(r)

'''
#匿名函数
用lambda关键词能创建小型匿名函数。
省略了用def声明函数的标准步骤

使用方式：
lambda  参数列表:(返回值)运算表达式
'''


# 正常函数和lambda函数对比：lambda代码更少
def test(a):
    return a + 1


print(test)
result = test(1)
print(result)

r = lambda a: a + 1  # r是匿名函数的名字
print(r)
print(r(1))

# 例子
r = lambda x, y: x + y
result = r(1, 2)
print(result)

# 匿名函数加上条件语句
func = lambda x: x + 1 if x % 2 == 0 else 0
print(func(1))

'''
匿名函数在高阶函数中的使用
使用场合：当函数需要作参数时，将其定义为匿名函数（该用法居多）
'''


def test():
    print('-------jsy-------')


def func(a, f):
    print('---->', a)
    f()


func(5, test)  # 传递了函数的地址


# 匿名函数做参数
def jsy(x, y, func):
    print(x, y)
    print(func)  # 打印了匿名函数的地址
    result = func(x, y)  # 执行匿名函数并将返回值赋给result
    print('{}+{}={}'.format(x, y, result))


jsy(1, 2, lambda x, y: x + y)  # 匿名函数作为jsy函数的第三个参数出现


# 下为匿名函数例子
def func1(a, f):
    print('------->', a)
    r = f(a)
    print('------>', r)


func1(8, lambda x: x ** 2)  # 现场定义匿名函数并将其作为参数传递，现场调用

'''
匿名函数与内置函数的结合使用
高阶函数：
一个函数在另一个函数中作参数使用
系统高阶函数：max  min  sorted

sorted函数：用来将一个无序列表进行排序
filter类：用来过滤一个列表里符和规定的所有元素，得到的结果是一个迭代器
map类：将列表里的每一项数据都执行相同操作，得到的结果是一个迭代器
reduce函数：对一个序列进行压缩运算，得到一个值；其函数参数用来指定元素按照哪种方式合并（不是系统函数，在functools模块）
'''
m = max(5, 9)
print(m)

m = max([2, 1, 10, 5, 66])
print(m)

# max函数与lambda的结合使用
list1 = [['tom', 19], ['tony', 20], ['lily', 18], ['danniel', 22]]
m = max(list1, key=lambda x: x[1])  # key是max函数要比较的值，且key还要是一个函数，所以用lambda的简洁性来使用；为每个嵌套列表里的第二个元素
print(m)

# sorted函数与lambda的结合使用
result = sorted(list1, key=lambda x: x[1])
print(result)

# filter函数与lambda的结合使用
# filter的匿名函数要求返回值必须是bool类型，只有条件为真才符合过滤条件
result = filter(lambda x: x[1] > 20, list1)  # 迭代list1中的内容
print(result)
print(tuple(result))

# 通过匿名函数指明提取的内容，并对内容进行加工
m = map(lambda x: x[0], list1)  # map(函数，可迭代式)
print(m)
print(list(m))  # 将map对象强转为list

#  (不是系统函数)  reduce使用：   reduce(lambda  x,y:x+y,  [1,2,3,4,5,6])
# reduce有三个参数，第一个为函数，第二个是序列，第三个是初始化值默认为None
from functools import reduce

r = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # 列表元素累加
print(r)

list1 = [1]
r = reduce(lambda x, y: x - y, list1, 2)
print(r)  # 说明初始化值赋给了x，list1中的唯一元素给了y，使x-y=1

# zip()
print(list(zip('abcdefg', range(9), range(9), range(5))))
