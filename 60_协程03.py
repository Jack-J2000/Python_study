#gevent
''

'''
geeenlet已经实现了协程，但是这个人工切换，有些麻烦。
python还有一个比greenlet更强大的并且能够自动切换任务的模块  gevent
其原理是当一个greenlet 遇到IO(指的是input output输入输出，比如网络，文件操作等)操作时，
比如访问网络，就自动切换到其他的greenlet，等到IO完成，在适当的时候切换回来继续执行。

由于IO操作非常耗时，经常使程序处于等待状态，有了gevent我们自动切换协程，
就保证总有greenlet在执行，而不是等待IO


猴子补丁(Monkey pitch)：实现了自动切换
'''
import gevent
import time
from gevent import monkey

monkey.patch_all()  #猴子补丁
def a():  #任务a
    for i in range(3):
        print('A'+str(i))
        time.sleep(0.1)

def b():  #任务b
    for i in range(3):
        print('B'+str(i))
        time.sleep(0.1)

def c():  #任务c
    for i in range(3):
        print('C'+str(i))
        time.sleep(0.1)

if __name__ == '__main__':
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)

    g1.join()
    g2.join()
    g3.join()
    print('Over ！')

'''
可见，协程的实现，可以借助生成器，greenlet,gevent和猴子补丁

'''