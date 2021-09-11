'''
编写一个简单的工资管理程序，系统可以管理以下四类人：工人(worker)，销售员(saleman)，经理(manager)，销售经理(salemanger)
所有的员工都有员工号，姓名，工资等属性，有设置姓名，获取姓名，获取员工号，计算工资等方法
    1.工人：工人具有工作小时数和时薪的属性，工资计算方法为工作小时数*时薪
    2.销售员：具有销售额和提成比例的属性，工资计算方法为销售额*提成比例
    3经理：具有固定月薪的属性，工资计算方法为固定月薪
    4.销售经理：工资计算方法为销售额*提成比例+固定月薪
请根据以上要求设计合理的类，完成以下功能：
    (1)添加所有类型的人员
    (2)计算月薪
    (3)显示所有人工资情况

'''


class Person:
    def __init__(self, num, name, salary):
        self.num = num
        self.name = name
        self.salary = salary

    # def setName(self,name):
    #     self.name = name
    # def getName(self):
    #     return self.name
    # def getNum(self):
    #     return self.num
    def count_salary(self):
        return self.salary

    def __str__(self):
        msg = '工号：{}，姓名：{}，工资：{}'.format(self.num, self.name, self.salary)
        return msg


class Worker(Person):

    def __init__(self, num, name, salary, hours, hour_salary):
        super(Worker, self).__init__(num, name, salary)
        self.hours = hours
        self.hour_salary = hour_salary

    def count_salary(self):
        money = self.hours * self.hour_salary
        self.salary += money
        return self.salary


class Saleman(Person):
    def __init__(self, num, name, salary, turnover, commission):
        super(Saleman, self).__init__(num, name, salary)
        self.turnover = turnover
        self.commission = commission

    def count_salary(self):
        money = self.turnover * self.commission
        self.salary += money
        return self.salary


class Manager(Person):
    def __init__(self, num, name, salary,monthly_pay):
        super(Manager, self).__init__(num, name, salary)
        self.monthly_pay = monthly_pay
    def count_salary(self):
        money = self.monthly_pay
        self.salary+= money
        return self.salary


class Salemanger(Person):
    def __init__(self):
        super(Salemanger, self).__init__(num, name, salary)

#每个子类均重写了count_salary()方法
worker = Worker('001','Tom',2000,160,100)
s = worker.count_salary()
print(s)   #160*100+2000=18000
print(worker)  #调用的是Person里的__str__方法

saleman = Saleman('002','lucy',5000,5000000,0.003)
s = saleman.count_salary()
print(s)
print(saleman)