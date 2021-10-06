# greenlet 完成协程任务 可以更好得进行任务切换
import time
from greenlet import greenlet


def a():  # 任务a
    for i in range(3):
        print('A' + str(i))
        gb.switch()
        time.sleep(0.1)


def b():  # 任务b
    for i in range(3):
        print('B' + str(i))
        gc.switch()
        time.sleep(0.1)


def c():  # 任务c
    for i in range(3):
        print('C' + str(i))
        ga.switch()
        time.sleep(0.1)


if __name__ == '__main__':
    # 通过手动控制switch，完成ABC依次打印
    ga = greenlet(a)
    gb = greenlet(b)
    gc = greenlet(c)
    ga.switch()
