'''
java的for循环：
for(  ;  ;  ){
      循环体
}

Python的for循环：
for  i   in   range(n):
           循环体中的内容

对于range方法：
                      range(n)：默认从0开始取值到n-1结束
                      range(start,stop)：[ start , stop )
                      range( start , stop , step )：step默认为1，是步长
'''

for i in range(10):  # 由结果可知range(n)  默认从零开始取值  0-->n-1
    print(i)  # 例题----1-10数字的打印

for i in range(1, 11):  # range(start,stop)  范围  [ start , stop)  最后一个数不包含
    print('---->', i)

print('-*-' * 10)

for i in range(1, 10, 2):  # range(start,stop,step)   step为增量，即从1开始每隔2个打印
    print('---->', i)

'''
for...else 结构

for i in range(n)
        循环体
else:
    当上面的for循环0~n-1没有出现中断 （break），则执行else语句
    即 ：已知循环次数时
'''
# 最多输入三次用户名和密码，若都不成功，提示账号被锁定
'''
for i in range(3):  # 最多走三次循环
    name = input('请输入用户名：')
    password = input('请输入密码：')
    if name == 'jsy' and password == '123':
        print('登录成功！')
        break
    print('用户名或密码错误！')
else:
    print('账号已锁定！')
'''

# else特点：不被中断（break），即可执行
'''
for i in range(n):           ---->当用于确定次数的循环时，更好用一些
      pass
while  条件：            ----->1.固定次数循环  2.不确定的循环
     pass
     

掷骰子游戏
两个骰子：1-6
1.玩游戏要有金币
2.玩游戏赠金币1枚，充值获取金币
3.10元的倍数，20个金币
4.玩游戏消耗5个金币
5.猜大小：猜对   奖励2枚金币   猜错没有金币   （两个骰子相加>6为大，否则为小）
6.   游戏结束 ： （1.）主动退出  （2.）没有金币退出
7. 退出时 打印金币数，共玩了几句
'''
import random

coins = 0
sum = 0
if coins < 5:
    print('金币不足请及时充值！')
while True:
    money = int(input('请输入充值的金额：'))
    if money % 10 == 0:
        coins += money * 2
        print('充值成功！当前金币数：%d' % coins)
        answer = input('是否开始游戏（y/n）：')
        while answer == 'y' and coins > 5:
            coins -= 5
            coins += 1
            print('~~~~~~~游戏开始~~~~~~~~')
            sum += 1
            ran1 = random.randint(1, 6)
            ran2 = random.randint(1, 6)
            guess = input('请猜大小（大/小）:')
            if guess == '大' and ran2 + ran1 > 6 or guess == '小' and ran2 + ran1 <= 6:
                print('猜对了！奖励2个金币')
                coins += 2
            else:
                print('猜错了！')
            answer = input('是否继续游戏（y/n）：')
        print('总共玩了%d局，金币数：%d' % (sum, coins))
        break  # 该break是退出while True 的循环
    else:
        print('充值失败！请充值10的倍数')
