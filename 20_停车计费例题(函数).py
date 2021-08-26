'''
停车计费系统：
进入停车场记录进入时间，如果出去则记录出去时间，停车时间是：出去-进去时间
停车场的数据结构：
[{'车牌':[进入时间,0]},{'车牌':[进入时间,出去时间]}，....]
15分钟  1快
1小时    4块
停车场变量 --->全局变量
def  enter():
      #键盘输入车牌
      pass
def  go_out():
      #键盘输入车牌
      pass
'''
import time
import random

# 没有车辆
car_park = []


def enter():
    print('欢迎进入停车计费系统')
    number = input('输入车牌号：')
    # 构建结构{'车牌':[0,5]}
    car = {}
    car[number] = [0]  # 键是车牌，值是进场时间
    car_park.append(car)
    print('{}已进场'.format(number))


def go_out():
    number = input('输入车牌号码：')
    for car in car_park:  # {}
        if number in car:
            print('成功出场！')
            # 记录结束时间
            time = random.randint(0, 24)
            time_record = car.get(number) #获取车牌号对应的值，是存储进出时间的列表
            time_record.append(time)        #往列表中添加出场时间
            #计算花费
            total = time * 4  #计算的是每小时4块
            print('{}停车{}小时，应缴费{}'.format(number,time,total))
            print(car_park)
        else:
            print('此车未进场！')
enter()
go_out()
