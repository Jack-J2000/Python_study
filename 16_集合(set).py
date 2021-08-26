'''
集合（底层是通过字典封装）：
set
特点：
1.没有重复，无序的
2.与字典区分：当花括号内容不是键值对的时候，为集合

添加：
1.add         加入元素
2.update   加入集合
移除：
1.remove     移除不存在元素，报错
2.discard     移除不存在元素，什么也不做
3.del       仅可对集合使用，无法指定元素(因为元素是混乱的)
4.clear    清空集合，留下空壳
5.pop      随机删除一个元素
交集intersection：公共部分
并集union：两集合相加
差集difference：
补集：
'''
set1 = {'jsy'}  # 当花括号不为空，内容不是键值对的时候，为集合
print(type(set1))

list1 = [1, 3, 4, 5, 8, 9, 1, 5, 9, 3, 6]

set2 = set(list1)  # 转集合后，去重复元素，并排序
print(set2)

# 空集合定义
set3 = set()
print(type(set3), len(set3))

# 添加元素
set3.add('武动乾坤')
print(set3)

set4 = {'jsy', '稻香', '爱的代价', '大碗宽面'}
set4.update(set3)
print(set4)  # 多个字符串元素输出时没有固定顺序

# append   extend   insert   ---> List   有序，允许重复
# add    update  ---> Set         无序，不允许重复

'''
产生5组(不重复)，字母和数字组成的4位验证码

'''
import random

m = 'asdfghjklqwertyuiopzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
set5 = set()
while True:
    s = ''
    for i in range(4):
        ran = random.choice(m)  # 用choice随机选择验证码
        s += ran
        # index = random.randint(0,len(m)-1)
        # s += m[index]
    set5.add(s)
    if len(set5) == 5:
        break
print(set5)

set = {'7Vqj', '2xte', 'rGYY', 'tWfi', '4wLo'}
# set.remove('a')  #移除不存在元素，报错
# print(set)
set.discard('a')  # 移除不存在元素，什么也不做
print(set)
set.pop()  # 随机删除元素
print(set)

# 交集intersection    并集union    差集difference
set2 = {1, 2, 3, 4, 5}
set3 = {3, 4, 5, 6, 7, 8, 9}

result = set2.intersection(set3)
print(result)

result = set2.union(set3)
print(result)

result = set2.difference(set3)  # set2 与 set3不同的部分，以set2为主体
print(result)

# 集合间用运算符   +  -  *
print(set2 & set3)  # 交集符号  &
print(set2 | set3)  # 并集符号 |
print(set2 - set3)  # 差集符号 -

'''
list: 允许重复，有序，有下标  []
tuple：允许重复，里面元素不能增加删除修改，只能查看 ()
dict：键值对形式存在    键：唯一   值：允许重复  { }
set：不允许重复，无序  { }

类型转换：
list ---> tuple,  set(不能重复，长度有可能发生改变)
tuple --->list , set
set --->  list,tuple  (此三者均可相互转)

dict ---> list,tuple (仅能把字典的键转进去，没有值)
list  --->  dict (仅出现以下情况时可转)
list = [['a',1],('',2),('c',3)]   #列表内可以是，列表或者是元组，而它们里面的内容必须成对
print(dict(list))
'''
list = [['a', {1}], ('', 2), ('c', 3)]
print(dict(list))

'''
图书管理系统：
至少5本书
library = [{'bookname':'xxx','author':'xxx','price':100,'number':xx},{ },{ }]

1.借书
2.还书
3.查询书(书名/作者)
4.查看所有
5.退出
'''
library = [
    {'bookname': '武动乾坤', 'author': '天蚕土豆', 'price': 100, 'number': 5},
    {'bookname': '斗破苍穹', 'author': '天蚕土豆', 'price': 100, 'number': 5},
    {'bookname': '大主宰', 'author': '天蚕土豆', 'price': 100, 'number': 5},
    {'bookname': '绝世唐门', 'author': '唐家三少', 'price': 100, 'number': 5},
    {'bookname': '三体', 'author': '刘慈欣', 'price': 100, 'number': 5}
]
print('~~~~~~~~~~~~~欢迎进入图书管理系统~~~~~~~~~~~~~~~')

while True:
    choice = input('请选择你要的服务：\n 1.借书\n 2.还书\n 3.查找书籍\n 4.查看所有书籍\n 5.退出')
    if choice == '1':
        bookname = input('请输入书名：')
        bookauthor = input('请输入作者：')
        for book in library:
            if book['bookname'] == bookname and book['author'] == bookauthor:
                if book['number'] > 0:
                    print('借书成功！')
                    book['number'] -= 1
                    break
                else:
                    print('抱歉，您要借的书库存为0')
                    break
        else:
            print('抱歉，您要的书不存在')
    elif choice == '2':
        bookname = input('请输入书名：')
        bookauthor = input('请输入作者：')
        for book in library:
            if book['bookname'] == bookname and book['author'] == bookauthor:
                book['number'] += 1
                print('还书成功！')
                break
        else:
            print('输入错误！')
    elif choice == '3':
        answer = input('请选择查找方式：\n 1.按书名查找\n 2.按作者查找\n')
        if answer == '1':
            bookname = input('请输入要查找的书名：')
            for book in library:
                if book['bookname'] == bookname:
                    print('书名：' + book['bookname'] + ',作者：' + book['author'] + ',价格：' + str(book['price']) + ',数目：' + str(
                book['number']))
                    break
            else:
                print('没有找到！')
        elif answer == '2':
            bookauthor = input('请输入要查找的作者：')
            for book in library:
                if book['author'] == bookauthor:
                    print('书名：' + book['bookname'] + ',作者：' + book['author'] + ',价格：' + str(book['price']) + ',数目：' + str(
                book['number']))
                    break
            else:
                print('没有找到！')
        else:
            print('错误！')
    elif choice == '4':
        for book in library:
            print('书名：' + book['bookname'] + ',作者：' + book['author'] + ',价格：' + str(book['price']) + ',数目：' + str(
                book['number']))
    elif choice == '5':
        break
    else:
        print('选择错误！请重新选择！')
