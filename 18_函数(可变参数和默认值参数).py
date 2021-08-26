'''
函数：  重复使用
定义格式：
def  函数名([参数，.....]):
      代码

函数命名名举例：get_name()      驼峰命名法用于多单词
                          search()
代码：
         封装重复内容

参数：
         1. 无参数
         2.有参数
'''


def jsy():  # 将函数加载到内存空间
    print('jsy')


jsy()  # 调用函数
'''
定义一个login函数：
admin 1234
输入用户名和密码，验证是否正确
'''
# def login():
#     username  = input('请输入用户名：')
#     passwords = input('请输入密码：')
#     if username=='admin' and passwords=='1234':
#         print('登录成功！')
#     else:
#         print('登录失败！')
# login()


p = 'JSY'


def prin(p):
    print(p)


prin(p)
'''
带参数例子：
1. login 带参数，n表示允许输入错误的次数.
2. 求1-n的累加和
'''

# def login(n):
#     sum = 0
#     flag = 0
#     while True:
#         result = input('请输入密码：')
#         if sum < n-1:
#             if result == 'jsy':
#                 print('解锁成功！')
#                 break
#             else:
#                 sum += 1
#                 flag = n - sum
#                 print('解锁失败，您还有%s次机会' % flag)
#         else:
#             print('机会已用尽！冻结中...')
#             break
# login(5)

def sum(i):
    a = 1
    s = 0
    for j in range(i):
        s += a
        a += 1
    print('1~{}的总和是{}'.format(i,s))
sum(5)

'''
默认值参数：
在定义函数的时候，有一个或多个参数已经赋好值了
def 函数名(参数1，参数2，参数3=值，参数4=值):
    pass
在调用时：  函数名(参数1，参数2)  #默认设置好的参数值可以不写；当然，写上会覆盖默认参数值
              在定义函数的时候，普通参数要位于默认值参数的前面
              默认参数的顺序是固定的，可以通过指明关键字参数来赋值，通过关键字赋值可改变赋值顺序
'''


def borrow_book(username, bookname, number=1, school='北大'):
    print('进入{}的借书系统...'.format(school))
    print('{}已借{}，借阅{}本'.format(username, bookname, number))


borrow_book('jsy', '狂人日记')
borrow_book('jsy', '大主宰', 6)
borrow_book('jsy', bookname='朝花夕拾', school='清华')  # 指明关键字参数来赋值，非默认参数也可使用

'''
当参数的数据类型是列表
'''
library = ['高数', '政治', '英语', '计算机组成和原理']


def add_book(bookname):  # 形参
    library.append(bookname)
    print('添加成功！')


def show_book(books):  # 遍历时相当于library的地址
    for book in books:
        print(book)


add_book('数据结构')  # 实参
show_book(library)  # 实参

'''
可变参数：
*args         （arguments）默认为一个容器，多个参数，缺省参数在*args的后面
**kwargs     （keywardarguments）关键字参数多个

装包：
def   函数(*args):     --->定义函数时，此时出现装包
     pass

拆包：
list , tuple , set
调用函数的时候：
函数名(*list)   #拆开当中的元素
'''


# 举例：   求和问题
def get_(*a):  # 可写入多个参数
    print(a)  # 以元组形式输出


get_(1)
get_(1, 2, 3, 4)

a, *b, c = 1, 2, 3, 4, 5
print(a, b, c)  # a和c只能赋一个值，而b可以列表形式存放多值

# 装包
a, b, c = (1, 2, 3)  # 参数值对应等量的数据
print(a)
print(b)
print(c)

# 拆包
ran_list = [23, 4, 5, 47, 85, 96, 1, 0]  # 需要先进行拆包
def get_sum(args): #再进行装包
    print(args)
    s = 0
    for i in args:
        s += i
    print('和：', s)

get_sum(ran_list)  # 自动拆包


# 可变参数：**kwargs  注意它的传值方式
def show_book(**kwargs):
    print(kwargs)  # 打印为字典
    for k, v in kwargs.items():
        print(k, v)


show_book()
show_book(bookname='墨菲定律', author='鸿雁')  # 仅以键值对的形式赋值，加到字典中

# 一颗星*是拆元组列表集合的包，两颗星**是拆字典的包
book = {'book': '红楼梦', 'author': '曹雪芹'}
show_book(**book)


#    *和**同时存在
def show_(*args, **kwargs):
    print(args)
    print(kwargs)


book = {'book': '红楼梦', 'author': '曹雪芹'}
show_('jsy', 'JJ', **book)
