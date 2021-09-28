# from functools import reduce
# while True:
#     a = list(map(int, input().split()))
#     b = []
#     del a[0]
#     for i in a:
#         if i % 2 != 0:
#             b.append(i)
#     result = reduce(lambda x,y:x*y,b)
#     print(result)

'''
奇数立方和，偶数平方和
'''
# while True:
#     a, b = list(map(int, input().split()))   #注意：输入数字的大小可能不同
#     result1 = 0
#     result2 = 0
#     if a>b:
#         a,b = b,a
#     while a <= b:
#         if a % 2 == 0:
#             sum1 = a ** 2
#             result1 += sum1
#         elif a % 2 != 0:
#             sum2 = a ** 3
#             result2 += sum2
#         a += 1
#     print(result1, result2)

'''
计算牛的数量
'''
# while True:
#     n = int(input())
#     if n <= 4 and n > 0:
#         print(n)
#     elif n > 4:
#         init = 4
#         numbers = [1, 1, 1, 1]
#         circle = n - 4
#         for i in range(circle):
#             add = numbers[-1] + numbers[-3]
#             init +=add
#             numbers.append(add)
#         print(init)
#     elif n == 0:
#         break

'''
计算球的体积
'''
# while True:
#     pi = 3.1415927
#     r = float(input())
#     v = (4/3)*pi*r**3
#     print('%.3f' %v)

'''
水仙花数
'''
# while True:
#     a, b = list(map(int, input().split()))
#     init = 100
#     numbers = []
#     input_num = a
#     flag = 0
#     for i in range(900):
#         if (init % 10) ** 3 + (int(init / 10) % 10) ** 3 + (int(init / 100)) ** 3 == init:
#             numbers.append(init)
#         init += 1
#     for j in range(b - a + 1):
#         if input_num in numbers:
#             print(input_num, end=' ')
#             flag += 1
#         input_num += 1
#     if flag == 0:
#         print('no')

'''
现在告诉你笼子中的鸡和兔共有m只，脚共有n只，且已知鸡的价格为每只100元，兔子的价格为每只150元。
请问这一笼鸡和兔共值多少钱？
如果问题无解则输出“No solution”。
1<=m<=1000，1<=n<=1000。
'''
# a, b = list(map(int, input().split()))
# i = a - 1  # 兔是i
# flag = 0
# for j in range(1, a):  # 鸡是j
#     if 2 * j + 4 * i == b:
#         value = 100 * j + 150 * i
#         print(value)
#         flag = 1
#     i -=1
# if flag==0:
#     print('No solution')
'''
XP最近发现一个很好玩的问题。现在有N盏电灯，序号为1到N，最开始的时候所有电灯都是关闭的。
XP有一群同学，序号是（1~K）,这些调皮的同学会去按电灯的开关，每个同学按开关符合一种规律。
序号为1的同学会按下序号是1的倍数的灯的开关，序号是2的同学会按下序号是2的倍数的灯的开关（将关的灯打开，开的灯关闭）。
现在XP有K位同学，每位同学都去操作一次，问最后有多少盏灯是亮着的？
'''
# while True:
#     N, K = map(int, input().split())
#     light_num = 0
#     for i in range(1, N + 1):
#         operation = 0
#         for j in range(1, K + 1):
#             if i % j == 0:
#                 operation += 1
#         if operation % 2 != 0:
#             light_num += 1
#     print(light_num)

'''
X星人在一艘海底沉船上发现了很多很多很多金币，可爱的X星人决定用这些金币来玩一个填格子的游戏。
其规则如下：第1个格子放2枚金币，第2个格子放6枚金币，第3个格子放12枚金币，第4个格子放20枚金币，第5个格子放30枚金币，以此类推。
请问放到第n个格子时一共放了多少枚金币？
'''
# from functools import reduce
# while True:
#     n = int(input())
#     list = []
#     flag = 1
#     num = 0
#     for i in range(n):
#         num =num+flag*2
#         list.append(num)
#         flag +=1
#     result =reduce(lambda x,y:x+y,list)
#     print(result)
'''
今天英语课，小表弟的英语老师教了他三个与动物有关的单词，分别是cat、pig和horse，
但是粗心的小表弟在写这三个单词的时候经常会写错。
假如小表弟每个单词最多写错一个字母（当然有时候也是会全部写对的，且字母个数是完全正确的）。
你能否编写一个程序，对小表弟写的单词进行自动纠错。
'''
# n = input()
# list1 = ['c', 'a', 't']
# list2 = ['p', 'i', 'g']
# list3 = ['h', 'o', 'r', 's', 'e']
# list = []
#
# for i in n:
#     list.append(i)
#
# if len(n) == 3:
#     cat = 0
#     pig = 0
#     for i in range(3):
#         if list[i] == list1[i]:
#             cat += 1
#         if list[i] == list2[i]:
#             pig += 1
#
#     if cat >= 2:
#         print('cat')
#     if pig >= 2:
#         print('pig')
#
# elif len(n) == 5:
#     horse = 0
#     for i in range(5):
#         if list[i] == list3[i]:
#             horse += 1
#     if horse >= 4:
#         print('horse')

