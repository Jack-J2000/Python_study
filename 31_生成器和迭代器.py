'''
生成器简介：
通过列表生成式(列表推导式)，我们可以直接创造一个列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，要是我们仅仅需要访问前面几个元素，
那后面绝大多数元素占用的空间都会被白白浪费了。所以，如果列表元素可以按照某种算法推导出来，那我
们就可以在循环的过程中不断推算出后续的元素。这样就不必创建完整的list，从而节省大量的空间。在Python
中，这种一边循环一边计算的机制，称为生成器：generator

得到生成器方式：
1.通过列表推导式得到生成器，外部是括号
2.借助函数完成，关键字 yield

'''
newlist = [x + 1 for x in range(10)]
print(type(newlist))
print(newlist)

# 得到生成器
g = (x + 1 for x in range(10))
print(type(g))  # 一个生成器对象，可迭代
print(g)
# 如果提前将生成器迭代完成，接下来将无法迭代，抛出异常：StopIteration
# flag = 0
# for i in g:
#     flag+=1
#     print(i)
#     if flag==8:     #这里将生成器迭代到了第八个
#         break

# 生成器的使用，方式一   -->通过调用_next_()
print(g.__next__())
print(g.__next__())

# 方式二 --->   next(生成器对象)    builtins 系统内置函数
print(next(g))
print(next(g))

g = (x * 3 for x in range(10))

while True:
    try:
        e = next(g)
        print(e)
    except:
        print('生成器的元素已迭代完毕，没有更多元素了！')
        break

'''
#借助函数定义生成器
#只要函数里出现了yield关键字，说明函数就不是函数了，变成了一个生成器对象
步骤：
1.定义一个函数，函数中使用yield关键字
2.调用函数，接收调用的结果，结果即为生成器
3.借助next()，_next_()得到元素

'''


def func():
    n = 0
    while True:
        n += 1
        print(n)
        yield n  # 动作：   return n  + 暂停(保留现场)
        print('JJ')


g = func()
print(g)  # g为生成器对象

print(next(g))  # 调用next()时，程序进入了func()执行代码，直到遇到yield，把n返回并退出函数
print(next(g))  # 第二次调用时，其实是从yield下方开始执行代码


# 不用递归出斐波那契数列
def fib(length):  #参数为斐波那契数列的长度
    i, j = 0, 1
    n = 0
    while n <length:
        yield i
        i,j=j,j+i
        n+=1
    return '没有更多元素！' #当调用生成器超范围时，报错StopIteration后的提示信息

g = fib(4)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

'''

'''
def gen():
    i = 0
    while i<5:
        temp =yield i
        print('temp:',temp)
        i +=1
    return '没有更多的数据！'

g = gen()
