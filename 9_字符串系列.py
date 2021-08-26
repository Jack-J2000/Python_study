'''
转义字符：
\n   换行
\t    退格
\\    输出  \  符号
\'
\"
'''
a = "I 'm Tom"
b = 'Tom said:"I\' m Tom"'
print(b)
print('JSY\nJSY')
print('JSY\tJSY')
print('JSY\\JSY')
print('JSY \'JSY\'')  # 带上单引号
print('JSY\"JSY\"')  # 带上双引号

s1 = 'hello'
s2 = s1  # s1 的地址给 s2 ，使其内容一致
s3 = 'hello'  # 只要有指针地址指向hello，它就不会被回收
s4 = 'jsy'
print(s1, s2, s3)
print(id(s1))  # 输出其地址一致
print(id(s2))
print(id(s3))
print(s1 is s4)  # is 比较的是两个字符串的地址

s1 = 'world'  # 新出现的 world ，需要给它新创建一个内存空间，故ID改变
print(id(s1))

'''
字符串 截取 
'''
s1 = 'ABCDEFG'
print(s1[0])  # 第一个字符
print(s1[2])  # 第三个字符
print(s1[-1], s1[6])  # 说明-1号索引代表了最后一个字符
print(len(s1))  # 表示字符的个数
'''
字符串索引机制：
1.0~len(s)-1
2.-len(s)~-1
'''

'''
切片：字符串，列表
格式：字符串变量[ start : end ]
[start,end)  包前不包后  从左向右切片

[ start , end , step ]
step:
1.步长
2.控制方向    step  正数  从左向右，看起点和终点
                step  负数  从右向左，看起点和终点
'''
s = 'ABCDEFG'

print(s[1:4])  # 从索引1号位到索引4号位；BCD
print(s[:5])  # start可不写，默认为从索引0开始；ABCDE
print(s[-3:-1])  # 包前不包后，从左向右切片，-1号不显示；EF

print(s[-3:7])  # EFG
print(s[-3:])  # 从-3号到最后一号；EFG

x = s[:]  # 为整个字符串
print(x)
print(s)

print(id(x))  # 两地址相同
print(id(s))

# 带步长的切片
print(s[:-1:2])  # 从A到F，进行步长为2的切片
print(s[::4])  # AE
print(s[-3::-4])  # step为负数，从E-->A输出，步长为4

print(s[::-1])  # 倒序输出


'''
查找：
find: 从左向右查找，只要遇到一个符合要求的就会返回位置，若没有找到则返回-1
rfind:从右向左查找，..................................
count: 统计指定字符的个数
index和find的区别：index没有找到就会报错

判断：  （返回bool类型）
startswith :开头是否是...
endwith :结尾是否是...
isalpha :是否是全字母
isdight ：是否是全数字
isspace：是否为空格
isalnum:是否由数字或字母组成
isupper：是否全部是大写字母
islower:是否全部是小写字母

替换内容：
replace(old,new,count)  默认全部替换，也可以通过count指定次数

切割字符串：
split('',maxsplit) 
splitlines() 按行分割
partition() 

修改大小写：
title()        #每个单词的首字母大写
capitalize()  #第一个单词的首字母大写
upper()      #所有字母变大写
lower()      #所有字母变小写

空格处理：
strip()     #去除左右两侧的空格
lstrip()    #去除左侧的空格部分
rstrip()    #去除右侧的空格部分

center()，ljust()，rjust() #添加空格来控制字符串的对齐方式
字符串拼接：
join()
'''
# 例子---网址的分段截取    find , index , rfind , rindex
path = 'https://www.baidu.com/s?wd=%E5%A5%A5%E8%BF%90%E4%BC%9A&rsv_dl=pc_index_tips'
i = path.find('_')
print(i)

# 计算出现次数 count
print(path.count('ht'))

print(path.index('baidu'))  # 返回第一个字符的索引号

# 判断开头
print(path.startswith('http'))
# 判断结尾
print(path.endswith('ps'))

s = 'JSY'
result = s.isalpha()  # 判断是否是全字母组成的
print(result)  # 结果为：True

s = 'JSY1234'
result = s.isalnum()  # 判断是否 由数字或字母组成
print(result)  # 结果为 True

s = '1234'
result = s.isdigit()
print(result)  # 结果为 True

s = '大帅哥JSY大帅哥'  # 字符串的替换
print(s.replace('大帅哥', 'jsy'))
print(s.replace('大帅哥', 'jsy', 1))  # 由于count=1 ，故只替换第一个 ‘ 大帅哥 ’

s = 'JSY jsy 姜世宇'
result = s.split(' ')  # 把所有空格的位置截取出来
print(result)  # 返回结果是一个列表
print(s.split(' ', 1))  # 第二个参数 maxsplit 表示最多分割次数

print(s.partition(' '))  # 只切一刀，以元组形式输出

s = 'hello world'
print(s.upper())  # 所有字母变成大写字母
print(s.title())  # 单词的首字母大写
print(s.lower())  # 所有字母变小写
print(s.capitalize())  # 第一个单词的首字母大写

s = '  jsy  jsy   '
print(len(s))
print(len(s.strip()))
print(s.strip())  # 删除两侧空格
print(s.lstrip())  # 删除左侧空格
print(s.rstrip())  # 删除右侧空格

s = 'hello world'
result = s.center(20)  # 给出20个单位长度，且该字符串居中,参数相当于加字符
print(result)
result = s.ljust(20)  # 给出20个单位长度，该字符串左对齐
print(result)
result = s.rjust(20)  # 给出20个单位长度，该字符串右对齐
print(result)

s = 'hello ' + 'world'
print(s)

# 字符串第二种格式化方式  format
name = '赵丽颖'
age = 18

result = '美女{}今年{}岁'.format(name, age)  # 使用 {} 来进行占位
print(result)

result = '美女{0}今年{1}岁，我也是{1}岁！'.format(name, age)  # 用 0，1数字标号的方式对后面两个参数进行复用
print(result)

result = '美女{name}今年{age}岁，我也是{age}岁！'.format(name='赵丽颖',age=18) #参数名的使用，参数必须在括号里赋值
print(result)

name = '小明'
score_chinese = 100
score_math = 99
s = '{0}本次考试数学分数是：{2},语文分数{1}，英语分数{1}'.format(name,score_chinese,score_math)
print(s)
s = '{}本次考试数学分数是：{},语文分数{}，英语分数{}'.format(name,score_math,score_chinese,score_chinese)
print(s)