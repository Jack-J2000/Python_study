'''
自定义进程：
当父类不满足需求时

start()：
1.开一个新的进程
2.run()
'''
from multiprocessing import Process
from time import sleep
class MyProcess(Process):  # 继承了主进程
    def __init__(self,name):
        super(MyProcess,self).__init__()
        self.name = name

    # 重写run方法
    def run(self):
        n = 1
        while True:
            sleep(1)
            print('{}____自定义进程:{}'.format(n,self.name))
            n += 1

if __name__ == '__main__':
    p = MyProcess('小明')
    p.start()
    p1 = MyProcess('小红')
    p1.start()