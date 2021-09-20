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
 
'''