# 正则表达式
# import re
#
# string = input()
# horse = 'hors[a-z]|hor[a-z]e|ho[a-z]se|h[a-z]rse|[a-z]orse'
# cat = 'ca[a-z]|[a-z]at|c[a-z]t'
# pig = 'pi[a-z]|[a-z]ig|p[a-z]g'
# match1 = re.match(cat, string)
# match2 = re.match(pig, string)
# match3 = re.match(horse,string)
#
# if match1:
#     print('cat')
# if match2:
#     print('pig')
# if match3:
#     print('horse')
'''
小明最近在学习图像处理算法。在其中某个算法中使用一个6位十六进制（不区分大小写）的字符串来表示一种颜色。
在6位十六进制的颜色表示方法中，前两位十六进制表示红色(Red)，
中间两位十六进制表示绿色(Green)，最后两位十六进制表示蓝色(Blue)。
现在需要编写一个程序，将使用6位十六进制表示的RGB颜色转成24位二进制。
# n = 'f'
# n1 = int(n,16)
# print(type(n1))
'''
# n = input()
# flag = 0
# num = []
# six=0
# if len(n) == 6:
#     for i in range(6):
#         if n[i] in '0123456789abcdefABCDEF':
#             flag += 1
# elif len(n) == 7 and n[0] == '#':
#     n = n[1:]
#     # print(n)
#     for i in range(6):
#         if n[i] in '0123456789abcdefABCDEF':
#             flag += 1
# if flag == 6:
#     for i in n:
#         result = bin(int(i,16))
#         result = result[2:]
#         num.append(result)
#     for i in num:
#         while True:
#             if len(i)%4==0:
#                 break
#             else:
#                 i='0'+i
#         six+=1
#         if six==6:
#             print(i)
#         else:
#             print(i,end=' ')

'''
Kimi想用“*”号构成一个平行四边形并在屏幕上输出。
当输入一个大于等于2的正整数N时，屏幕上将显示一个由N*N个“*”组成的平行四边形。
例如：输入3，输出如下平行四边形。
  ***
 ***
***
'''
# N = int(input())
# if N>=2:
#     n = N
#     for i in range(N):
#         space = ' '*(n-1)
#         star = '*'*N
#         n -=1
#         print(space+star)
'''
因为某些原因，Jack和Rose没有办法参加毕业演出，
他们两个的工作任务都将由劳模Tom来代替。
现在需要更新演职人员名单，将所有的Jack和Rose替换成Tom。
请你编写一段程序实现人员替换功能。
提示:  replace(old,new,count)
'''
# people = input()
# new_people1 = people.replace('Jack','Tom')
# new_people2 = new_people1.replace('Rose','Tom')
# print(new_people2)
'''
自从学了素数以后，明明喜欢上了数字2、3和5。
当然，如果一个数字里面只出现2、3和5这三个数字，他也一样喜欢，
例如222、2355、223355。
现在他希望你能够帮他编写一个程序，
快速计算出由2、3、5这三个数字组成的由小到大的第n个数，
当然也包括2、3和5。
n=1000 (53352)
'''
# while True:
#     n = int(input())
#     list1 = [2,3,5]
#     list2 = []
#     list3 = []
#     list4 = []
#     list5 = []
#     list6 = []
#     for i in list1:
#         for j in list1:
#             num = i*10+j
#             list2.append(num)
#     # print(list2)
#     # print(len(list2))
#
#     for i in list2:
#         for j in list1:
#             num = i * 10 + j
#             list3.append(num)
#     # print(len(list3))
#
#     for i in list3:
#         for j in list1:
#             num = i * 10 + j
#             list4.append(num)
#     # print(len(list4))
#
#     for i in list4:
#         for j in list1:
#             num = i * 10 + j
#             list5.append(num)
#     # print(len(list5))
#
#     for i in list5:
#         for j in list1:
#             num = i * 10 + j
#             list6.append(num)
#     # print(len(list6))
#     list = list1+list2+list3+list4+list5+list6
#     # print(len(list))
#     print(list[n-1])

