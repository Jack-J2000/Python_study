# 1.列表推导式
# 2.字典推导式
# 3.集合推导式

'''
列表推导式：在列表推导式里最左边放着的  要么是待放入的元素，要么是待改变的机制(if...else)
'''
# 过滤掉长度小于或等于3的人名
names = ['tom', 'lily', 'jack', 'gor', 'A']

result = filter(lambda name: len(name) > 3, names)  # 用过滤器的方式
print(result)  # 输出一个过滤器对象
print(type(result))
for i in result:
    print(i)

result = [name.title() for name in names if len(name) > 3]  # 对选出的元素首字母大写，用列表推导式的方法
print(result)

# 将1-100之间能被3整除，组成一个新的列表
newlist = [i for i in range(1, 101) if i % 3 == 0]
print(newlist)


# 将  偶数0-5  奇数0-10  按照   [(偶数，奇数),(),() ] 的方式输出

def func():
    newlist = []
    for i in range(5):
        if i % 2 == 0:
            for j in range(10):
                if j % 2 != 0:
                    newlist.append((i, j))
    print(newlist)


func()

newlist = [(i,j) for i in range(5) if i % 2 == 0 for j in range(10) if j % 2 != 0]  #使用列表推导式，相比起来极大的节省了代码空间
print(newlist)


#list = [[1,2,3],[4,5,6],[7,8,9],[1,3,5]] ----->[3,6,9,5]
list = [[1,2,3],[4,5,6],[7,8,9],[1,3,5]]
newlist = [l[-1] for l in list]
print(newlist)

#当出现  if...else结构   时需注意
#出现了三目运算符 ：         为真时的结果 if 判定条件 else 为假时的结果
dict1 = {'name':'Jack','salary':6000}
dict2 = {'name':'Jsy','salary':10000}
dict3 = {'name':'Tom','salary':4500}

list1 = [dict1,dict2,dict3]
#如果薪资大于5000加200，低于等于5000加500
newlist = [person['salary']+ 200 if person['salary'] else person['salary']+500 >5000 for person in list1] #改变字典中的值并且放入新列表中
print(newlist)

'''
集合推导式：大致与列表推导式相同；自动删去重复元素
'''
list1 = [1,2,5,6,8,1,2,4,9]
set1 = {num+1 for num in list1}
print(set1)  #自动删去重复元素

'''
字典推导式：
'''
#进行键值的颠倒
dict1 = {'a':'A','b':'B','c':'C'}
newdict = {value:key for key,value in dict1.items()} #注意元素要以键值对的形式存在
print(newdict)
