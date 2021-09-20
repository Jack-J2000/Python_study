'''
电脑管家里可以，一边杀毒，一边清理电脑垃圾，一边卸载

线程多为耗时操作，也称轻量级进程，是程序执行流的最小单元。
线程自己不拥有系统资源，只拥有一点在运行中必不可少的资源，但它可以与同属一个进程的
其他线程共享进程所拥有的全部资源。一个线程可以创建或撤销另一个线程，同一进程中的多个线程之间可以
并发执行。由于线程之间的相互制约，致使线程在运行中呈现出间断性。线程也有就绪，阻塞，和运行三种基本状态。
每一个程序都至少有一个线程，若程序只有一个线程，那就是程序本身。

'''
'''
多线程(multithreading)：
是指从软件或者硬件上实现多个线程并发执行的技术，可以在单个程序中利用多个线程完成不同的工作。

优点:
1.使用线程可以把占据长时间的程序中的任务放到后台去处理
2.用户界面可以更加吸引人，比如用户点击了一个按钮触发某些事件的处理，可弹出一个进度条显示处理的速度
3.程序执行的速度可能加快

thread 和 threading 提供对线程的支持。thread提供了低级别的，原始的线程以及简单的锁
threading 模块提供其他的方法
threading.currentThread()   #返回当前的线程变量
threading.enumerate()      #返回一个包含正在运行的线程list
threading.activeCount()     #返回正在运行的线程数量。与len(threading.enumerate())结果相同

'''

#线程的使用
'''
如何创建并使用线程？
t1 = threading.Thread(target=download,name='jsy',args=(1,))
t1.start()


就绪-->运行-->阻塞-->就绪  #如果线程在运行时出现阻塞，当阻塞结束后会回到就绪态而不是运行态
'''
#进程：Process
#线程：Thread
import threading
from time import sleep


def download(n):
    images = ['glrl.jpg','boy.jpg','man.jpg']
    for i in images:
        print('正在下载{}'.format(i))
        sleep(n)
        print('{}下载成功！'.format(i))
def listenMusic():
    musics = ['大碗宽面','烤面筋','我们不一样']
    for music in musics:
        print('正在听歌{}'.format(music))


if __name__ == '__main__':
    t1 = threading.Thread(target=download,name='jsy',args=(1,))
    t1.start()
    t2 = threading.Thread(target=listenMusic,name='J')
    t2.start()
    # n = 1
    # while True:
    #     print(n)
    #     sleep(1)
    #     n+=1
