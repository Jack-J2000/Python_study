#猫
class Cat:
    type = '猫'

    def __init__(self,nickname,age,color):
        self.nickname = nickname
        self.age = age
        self.color = color

    def eat(self,food):
        print('{}喜欢吃{}！'.format(self.nickname,food))

    def catch_mouse(self,mouse_color,mouse_weight):
        print('{}抓了一只{}KG的{}老鼠'.format(self.nickname,mouse_weight,mouse_color))

    def sleep(self,hour):
        print('%s已经睡了%d小时！' %(self.nickname,hour)) #字符串另一种格式化方式

    def show(self):
        print('这只猫的详细信息：')
        print('名字：{}'.format(self.nickname))
        print('年龄：{}岁'.format(self.age))
        print('颜色：{}'.format(self.color))

#创建对象
cat1 = Cat('山竹',3,'白色')
#通过对象调用方法
cat1.catch_mouse('黑色',1)
cat1.sleep(6)
cat1.eat('小鱼干')
cat1.show()