''
'''
生产者与消费者：两线程间的通信

Python的queue模块中提供了同步的，线程安全的队列类，包括FIFO（先入先出）队列Queue，
LIFO（后入先出-栈）队列LifoQueue，和优先级队列PriorityQueue。这些队列都实现了锁原语
（可以理解为原子操作，即要么不做，要么就做完），能够在多线程中直接使用。
可以使用队列来实现线程间的同步。

'''
import threading
import queue
import random
import time


def produce(q):
    i = 0
    while i < 10:
        num = random.randint(1, 100)
        q.put('生产者产生数据：%d' % num)
        print('生产者产生数据：%d' % num)
        time.sleep(1)
        i += 1
    q.put(None)
    #完成任务
    q.task_done()

def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print('消费者获取到：%s' %item)
        time.sleep(2)
    #完成任务
    q.task_done()


if __name__ == '__main__':
    q = queue.Queue(10)
    arr = []

    # 创建生产者
    tp = threading.Thread(target=produce, args=(q,))
    tp.start()
    # 创建消费者
    tc = threading.Thread(target=consume, args=(q,))
    tc.start()

    tp.join()
    tc.join()
    print('END！')

'''
线程总结：
线程 Thread

1.创建线程
    A方法.
    t.Thread(target=func,name='',args=(),kwargs={})  ---新建状态
    t.start()  ---就绪状态
    run()    ---运行状态
    join()  ---阻塞状态
    
    B方法.自定义线程
    class MyThread(Thread):
        def __init__(self,name):
            super().__init__()
            self.name = name
        def run(self):
            任务
    t = MyThread('name')
    t.start()
    
2.数据共享
    进程共享数据与线程共享数据的区别：
        进程是每个进程中都有一份
        线程是共同一个数据 --->  出现数据安全问题
    GIL ---> 伪线程，自动加锁(全局共享锁)
    lock = Lock()
    lock.acquire()
    ......
    lock.release()
    
    ---> 使用锁时需避免死锁
    
3.线程间通信：生产者与消费者案例
    生产者：线程
    消费者：线程
    q = queue.Queue()
    
    # 创建生产者
    tp = threading.Thread(target=produce, args=(q,))
    tp.start()
    # 创建消费者
    tc = threading.Thread(target=consume, args=(q,))
    tc.start()
    
    q.put()
    q.get()
扩展：GIL

'''