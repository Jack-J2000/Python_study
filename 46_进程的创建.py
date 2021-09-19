'''
生活中，你可能一边听歌，一边写作业；一边上网，一边吃饭... 这些都是生活中的多任务场景。
电脑也可以执行多任务，比如你可以同时打开浏览器上网，听音乐，打开pycharm编写代码...，
简单的说**多任务就是同一时间运行多个程序**

-单核CPU实现多任务原理：操作系统轮流让各个任务交替进行，QQ执行2us，切换到微信，再执行2us，再切换到陌陌，执行2us...。
 表面是看，每个任务反复执行下去，但是CPU调度执行速度太快了，导致我们感觉所以任务都在同时执行一样

-多核CPU实现多任务原理：真正的并行执行多任务只能在多核CPU上实现，但是由于任务数量远远多于CPU的核心数量，
 所以，操作系统也会自动把很多任务调度到每个核心上执行

-并发和并行
    -**并发**：当有多个线程在操作时，如果系统只有一个CPU，则它根本不可能真正同时进行一个以上的线程，
    它只能把CPU运行时间划分成若干个时间段，再将时间段分配给各个线程执行，在一个时间段的线程代码运行时，其他线程处于挂起状态。
    这种方式我们称为并发(Concurrent)
    -**并行**：当系统有一个以上CPU时，则线程的操作有可能非并发。当一个CPU执行一个线程时，另一个CPU可以执行另一个线程，
    两个线程互不抢占CPU资源，可以同时进行，这种方式我们称之为并行(Parallel)
-实现多任务的方式：
    -多进程模式
    -多线程模式
    -协程

进程 > 线程 > 协程
进程是线程的容器，是程序的实体
进程是分配空间，线程是分配时间
'''
'''
进程优点：稳定性高，一个进程崩溃了不会影响其他进程
进程缺点：1.创建进程开销巨大 2.操作系统能同时运行的进程数目有限

在linux下可以使用fork函数创建进程，在windows系统上可以引用multiprocessing模块，创建进程。
我们可以使用multiprocessing模块中Process类创建新的进程
python里的fork()在os模块里
'''

'''
进程的创建：
from multiprocessing import Process
process = Process(target=函数,name=进程名,args=(给函数传递的参数))
process.start()  启动进程并执行任务
process.run()  只是执行了任务没有启动进程
terminate()  终止

多进程对于全局变量的访问，在每一个全局变量里面都放一个m变量，
保证每个进程访问变量互不干扰，与变量的可变和不可变无关

多进程与多线程的执行顺序不固定，需要人为控制
'''
from multiprocessing import Process  # 使用该模块创建进程
from time import sleep
import os

m = 1  # 不可变类型


def task1(s, name):
    global m
    while True:
        m += 1
        sleep(s)
        print('这是任务1...', os.getpid(), m)  # 两进程并不共享全局变量m，相当于每个进程单独拥有一份m


def task2(s, name):
    global m
    while True:
        m += 1
        sleep(s)
        print('这是任务2...', os.getpid(), m)


if __name__ == '__main__':
    number = 0

    print(os.getpid())
    # 子进程
    p = Process(target=task1, name='任务1', args=(1, 'aa'))
    p.start()
    print(p.name)  # 打印动作在主进程里
    p1 = Process(target=task2, name='任务2', args=(2, 'bb'))
    p1.start()
    print(p1.name)  # 打印动作在主进程里

    # while True:  # 主进程走到一定程度终止子进程并break
    #     number += 1
    #     sleep(0.1)
    #     if number == 100:
    #         p.terminate()
    #         p1.terminate()
    #         break
    #     else:
    #         print(number)


