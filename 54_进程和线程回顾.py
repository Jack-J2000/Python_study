''
'''
进程，线程
Process类
创建进程：
def func(n):
    pass
p = Process(target=func,name='',args=(1,),kwargs='')
p.start
run()

#自定义进程
class MyProcess(Process):
    def run(self):
        pass
p = MyProcess()
p.start()

#进程的数据共享
n = 0  进程对于变量n，每个进程都有自己的n，互不干扰
 
 #进程池：Pool
 p = Pool(5)
 
 阻塞式    apply(func,args,kwargs)
 非阻塞式  apply_async(func,args,kwargs,callback=进程做完后执行的函数)
 
 #进程间通信
q = Queue(队列容量)
q.put()
q.get()
q.empty()
q.full()

#线程：与进程是包含关系
进程里面可以存着多个线程，多个线程共用进程资源
t = Thread(target=func,name='',args=(1,),kwargs='')
t.start()
GIL：全局解释器锁
线程：'伪线程'

进程做任务速度更快，线程适合做耗时操作

线程同步：
'''
