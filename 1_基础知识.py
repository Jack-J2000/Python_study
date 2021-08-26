# print('JSY')
# 单行注释  CTRL+/

# 下为多行注释
'''
hahaha
'''

# 格式化   CTRL+ALT+L

# for i in range(10):
#     print(i)

# 行的复制   CTRL+D
# 删除一行   CTRL+X或CTRL+Y

'''
变量命名   
弱语言：变量声明的时候对数据类型不是很严格。
JAVA ：int   float 有一定规范限制

Python变量名的命名规范：
1.字母，数字，下划线，其他符号不可以
2.不能数字开头
3.不能使用关键字
4.严格区分大小写
(以后做项目时尽量做到，见名知义)
'''
# getNameByLine  驼峰式命名 （小驼峰） 第一个单词的首字母小写
# GetNameByLine 大驼峰   每个单词的首字母大写
# get_name_by_line  下划线命名

# 名字=520     汉字命名会有黄牌警告
# print(名字)

'''
数据类型和类型转换
数字：int，float，long
布尔(boolean)：True，False

字符串：string (单引号或双引号下均为字符串，再有三引号下也可)
列表：List
元组：Tuple
字典：Dictionary

'''
money = '28'
print(type(money))  # 打印输出该变量的数据类型，且该变量值之后可发生变化
money = 1
print(type(money))

message = '钢铁侠说："I am IronMan"'  # 使用单双引号来控制包含关系，单引号和双引号的位置可以互换
print(message)

shi = '''
            静夜思
            唐 李白 
    床前明月光，疑是地上霜。
    举头望明月，低头思故乡。
'''
print(shi)  # 三引号用于保留格式的输出

# 布尔类型：True False
# 开发中的判断，例如：是否登录成功......

# 类型转换
Number = input('请输入一个数字：')  # 阻塞
# print(UserName + 1000)  此时报错，需要进行类型转换   str-->int
print(int(Number) + 1000)  # 整形数的相加，实现类型转换
print(Number + '1000')  # 字符串的连接
print(Number + str(1000))
print(type(Number))  # 由input输入的数据类型默认为字符串类型

'''
字符串进行格式化
%d   整型
%s   字符串
%f   浮点型  （输出自动保留6位小数）
%c   字符型
'''
name = 'JSY'
age = 21
money = 12.34
print(name + '已经' + str(age) + '岁了！')
print('%s已经%d岁了！' % (name, age))  # 字符串的格式化输出，类似与C语言的输出

print('%s已经%d岁了！,但是身上只有%f块钱。'%(name,age,money))  #自动保留六位小数
print('%s已经%d岁了！,但是身上只有%.2f块钱。'%(name,age,money)) #  将%f变为%.2f  可手动保留2位小数

print('%s已经%s岁了！,但是身上只有%s块钱。'%(name,age,money))  #  %s的功能较为强大，使用在整型或，浮点型上将其自动转换为字符串型

#内置方法
'''
print()
input()
type()
id()
len()

min()
max()
sum()
abs()   绝对值
sorted()   排序完成后以列表形式输出

bin()
oct()
hex()

chr()    根据ASSCII值转换为对应的字符
ord()    根据字符转换为对应的ASSCII值

del  变量名
in
not  in
is
isinstance(变量，类型)  判断该变量是否是该类型
+  支持 字符串，列表，元组
*  支持 字符串，列表，元组
- & | 只能在 集合上使用
'''
list1 = [1,2,3,4,8,9]
result = max(list1)
print(result)

result = sum(list1)
print(result)