'''
输入一个正整数（秒钟），请将其转换成为如下格式：
时:分:秒。
'''
# n = int(input())
# hour = 0
# minute = 0
# second = 0
# while True:
#     if n - 3600 > 0:
#         n = n - 3600
#         hour += 1
#     elif n - 60 > 0:
#         n = n - 60
#         minute += 1
#     else:
#         second = n
#         break
# print('{}:{}:{}'.format(hour,minute,second))

'''
有这样一道智力题：“某商店规定：三个空汽水瓶可以换一瓶汽水。小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？”答案是5瓶，
方法如下：先用9个空瓶子换3瓶汽水，喝掉3瓶满的，喝完以后4个空瓶子，用3个再换一瓶，喝掉这瓶满的，这时候剩2个空瓶子。
然后你让老板先借给你一瓶汽水，喝掉这瓶满的，喝完以后用3个空瓶子换一瓶满的还给老板。如果小张手上有n个空汽水瓶，最多可以换多少瓶汽水喝？
'''
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     new_coco = 0
#     while True:
#         if n >= 3:
#             new_coco += 1
#             n -= 3
#             n += 1
#         elif n == 2:
#             new_coco += 1
#             n = 0
#         if n==0 or n==1:
#             break
#     print(new_coco)

'''
定理：把一个至少两位的正整数的个位数字去掉，再从余下的数中减去个位数的5倍。
当且仅当差是17的倍数时，原数也是17的倍数 。
例如，34是17的倍数，因为3-20=-17是17的倍数；201不是17的倍数，因为20-5=15不是17的倍数。
输入一个正整数n，你的任务是判断它是否是17的倍数。
'''
# while True:
#     n = input()
#     if n =='0':
#         break
#     num1 = n[:-1]    #除个位外其他位数
#     num2 = n[-1]    #个位
#     new_num1 = int(num1)   #变整型
#     new_num2 = int(num2)
#     if (new_num1-5*new_num2)%17==0 and int(n)%17==0:
#         print(1)
#     else:
#         print(0)

'''
。A太太工作了 5天，B太太则工作了 4天，才将花园整理完毕。
C 太太因为正身怀六甲无法加入她们的行列，便出了 90 元。
请问这笔钱如何分给 A、B二位太太较为恰当？A应得多少元？
90/(5+4)*5=50元？如果这么想你就上当了！正确答案是 60元。
假定 A 太太工作了 x 天，B 太太工作了 y 天，C 太太出了 90 元，则 A太太应得多少元？
输入保证二位太太均应得到非负整数元钱。
'''
# n = int(input())
# while n:
#     a, b, c = map(int, input().split())
#     a = a*24
#     b = b*24
#     average = int((a + b) / 3)
#     # print(average)
#     coin_b = b - average
#     coin_a = a - average
#     if coin_b <= 0:
#         coin_a = c
#         print(coin_a)
#     if coin_a <= 0:
#         coin_b = c
#         print(coin_b)
#     if coin_a>0 and coin_b>0:
#         if average!=0:
#             coin_a = int((c/average)*coin_a)
#             print(coin_a)
#         if average==0:
#             print(int(c/2))
#     n -= 1
'''
n 个人站成一行玩一个报数游戏。所有人从左到右编号为 1 到 n。
游戏开始时，最左边的人报 1，他右边的 人报 2，编号为 3 的人报 3，等等。
当编号为 n 的人（即最右边的人）报完 n 之后，轮到他左边的人（即编号为 n-1 的人）报 n+1，
然后编号为 n-2 的人报 n+2，以此类推。当最左边的人再次报数之后，报数方向又变成从左 到右，依次类推。
为了防止游戏太无聊，报数时有一个特例：如果应该报的数包含数字 7 或者是 7 的倍数，他应当用拍手代 替报数。
下表是 n=4的报数情况（X表示拍手）。当编号为 3 的人第 4 次拍手的时候，他实际上数到了 35。
给定 n，m和 k，你的任务是计算当编号为 m的人第 k 次拍手时，他实际上数到了几。 
'''
# while True:
#     n, m, k = map(int, input().split())
#     # print(n, k, m)
#     if n == 0 and k == 0 and m == 0:
#         break
#
#     list = []
#     for i in range(n):
#         list.append(0)
#     circle1 = 0
#     circle2 = 0
#     num = 1
#     flag = 0
#     while True:
#         if circle1 == circle2:
#             for i in range(n):
#                 list[i] = num
#                 num += 1
#
#             if list[m - 1] != 0 and (list[m - 1] % 7 == 0 or '7' in str(list[m-1])):
#                 flag += 1
#             if flag == k:
#                 print(list[m - 1])
#                 break
#             circle1 += 1
#         else:
#             for i in range(n - 2):
#                 list[n - i - 2] = num
#                 num += 1
#
#             if m!=1 and m!=n:
#                 if list[m - 1] != 0 and (list[m - 1] % 7 == 0 or '7' in str(list[m-1])):
#                     flag += 1
#                 if flag == k:
#                     print(list[m - 1])
#                     break
#             circle2 += 1

