'''
字典：   { }
元素： 键值对    注意：键是唯一的，值是可以重复的

下标 或切片  ------> 没有
操作：
1.  添加元素   (先定义字典，再添加元素；为自动添加)
字典名 [key] = value  (key必须是字符串)
注意：key是唯一的，若在添加的时候出现同名key，后面key对应的value替换原来的

2. 修改value值
重新赋值，覆盖之前的值

3. 删除元素内容
clear()   清空字典元素，留下空壳
pop(key)  删除key对应的键值对；返回值为键所对应的值
popitem :  删除最后一个键值对；返回值为键值对；从后往前删
系统自带删除方法：    del  会删除整个字典，地址也不存在了

4.遍历和查询
字典名.key()          #获取所有的键
字典名.value()           #获取所有的值
字典名.items()          #获取键值对
for k,v in book.items():
       print(k,v)
5.获取值的方法：
(1) get(key)           根据key值返回value值；不存在返回默认None，也可设置第二个参数的返回值
(2) 字典名 [key]      不存在会报错
6. in操作时
只能判断键是否在字典里，不能判断值
'''
#定义一个字典
dict1 = {}
dict1['name'] = '阿bin'
print(dict1)

dict1['name'] = 'JJ'
dict1['age'] = 20
dict1['sex'] = '男'
print(dict1)

#改变年龄    键，可以添加，删除，但不可修改；只能改值
dict1['age'] = 21

'''
练习：
book = {}
书名，价格，作者，出版社
促销：价格折扣8折
打印最终字典中的内容
'''
book = {}
book['书名'] = '《武动乾坤》'
book['价格'] = 100
book['作者'] = '天蚕土豆'
book['出版社'] = '***出版社'
#促销 相当与 修改操作
book['价格'] *= 0.8
print(book)

      #         删除操作
# book.clear()  清空
# p = book.pop('出版社') #pop :  删除出版社；返回值为key键对应值
# print(p)
# print(book)

# p = book.popitem()  #popitem :  删除最后一个键值对；返回值为键值对；从后往前删
# print(p)
# print(book)

# del book['价格']
# print(book)

'''
图书管理系统
book = {}
书名，价格，作者，出版社
借书：
books = [{},{}]     #可相当于放多本书的信息；

删除：每一本书里的出版社
最终打印books
'''
books = [{'书名': '《武动乾坤》', '价格': 80.0, '作者': '天蚕土豆', '出版社': '***出版社'},
             {'书名': '《斗破苍穹》', '价格': 80.0, '作者': '天蚕土豆', '出版社': '###出版社'}]
for book in books:
    book.pop('出版社')
    print(book)

#字典的获取值
book = {'书名': '《武动乾坤》', '价格': 80.0, '作者': '天蚕土豆', '出版社': '***出版社'}
#根据key得到value的值
value = book.get('书名1','a')  #若没有key值，则返回第二个参数值 a
print(value)
value = book.get('书名')
# value = book['书名1']
print(value)

for i in book:           #直接遍历字典取出的是key
    print(i)

print(book.values())    #输出字典里所有的值
print(list(book.values()))
for v in book.values():
    print(v)

print(book.keys())      #获取字典所有的key

print(book.items())            #打印键值对
for i in book.items():
    print(i)                   #键值对以元组格式输出

for k,v in book.items():      #键给 k；值给 v
    print(k,v)               #键值对分开，以字符串格式输出

# setdefault  只能作添加键值对使用
book.setdefault('出版日期','10.6')
print(book)

#update 用于合并字典
# dict2 = {'a':1,'b':2}
# book.update(dict2)
# print(book)

#fromkeys   创建一个新字典，第一个参数为键，第二个为值
result = book.fromkeys(['s','j'],4)
print(result)

#split在列表中使用
book = input('请输入书名，价格：').split(' ')
print(book)              #以列表形式输出
name,price = input('请输入书名，价格：').split(' ')
print(name,price)         #同时对两个变量赋值，但是均为字符串型
'''
books = []  容器，可放多本书
书：{}
书名  作者  价格
添加三本书
1.添加书（不能添加同名书籍）
2.
3.
'''
# books = []
# print('~~~~~~~~~~请开始添加书籍~~~~~~~~~~')
# while True:
#     if len(books)==3:
#         break
#     name = input('书名：')
#     while True:
#         for book in books:
#             if book.get('书名')==name:
#                 print('书名重复！')
#                 name = input('请再次输入书名：')
#                 break
#         else:
#             break
#
#     author = input('作者：')
#     price = float(input('价格：'))
#
#     books.append({
#         '书名':name,
#         '作者':author,
#         '价格':price
#     })
#
# print(books)

books = []
flags = True
while flags:
    book = input('请输入要添加的书名，作者，价格(以空格分割)：').split(' ')
    for i in books:
        if i['书名'] == book[0]:
            print('《%s》已存在，请重新输入！' % book[0])
            break
    else:
        books.append({'书名':book[0],'作者':book[1],'价格':book[2]})

print(books)

