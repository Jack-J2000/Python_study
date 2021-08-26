'''
列表推导式：最终得到的是一个列表
格式1：
list1 = [ for i in 可迭代的 ]
格式2：
list2 = [ i for i in range(0,101) if i%2==0 ]
'''
list1 = []
for i in range(1, 21):
    list1.append(i)
print(list1)
####下为列表推导式的使用
list1 = [i for i in range(1, 21)]
print(list1)

# 1~100之间的偶数
list2 = [i for i in range(0, 101, 2)]
print(list2)

# 格式2的使用
list2 = [i for i in range(0, 101) if i % 2 == 0]
print(list2)

# 另一种使用方法
list3 = ['66', '007', 'jsy', 'JSY', 'main']
list4 = [word for word in list3 if word.isalpha()]
print(list4)

# 如果是  h开头的则将首字母大写，不是h开头的则全部大写
# 格式3  [结果1  条件   else  结果2   for 变量 in 可迭代的]       条件成立往左执行，条件不成立往右执行
list3 = ['66', 'hhh', 'jsy', 'JSY', 'main']
list5 = [word.title() if word.startswith('h') else word.upper() for word in list3]  # 对于列表元素的修改
print(list5)

# 格式4 两层for循环
new_list = []
for i in range(1, 5):
    for j in range(1, 4):
        new_list.append((i, j))
print(new_list)
# 下为使用列表推导式（简化）
list6 = [(i, j) for i in range(1, 5) for j in range(1, 4)]
print(list6)

# 列表推导式练习
# 1. 请写出一段 python代码   实现分组一个 list 里面的元素，比如[1,2,3,4,5,6,...,100]，变成[[1,2,3],[4,5,6],...]
# 2. 找出里面名字含有两个 'e' 的放到新列表中：
# name = [['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe'],
#              ['Alice','Jill','Ana','Wendy','Jennifer,'Sherry','Eva']]

test1 = [i for i in range(1, 101)]
print(test1)
test2 = [test1[j:j + 3] for j in range(0, len(test1), 3)]
print(test2)

name = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
        ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# new = []
# for obj in name:
#    for o in obj:
#        if o.count('e')==2:
#            new.append(o)
# print(new)
#                         下为        列表推导式方法
test3 = [o for obj in name for o in obj if o.count('e')==2]
print(test3)