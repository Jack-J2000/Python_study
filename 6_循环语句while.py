'''
循环方式：
1.while
2.for
while 格式：

while 条件:
       要循环执行的代码

'''
'''
# 例题----打印1-50之间能被3整除的数字
n = 1
while n <= 50:
    if n % 3 == 0:
        print(n)
    n += 1
'''

'''
# 例题-----打印1-10数字之间的累加和
n = 1
sum = 0
while n <= 10:
    sum += n
    n += 1
print(sum)
'''

# count = 0
# while True:     #bool类型的True 第一个字母大写
#     print('------')
#     count += 1
#     if count == 5:
#         break      #跳出while循环
# print('OVER!')

'''
total = 0  # 超市购买商品案例
nums = 0
while True:
    price = float(input('请输入价格：'))
    num = int(input('请输入数量：'))
    total += price * num
    nums += num
    answer = input('当前商品总额%.2f，是否继续购买（输入q停止购买）：' % total)
    if answer == 'q':
        break
print('商品共计%d，商品总共金额为：%.2f' % (nums,total))
'''

# 猜数
'''
产生随机数。
 可猜多次，直到猜对，若猜错了适当给出提示，提示猜大或猜小
 1.统计猜了几次
 2.若1次猜中，运气爆棚！
    2-5次猜中，运气还可以
    6次以上，运气一般
'''
import random

ran = random.randint(1, 50)
sum = 0
print(ran)
while True:  # 当不知道要循环多少次时，可使用 while True .... break
    answer = int(input('请猜一个数：'))
    sum += 1
    if answer > ran:
        print('猜大了！')
    elif answer < ran:
        print('猜小了！')
    else:
        if sum == 1:
            print('运气爆棚！')
        elif 2 <= sum <= 5:
            print('运气还可以')
        else:
            print('运气一般')
        print('猜对了！')
        break

'''
while...else 结构
该结构在已知循环次数时可使用
'''
n = 1
while n <= 5:
    print('JSY')
    if n == 3:
        break
    n += 1
else:
    print('over!')
