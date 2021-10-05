'''
queue
'''
from multiprocessing import Queue

q = Queue(5)  # 队列容量
# 向队列里添加元素
q.put('A')
q.put('B')
q.put('C')
q.put('D')
q.put('E')
print(q.qsize())
# timeout表示2秒后报异常
if q.full() == False:  # full判断队列是否为满  empty判断队列是否为空
    q.put('A', timeout=2)  # 自动阻塞，当加入时超过最大容量只能等待队列里的元素被取走
else:
    print('队列已满！')

# 获取队列的值
print(q.get())  # 当队列为空时还在取元素，会阻塞
print(q.get())
print(q.get())
print(q.get())
print(q.get())
# print(q.get(timeout=2))
# q.put_nowait('J')
# q.get_nowait()
'''
get(),put()为阻塞式，队列为空或为满时等待
get_nowait,put_nowait 为非阻塞式，队列为空或为满时不等待，直接报异常
'''

'''
进程通信：

'''
from multiprocessing import Process
from time import sleep


def download(q):
    images = ['glrl.jpg', 'boy.jpg', 'man.jpg']
    for i in images:
        print('正在下载{}'.format(i))
        sleep(1)
        q.put(i)


def getfile(q):
    while True:
        try:
            file = q.get(timeout=5)
            print('{}保存成功！'.format(file))
        except:
            print('全部保存成功！')
            break


'''
简单的理解 Queue 实现进程间通信的方式，就是使用了操作系统给开辟的一个队列空间，
各个进程可以把数据放到该队列中，当然也可以从队列中把自己需要的信息取走。
'''
# 开两个进程，执行下载任务，利用队列来对两进程之间实现通信
if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))  # target为待执行任务；注意只写函数名不加括号
    p2 = Process(target=getfile, args=(q,))  # 利用args传入队列对象

    p1.start()
    p1.join()  # 将任务全部执行完毕后才可执行下一步
    p2.start()
    p2.join()

    print('!!!!!!')
