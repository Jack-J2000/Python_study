''
'''
开发过程中使用线程，在线程间共享多个资源的时候，
如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁
尽管死锁很少发生，但一旦发生就会造成应用的停止响应，程序不做任何事情

避免死锁的方法：
1.重构代码
2.在acquire里加timeout=
'''
from threading import Lock, Thread
import time

lockA = Lock()
lockB = Lock()


class MyThread(Thread):
    # def __init__(self,name):
    #     pass

    def run(self):  # start()
        if lockA.acquire():  # 如果获取到锁则返回Ture
            print(self.name + '获取了A锁')
            time.sleep(1)  # 线程1在休息的时候B锁就被线程2获取了，所以无法获取B锁
            if lockB.acquire(timeout=2):  # 如果2秒得不到B锁，两秒后释放A锁
                print(self.name + '又获取了B锁')
                lockB.release()
            lockA.release()


class MyThread1(Thread):
    def run(self):  # start()
        if lockB.acquire():  # 如果获取到锁则返回Ture
            print(self.name + '获取了B锁')
            time.sleep(1)
            if lockA.acquire():
                print(self.name + '又获取了A锁')
                lockA.release()
            lockB.release()


if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread1()

    t1.start()  # 默认执行自定义线程里的 run()方法
    t2.start()
