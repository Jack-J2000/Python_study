'''
参数：外界向函数传值

返回值：函数内容向外界传送；使用函数里面定义的参数
            若一个函数有返回值，则需要接收
            返回多个值时，为元组形式
            停止函数的调用，立刻结束函数并返回值
            当函数没有返回值时，返回None
类似JAVA：  return
'''

def get_sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(get_sum(1, 2, 4))


def get_sort(number):
    # 排序：冒泡排序
    for i in range(0, len(number) - 1):
        for j in range(0, len(number) - 1 - i):
            if number[j] > number[j + 1]:
                number[j], number[j + 1] = number[j + 1], number[j]
    # 获取头，尾
    min = number[0]
    max = number[-1]
    print(number)
    # 返回
    return min, max  # 返回多个值时，为元组形式

list1 = [21, 11, 25, 69, 96, 12, 1, 10, 20]
print(get_sort(list1))

# a, b = (1, 2)
# print(a, b)


'''
全局变量和局部变量：函数里没有a，则使用全局变量a；想要在函数里改变全局变量，需用global
                       函数里有a ，优先用局部变量a；在函数内部声明局部变量
                       局部变量调用函数时创建，函数完成后被回收
                       查看全局变量使用globals() ---->是一个字典，分为  1.系统  2.自定义
                       查看局部变量使用locals()  ---->字典
全局变量只能在函数内调用，但不可在函数内改变；想要在函数里改变全局变量，需加global
global关键字的使用：  （可变与不可变；值与地址之间的关系）
只有不可变的类型才需要添加global
可变的类型不需要添加global
不可变类型：当改变变量的值时，地址发生了改变   int  str  float  tuple
可变类型：True False  list，字典，集合(内容改变时，地址也不会变)

'''
#查看全局和局部变量
J = 21
print(globals())
print(locals())


# 全局变量
a = 100


def test1():
    # 局部变量
    a = 0
    print('a = ', a)  # 函数里有a ，优先找内部a


test1()


def test2():
    b = 2
    print('a = ', a)  # 函数里没有a，则使用全局变量a
    print('b = ', b)


test2()


def test3():
    # 改变全局变量a的值
    global a
    a = 0     #在全局上，a的值变为0
    print('a = ',a)
test3()


'''
函数间调用的实现：
验证是否登录：islogin
      自定义一个判断用户是否登录功能islogin
      参数：username,password
      判断用户输入用户名密码是否正确，如果正确则返回Ture，否则返回False
      
借书：borrow_book
参数：bookname
函数体：
判断是否登录，若登录可借书
没有登录会出现提示
'''
# islogin = False
# def login(username, password):
#     global  islogin
#     if username == 'jsy' and password == '1234':
#         print('登录成功！')
#         islogin = True
#     else:
#         print('登录失败！')
#
# def borrow_book(bookname):
#     if islogin:
#         print('成功借阅{}'.format(bookname))
#     else:
#         username = input('用户名：')
#         password = input('密码：')
#         login(username, password)

# borrow_book('武动乾坤')
# borrow_book('武动乾坤') #此时的 islogin是True

#案例
library = ['红楼梦','西游记','三国演义']
def add_book(bookname):
    if bookname not in library:
        library.append(bookname)
    else:
        print('已经存在该书！')
def show_book():
    for book in library:
        print(book)

add_book('墨菲定律')
show_book()

