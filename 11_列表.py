'''
列表好比一个容器
如何定义一个列表：
1.  空列表: []
2.有内容的列表：['','',''] , [1,2,3,4]  [ 3.5,9.9,5.2]  #任意数据类型均可放，也可放列表
3.列表间可相加

'''
list1 = []
list2 = ['牛奶', '12', '辣条', '方便面']  # 与字符串中的机制十分相似
print(list2)
print(list2[2])

# 切片
print(list2[2:4])
print(list2[::-3])
print(list2[-1:1:-2])  # start 和 end 的方向不能 和 step的方向冲突，否则显示为空

s = 'abcdefg123'
for i in s:
    print(i)
'''
列表： 增   删   改   查
增：
append()  追加，类似于排队，可将列表视为整体添加
extend()   添加一个列表(接连添加其元素，不能加入整个列表)
insert(位置，元素)
删：
remove() #根据输入元素名，删除对应的元素；若无此元素则报错 (可先使用 in 判断是否存在要删除的元素)；存在多个同名时，仅删除第一个
clear()   #清空列表
pop()     #下标写的时候不要超出范围，不写内容时从后往前删
del()     #与pop的机制相似
改：
index(元素) :根据元素找该元素的下标，返回索引值（若没有此元素则报错）
列表[index] = 新值
查：
1.元素 in 列表  返回bool类型  ；元素  not in 列表
2.列表.index(元素)  返回索引号
3.列表.count(元素)  返回整数
排序：
sort(reverse)  #默认升序，当参数reverse=True时，可排序为降序
reverse() #单纯的把列表倒过来输出
'''
list1 = []
list2 = ['LOL']

list1.append('蒙多')
list1.append('辛吉德')
list1.append('崔丝塔娜')
print(list1)

# 列表的合并
list1 += list2  # 第一种方法
print(list1)

list1.extend(list2)  # 第二种方法，在list1后加上list2
'''
##商品添加例子##
container = []
flag = True
while flag:
    name = input('商品名称：')
    price = input('商品价格：')
    number = input('商品数量：')
    goods = [name,price,number]
    container.append(goods)  #以整个列表的形式添加到container

    answer = input('是否继续添加?(按q或Q退出)')
    if answer.lower()=='q':
        flag = False
print('---'*15)
print('名称\t价格\t数量')
for goods in container:
    print('{}\t{}\t{}'.format(goods[0],float(goods[1]),int(goods[2])))
#打印出  共**件  总金额***

'''
list1 = ['面包', '鸡蛋', '火腿', '包子']
list1.pop()  # 下标写的时候不要超出范围，不写内容时从后往前删
print(list1)

if '鸡蛋' in list1:
    list1.remove('鸡蛋')  # 根据输入元素名，删除对应的元素；若无此元素则报错 (可先使用 in 判断是否存在要删除的元素)
print(list1)

# 连续出现同一字符串会出现漏删的情况
list2 = ['赛恩', '泰达米尔', '维嘉', '维嘉', '莫德凯撒']
for i in list2:
    if i == '维嘉':
        list2.remove(i)  # 由于删除后，后面元素自动补上，再移动索引会出现指向错误
print(list2)

# 使用while循环解决漏删问题
list2 = ['赛恩', '泰达米尔', '维嘉', '维嘉', '莫德凯撒']
n = 0
while n < len(list2):
    if list2[n] == '维嘉':
        list2.remove('维嘉')  # 移除后索引不动，后面字符串自动补上
    else:
        n += 1
print(list2)

# for循环的改进，解决漏删问题
list2 = ['赛恩', '泰达米尔', '维嘉', '维嘉', '莫德凯撒', '维嘉', '维嘉']
for i in list2[::-1]:  # 倒着删。由于删除一个元素，其余元素向左补充
    if i == '维嘉':
        list2.remove('维嘉')
print(list2)

list2 = ['赛恩', '泰达米尔', '维嘉', '维嘉', '莫德凯撒', '维嘉', '维嘉']
for i in range(list2.count('维嘉')):  #删除确定数量的字符串
        list2.remove('维嘉')
print(list2)

# 插入 insert
list1 = ['1', '2', '3', '4', '5', '6']
list1.insert(1, 8)  # 用法：(位置，元素)  占用位置后，其他元素向后移动
print(list1)
weizhi = list1.index('1')  # 返回元素的索引值
print(weizhi)


#生成8个1-20之间的随机整数，保存到列表中，然后循环打印，进行排序
import random
numbers = []
for i in range(8):
    ran = random.randint(1,20)
    numbers.append(ran)
print(numbers)

# numbers.sort()  #对列表排序，默认升序
# print(numbers)

# numbers.sort(reverse=True) #通过使用reverse参数排序，当为True时结果为降序；而默认为False，
# print(numbers)

# numbers.sort()
# numbers.reverse()  #先升序，再用reverse倒着输出，间接实现降序
# print(numbers)

'''
生成8个1-100之间的随机整数，保存到列表中
键盘输入一个1-100之间的整数，将整数插入到排序后的列表中（升降没有要求）
'''
# numbers = []
# for i in range(8):
#     ran = random.randint(1,100)
#     numbers.append(ran)
# print(numbers)
# num = int(input('请输入一个1-100之间的随机整数：'))
# numbers.append(num)
# numbers.sort()
# print(numbers)

#交换两个变量的值
a = 2
b = 3
print(a,b)
# a,b = b,a  #交换两个变量的值
# print(a,b)
c = 5
a,b,c = b,a,b  #b的值给a; a的值给b; b的值给c
print(a,b,c)

#冒泡排序
numbers = []
#随机生成8个1~100的整数，并添加到列表中
for i in range(8):
    ran = random.randint(1,100)
    numbers.append(ran)
print(numbers)
#对列表的元素进行排序
for j in range(0,len(numbers) - 1):
    for i in range(0,len(numbers)-j-1):  #一轮后，把最大 的数送到最后的位置
        if numbers[i] > numbers[i+1]:
            a = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = a
print(numbers)
