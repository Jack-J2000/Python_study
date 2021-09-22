# 协程：微线程
''
import time

'''
进程 > 线程 > 协程(相当于电脑管家(进程)里的杀毒功能(线程)中同时查(协程)C，D，E盘中的文件)

Process---Thread---生成器完成(yield)
协程：只要出现耗时操作就会切换动作，争取时刻资源都处于利用状态，高效利用CPU
耗时操作---网络操作，网络下载(爬虫)，I/O操作(文件读写)，堵塞
'''


def task1():
    for i in range(3):
        print('A' + str(i))
        yield
        time.sleep(1)


def task2():
    for i in range(3):
        print('B' + str(i))
        yield
        time.sleep(2)


if __name__ == '__main__':
    g1 = task1()
    g2 = task2()
    while True:
        try:
            next(g1)
            next(g2)
        except:
            break