'''
Kimi号称自己已经记住了1-100000之间所有的斐波那契数。
为了考验他，我们随便出一个数n，让他说出第n个斐波那契数。
当然，斐波那契数会很大。
因此，如果第n个斐波那契数不到6位，则说出该数；否则只说出最后6位(无需输出前导0)。
'''
# while True:
#     n = int(input())
#     a, b = 1, 1
#     if n == 1:
#         print(1)
#     else:
#         for i in range(n - 1):
#             a, b = b, a + b
#         if len(str(b)) <= 6:
#             print(b)
#         else:
#             b1 = str(b)
#             b1 = b1[-6:]
#             # print(b1[-6:])
#             flag = 0
#             for i in range(6):
#                 if b1[i] == '0':
#                     flag += 1
#                 if b1[i] == '0' and i != 5 and b1[i + 1] != '0' and flag == i + 1:
#                     b1 = int(b1[i + 1:])
#                     print(b1)
#                     break
#             else:
#                 b1 = int(b1)
#                 print(b1)

# while True:
#     n = int(input())
#     if n == 1:
#         print(1)
#     elif n > 1:
#         init1 = 1
#         init2 = 1
#         for i in range(n - 1):
#             result = init1 + init2
#             if i != n - 2:
#                 init1 = init2
#                 init2 = result
#         if result < 1000000:
#             print(result)
#         else:
#             print(result % 1000000)
'''
使用递归编写一个程序，求：
S(n)=1-1/2+1/3-1/4+1/5-1/6+......
'''
# import sys    #加入这两行代码，设置递归层数
# sys.setrecursionlimit(10000)
#
# def S(n):
#     if(n==1):
#         s = 1
#     elif(n>1):
#         if(n%2==0):#偶数取负
#             t = -1/n
#         else:
#             t = 1/n
#         s = S(n-1)+t
#     return s
# while(True):
#     a = int(input())
#     n = S(a)
#     print('%.6f'%n)

'''
使用递归编写一个程序，逆序输出一个非负整数。例如输入1234，输出4321(不含前导0)。
'''
# while True:
#     n = input()
#     zero = 0
#     for i in range(len(n)):
#         if n[i] == '0':
#             zero += 1
#         if n[i] == '0' and (i + 1) != len(n) and n[i + 1] != '0' and zero == i + 1:
#             n = n[i + 1:]
#             break
#     # print(n)
#
#     new_n = n[::-1]
#     flag = 0
#     for i in range(len(new_n)):
#         if new_n[i] == '0':
#             flag += 1
#         if new_n[i] == '0' and (i + 1) != len(new_n) and new_n[i + 1] != '0' and flag == i + 1:
#             new_n = int(new_n[i + 1:])
#             print(new_n)
#             break
#     else:
#         new_n = int(new_n)
#         print(new_n)

'''
有一只经过训练的蜜蜂只能爬向右侧相邻的蜂房，不能反向爬行。
请编程计算蜜蜂从蜂房a爬到蜂房b的可能路线数。
1 2 3 5 8
'''
# def func(sub):
#     if sub < 3:
#         return 1
#     else:
#         return func(sub - 1) + func(sub - 2)
#
# while True:
#     a, b = map(int, input().split())
#     sub = b-a+1
#     result = func(sub)
#     print(result)

