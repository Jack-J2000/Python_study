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
while True:
    N, K = map(int, input().split())
    light_num = 0
    for i in range(1, N + 1):
        operation = 0
        for j in range(1, K + 1):
            if i % j == 0:
                operation += 1
        if operation % 2 != 0:
            light_num += 1
    print(light_num)
