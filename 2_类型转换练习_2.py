'''
键盘输入两个数，并输出两个数的和
input(输入第一个数：)
input(输入第二个数：)

'''
one = input('输入第一个数：')
two = input('输入第二个数：')
sum = float(one) + float(two)  # 无法将带小数点的字符串，例如1.1转化为整型
print('这两个数的和是：' + str(sum))
print(sum)
print(type(sum))

print(float(one) - float(two))

'''
字符串a
str-->int     int(a)   但是如果a是带小数点的  例如 9.9  则报错
str-->float   float(a) 字符串可以带小数点

int-->str   str(a)
float-->str str(a)

int-->float  float(a)  加小数点
float-->int  int(a)     小数点后数字被抹除
'''
a = 5
print(bool(a))
