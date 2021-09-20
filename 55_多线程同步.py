''
'''
共享数据：如果多个线程同时对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步
同步：一个一个的完成，一个做完，另一个才能进来，效率就会降低，而安全性增高
使用Thread对象的Lock和Block可以实现简单的线程同步，这两个对象都有acquire方法和release方法，
对于那些需要每次只允许一个线程操作的数据，可以将其放到acquire和release方法之间。

多线程的优势在于可以同时运行多个任务(至少感觉像是这样)。
但是当线程需要共享数据时，可能存在数据不同步问题，
为了避免这种情况，引入了锁的概念

lock = thread.Lock()
lock.acquire() 请求得到锁
lock.release()  释放锁

只要不释放，其他的线程都无法进入运行状态
'''
import threading
import random
import time

lock = threading.Lock() #定义一个锁
list1 = [0] * 10


def task1():
    # 获取线程锁，如果已经上锁，则等待锁的释放
    lock.acquire()  # 阻塞
    for i in range(len(list1)):
        list1[i] = 1
        # time.sleep(0.5)
    lock.release()  # 释放锁


def task2():
    lock.acquire()  #阻塞
    for i in range(len(list1)):
        print('--->',list1[i])
        # time.sleep(0.5)
    lock.release()

if __name__ == '__main__':
    t2 = threading.Thread(target=task2())
    t1 = threading.Thread(target=task1())

    t1.start()
    t2.start()

