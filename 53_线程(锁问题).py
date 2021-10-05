import threading

# GIL全局解释器锁
# 加锁实现线程同步，保证了数据安全，但是速度降低
# 当数据改变量过大时，锁会自动释放，数据不安全，所以线程并不安全，此时需要手动加锁

'''
线程：耗时操作(爬虫，I/O操作)
进程：计算密集型(计算量大)

python底层只要用线程默认加锁
'''
n = 0


def task1():
    global n
    with lock:
        for i in range(10000000):
            n += 1
    print('n的值：', n)


def task2():
    global n
    with lock:
        for i in range(10000000):
            n += 1
    print('n的值：', n)


if __name__ == '__main__':
    lock = threading.Lock()
    th1 = threading.Thread(target=task1, name='th1')
    th2 = threading.Thread(target=task2, name='th2')
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print('最后打印{}'.format(n))