'''
用大小为1×2的骨牌铺满一个大小为2×n的长方形方格，
编写一个程序，输入n，输出铺放方案总数。例如，输入n=3，即大小为2×3的方格，
输出3。3种骨牌铺放方案如下图所示：
'''
#
# def func(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 2
#     else:
#         return func(n-1)+func(n-2)
#
# while True:
#     n = int(input())
#     result = func(n)
#     print(result)
'''
一只超级青蛙一次可以跳上1级台阶，也可以跳上2级……它也能够跳上n级台阶。
请问，该青蛙跳上一个n级的台阶总共有多少种跳法？

'''
# def func(n):
#     if n == 1:
#         return 1
#     else:
#         return 2*func(n-1)
#
# while True:
#     n = int(input())
#     print(func(n))
'''
使用递归编写一个程序实现汉诺塔问题，要求在输入圆盘数量之后，
输出圆盘的移动步骤，输出格式示例如下：
第1步：1号盘从A柱移至B柱
第2步：2号盘从A柱移至C柱
'''
# def Hanoi(n, A, B, C):
#     if n > 0:
#         Hanoi(n - 1, A, C, B)
#         Move(n, A, C)
#         Hanoi(n - 1, B, A, C)
# def Move(n, a, b):
#     global step
#     step += 1
#     print('第{}步:{}号盘从{}柱移至{}柱'.format(step, n, a, b))
# while True:
#     step = 0
#     n = int(input())
#     Hanoi(n, 'A', 'B', 'C')
#     print()
'''
 告之盘子总数和盘号，计算该盘子的移动次数.
包含多组数据，首先输入T,表示有T组数据.每个数据一行，
是盘子的数目N(1<=N<=60)和盘号k(1<=k<=N)。
'''
# n = int(input())
# while n:
#     a,b = map(int,input().split())
#     print(2**(a-b))
#     n-=1
'''
Kimi开了一家早餐店，这家店的客人都有个奇怪的癖好：他们只要来这家店吃过一次早餐，
就会每天都过来；并且，所有人在这家店吃了两天早餐后，接下来每天都会带一位新朋友一起来品尝。
于是，这家店的客人从最初一个人发展成浩浩荡荡成百上千人：1、1、2、3、5……
现在，Kimi想请你帮忙统计一下，某一段时间范围那他总共卖出多少份早餐（假设每位客人只吃一份早餐）。
'''
# while True:
#     a, b = map(int, input().split())
#     if a == b:
#         pass
#     else:
#         sum = 0
#         flag = 0
#
#         for i in range(a, b + 1):
#             init1 = 1
#             init2 = 1
#             if i > 2:
#                 for j in range(i - 2):
#                     flag = init2+init1
#                     init1 = init2
#                     init2 = flag
#                 sum+=flag
#             else:
#                 sum += 1
#     print(sum)

'''
1, 2, 3...9 这九个数字组成一个分数，其值恰好为1/3，
要求每个数字出现且只能出现一次，如何组合？编写程序输出所有的组合。
'''
#                     下方法         实现全排列
# import itertools
# nums = [1,2,3,4,5,6,7,8,9]
# for val in itertools.permutations(nums):
#     print(val)


# result = []
# def perm(k,n,*args):
#     args = list(args)
#     if k==n:
#         c=''
#         global result
#         for i in range(n+1):
#             c+=args[i]
#         if int(c[:4])*3==int(c[4:]):
#             c1 = int(c[:4])
#             c2 = int(c[4:])
#             # print('{}/{}'.format(c1,c2))
#             result.append('{}/{}'.format(c1,c2))
#     for i in range(k,n+1):
#         t = args[k]
#         args[k]=args[i]
#         args[i]=t
#         perm(k+1,n,*args)
#         t=args[i]
#         args[i]=args[k]
#         args[k]=t
#
# nums = ('1','2','3','4','5','6','7','8','9')
# perm(0,8,*nums)
# print(result[1])
# print(result[0])
'''
编写一个程序，使用递归算法输出一个一维字符数组中所有字符的全排列，假设字符都不一样。
例如{'a','b','c'}的全排列为(a,b,c), (a,c,b), (b,a,c), (b,c,a), (c,a,b), (c,b,a)
'''
# def func(k,n,*args):
#     args = list(args)
#     if k==n:
#         c = ''
#         for i in range(n+1):
#             c+=args[i]
#         print(c)
#         print()
#     for i in range(k,n+1):
#         t=args[k]
#         args[k]=args[i]
#         args[i]=t
#         func(k+1,n,*args)
#         t=args[i]
#         args[i]=args[k]
#         args[k]=t
# while True:
#     n = int(input())
#     char = []
#     a = 97
#     for i in range(n):
#         char.append(chr(a))
#         a += 1
#     func(0,n-1,*char)

'''
现在我们把问题稍微改变一下：如果一共有4根柱子，而不是3根，
那么至少需要移动盘子多少次，才能把所有的盘子从第1根柱子移动到第4根柱子上呢？
为了编程方便，您只需要输出这个结果mod 10000的值。
'''
# def Hanoi(n, A, B, C):
#     if n > 0:
#         Hanoi(n - 1, A, C, B)
#         Move(n, A, C)
#         Hanoi(n - 1, B, A, C)
# def Move(n, a, b):
#     global step
#     step += 1
#     print('第{}步:{}号盘从{}柱移至{}柱'.format(step, n, a, b))
# while True:
#     step = 0
#     n = int(input())
#     Hanoi(n, 'A', 'B', 'C')
#     print()
