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
while True:
    n = input()
    if n =='0':
        break
    num1 = n[:-1]    #除个位外其他位数
    num2 = n[-1]    #个位
    new_num1 = int(num1)   #变整型
    new_num2 = int(num2)
    # print(new_num1)
    # print(new_num2)
    if (new_num1-5*new_num2)%17==0 and int(n)%17==0:
        print(1)
    else:
        print(0)
'''
我们首先提取出对话的最后一句话，把所有非字母的字符替换成空格，把所有字符 替换成小写，
然后导出一个单词列表（由空格隔开），只要列表中的任何一个单词是 hehe，
这 段对话就算作“止于呵呵”。
本题只考虑由 n(n>1)个 he连接而成的单词，比如 hehehe或者 hehehehe。
'''
import re
name = []
conversation = []
while True:
    dialogue = input()
    for i in range(len(dialogue)):
        if dialogue[i]==':':
            a = dialogue[:i]
            b = dialogue[i+1:]
            name.append(a)
            conversation.append(b)
            break

    new_b = b.strip()
    new_b = new_b.split(' ') #存放输入各单词的列表
    flag1 = 0 #是否满足呵呵

    for i in new_b:
        i = i.lower()
        if len(i)%2==0 and int((len(i)/2))*'he'==i:
            flag1 = 1
            break
    if flag1:
        break







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
