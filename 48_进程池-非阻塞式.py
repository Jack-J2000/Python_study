''
import os

'''
当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态生成多个进程，
但是如果是成百甚至上千个目标时，手动的去创建进程的工作量巨大，此时就可以用到multiprocessing模块里的Pool方法
初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没有满
那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到指定的最大值，那么该请求就会等待，
直到池中有进程结束，才会创建新的进程来执行。

进程池分为
非阻塞式：全部添加到队列中，立刻返回，并不等待其他进程执行完毕才结束，
            但是回调函数是等待任务完成之后才会调用执行
阻塞式(意义不大)：
'''
import time
import random
from multiprocessing import Pool
#非阻塞式进程

def task(task_name):

    print('开始做任务啦！',task_name)
    start = time.time()
    #使用sleep()
    time.sleep(random.random()*2)
    # time.sleep(random()*2)
    end = time.time()
    # print('完成任务{}  用时：{},进程ID：{}'.format(task_name,end-start,os.getpid()))
    # return task_name
    return '完成任务{}  用时：{},进程ID：{}'.format(task_name,end-start,os.getpid())

container = []
def callback_func(n):
    container.append(n)

if __name__ == '__main__':
    #创建了容量为5的进程池，在创建的时候就已经分配好了进程号，任务的迭代不影响进程号的改变
    pool = Pool(5)   #进程池的存活依赖于主进程，同生共死
    tasks = ['LOL','洗衣服','吃饭','遛狗','听歌','睡觉']

    for i in tasks:
        #进程池里可装5个进程，但是有6个任务所以最后一个任务需要等其他进程结束才能开始，需要排队
        pool.apply_async(func=task,args=(i,),callback=callback_func)  #使用非阻塞模式(非同步)；callback为回调，当func执行完毕后，return的东西会给到回调函数callback


    pool.close()  #添加任务结束；关闭进程池，不再接收新的请求。
    pool.join()   #堵住主进程，必须在完成任务后才能往下进行

    for i in container:
        print(i)
    print('OVER！')



