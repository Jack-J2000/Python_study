'''
break    跳出当前循环
continue  跳出本次循环，继续下一条循环
'''
# 不打印能被3整除的
for i in range(10):
    if i % 3 == 0:
        continue
    print(i)

'''

循环嵌套
'''
n = 1
while n <= 5:
    print('*' * n)
    n += 1

n = 1
while n <= 5:  # 控制行数
    m = 5
    while m >= n:  # 控制每行 * 的数量
        print('*', end='')
        m -= 1
    n += 1
    print()  # 相当于换行

# 用for循环打印图形
for i in range(5):
    for j in range(i + 1):  # 此处嵌套时需注意 i 的值在下一层会变小。由于[ start , step )
        print('*', end='')
    print()
