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
    pass

def consume(q):
    pass

if __name__ == '__main__':
    q = queue.Queue(10)
    arr = []

    #创建生产者
    tp = threading.Thread(target=produce,args=(q,))
    tp.start()
    #创建消费者
    tc = threading.Thread(target=consume,args=(q,))
    tc.start()

    tp.join()
    tc.join()








