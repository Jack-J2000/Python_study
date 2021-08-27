# 算数运算符
a = 1
b = 2
c = a + b
print(a, b, c, 100, 1, sep='-')  # 观看源码可知，修改sep可改变间隔的符号（按CTRL看源码）
print(c / 2)
print(c // 2)  # 整除
print(2 ** 3)  # *代表   2的次幂
print(3 % 2)  # 求余 判奇偶 或是倍数
'''
键盘输入一个三位数，依次输出个位，十位，百位
'''

# number = int(input('请输入一个三位整数：'))
# print(type(number / 10))  # 可知python里整型除后变浮点型
# print(number % 10, int((number / 10)) % 10, int((number / 100)) % 10)  #用数据转换的方式解决
#
# print(number % 10, (number // 10) % 10, number // 100)  # 用到了 //  整除

# 赋值运算符
'''
=
+=
-=
*=
/=
//=
**=
%=

'''
a = 1
a += 1  # a=a+1
print(a)
b += a  # b=b+a
b //= a  # b=b//a

# 关系（比较）运算符

'''
结果： True False
>  <  >=  <=  ==  !=  is
'''
# is 为内存地址的比较
a = 10
b = 23
print(a > b)  # 结果：False
print(a < b)  # 结果：True
x = 'abea'
y = 'abeb'
print(x > y)  # 字符串中从第一个依次比较其ASCII码
print(x < y)

'''
输入考试分数，判断成绩是否在100到80之间
'''
# score = float(input('输入分数：'))
# print(80 <= score <= 100)

# 逻辑运算符   与  或  非
# and  一假便假
# or    一真即真
# not    相当于bool类型中的反面
a = 1
b = 5
print(a and b)  # and 两边为非零数字时，结果显示最后面的数字
print(a or b)  # 两数字非零，输出第一个数
c = 0
print(a and c)  # and 两边出现0 ，则结果为0，仅当两边均大于0，结果才为1

print('jsy' * 5)  # 倍数打印字符串
print('**' * 25)
# 运算符的优先级：（）   **
result = 20 * 5 ** 2  # ** 指数优先级最高
print(result)
a = 1
b = 2
x = 20
print(b > a + x < a + b)  # 2>21<3
print(b > a + (x < a + b))  # 2 > 1+False      (False代表了0；括号也是优先级最高)
