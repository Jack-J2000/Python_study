import threading

'''
线程可以共享全局变量。
可以用来做买火车票的程序。


'''
ticket = 1000


def run1():
    global ticket
    for i in range(100):
        ticket -= 1


def run2():
    global ticket
    for i in range(200):
        ticket += 1


if __name__ == '__main__':
    # 创建线程
    th1 = threading.Thread(target=run1(), name='th1')
    th2 = threading.Thread(target=run1(), name='th2')
    th3 = threading.Thread(target=run1(), name='th3')
    th4 = threading.Thread(target=run2(), name='th4')
    th1.start()
    th2.start()
    th3.start()
    th4.start()

    th1.join()
    th2.join()
    th3.join()
    th4.join()
    print('ticket：', ticket)  # 两线程共享变量ticket
