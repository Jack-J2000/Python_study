'''
abs()  函数  ：求绝对值
允许区间比较

条件语句
if
if...else
if...elif...else
在进行嵌套时，需注意每行的缩进问题
格式：
if    条件：
      条件成立要执行的语句
---------------------------------------------
if    条件：
      条件成立要执行的语句
else：
       print('')
-----------------------------------------------
if    条件1：
       条件1成立要执行的语句
elif  条件2：
        条件2成立要执行的语句
else：
        都不符合时要执行的语句
'''

''''案例
Number = int(input("请输入："))
if Number == 4:
    print('123')
    print('over')
else:
    print('条件不成立！')
'''

# 条件语句案例  猜数字
''''
import random
ran = random.randint(1, 10)  # 产生从1到10随机一个整数
print(type(ran))
guess = int(input('请猜一个数：')) #此时需注意数据类型的转换

if guess == ran:
    print('猜对了！')
else:
    print('没猜到！')
    print('结果应为%d'%(ran))
'''

'''
人员管理系统，功能：添加员工   删除员工  查询员工  修改员工信息

'''
print('--------欢迎进入人员管理系统--------')
choice = int(input('请选择功能：\n 1.添加员工\n 2.删除员工\n 3.查询员工\n 4.修改员工信息\n'))
if choice == 1:
    print('添加员工')
elif choice == 2:
    print('删除员工')
elif choice == 3:
    print('查询员工')
else:
    print('修改员工信息')
print('--------------------------------')

# 三元运算符
a = 1
b = 2

# 以下两种格式效果一样
'''
if a < b:
    c = a
else:
    c = b
----------------------------------------
c = a if a < b else b
'''

# 自动类型转换
if '0':  # 字符串有内容为  真
    print('111')
if '':  # 字符串无内容为假
    print('222')
if 0:  # 整型0  为假
    print('333')
