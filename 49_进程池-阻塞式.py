'''
进程池之阻塞式
'''
'''

阻塞式特点：
添加一个任务，执行一个任务，如果一个任务不结束，其他任务进不来

进程池：
pool = Pool(max)   #创建进程池对象
pool.apply()    #阻塞的
pool.apply_async()   #非阻塞的

pool.close() #停止添加进程
pool.join()  #让主进程让步
'''
import os
import time
import random
from multiprocessing import Pool
def task(task_name):

    print('开始做任务啦！',task_name)
    start = time.time()
    #使用sleep()
    time.sleep(random.random()*2)
    # time.sleep(random()*2)
    end = time.time()
    print('完成任务{}  用时：{},进程ID：{}'.format(task_name,end-start,os.getpid()))

# container = []
# def callback_func(n):
#     container.append(n)

if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['LOL', '洗衣服', '吃饭', '遛狗', '听歌', '睡觉']

    for i in tasks:
        # 进程池里可装5个进程，但是有6个任务所以最后一个任务需要等其他进程结束才能开始，需要排队
        pool.apply(func=task, args=(i,))  # 使用阻塞模式，没有回调函数；一人任务结束后才加入下一个任务
    pool.close()
    pool.join()

