'''
sys模块：
当你导入一个模块，Python解析器对模块位置的搜索顺序是：
1.当前目录
2.如果不在当前目录，Python则会搜索在 shell 变量PYTHONPATH 下的每一个目录
3.如果都找不到，Python会查看默认路径。UNIX下，默认路径一般为/user/local/lib/python/
   模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录
'''
import sys

print(sys.path)  #模块搜索路径
print(sys.version)
print(sys.argv)  #运行程序时的参数，argv是一个列表
n = 0
print(sys.getrefcount(n))
'''
time模块：
1.时间戳  time.time()   #当前时间(秒的形式)
2.time.sleep(3)   #程序至此暂停三秒
3.time.ctime()    #当前时间(年月日时分秒的形式)
4.time.localtime()   #将时间戳转换为元组的形式(当前时间详细信息显示)
5.time.mktime()    #将(时间)元组转为时间戳的形式
6.time.strftime()   #将元组时间 转为字符串形式
7.time.strptime()   #将字符串转为元组方式

其中，1，2，6需重点掌握
'''
import time
t1 = time.time()
print(t1) #程序至此的执行时间

# time.sleep(3) #程序至此暂停3秒

t2 = time.time()
print(t2)

s = time.ctime(t1)  #当前时间
print(s)

#将时间戳转换为元组的形式(当前时间详细信息显示)
loc = time.localtime(t1)
print(loc)
print(loc.tm_hour)  #可调用元组里的具体内容
print(loc.tm_mon)


#将(时间)元组转为时间戳的形式
loc = time.mktime(loc)
print(loc)  #小数点后清零

#将元组时间 转为字符串形式
s = time.strftime('%Y-%m-%d')
print(s)  #以年月日的形式打印
s = time.strftime('%Y-%m-%d %H:%M:%S')
print(s)

#将字符串转成元组的方式
t = time.strptime('2021/9/13','%Y/%m/%d')  #第一个参数为时间字符串，第二个参数为待转换的格式
print(t)


'''
datetime模块：
time  时间  time里的hour second minute 以对象的形式存在
date  日期  date里的year month day 以对象形式存在
datetime  日期和时间  now()
timedelta  时间差      timedelta(day='',week='',...)  结合now()作加减运算得出时间差

'''
import datetime

print(datetime.time.hour)  #返回对象
# print(time.localtime().tm_hour)

d = datetime.date(2021,9,13)
print(datetime.date.month)
print(datetime.date.ctime(d))  #年月日时分秒的形式

print(datetime.date.today())  #输出当前的日期

#时间差
timedel = datetime.timedelta(hours=2)  #定义一个时间差
print(timedel)

now = datetime.datetime.now()  #————>得到当前日期和时间
print(now)
result = now - timedel
print(result)   #当前时间减去2小时

#时间差使用场景！！！
#缓存：数据redis 作为缓存  redis.set(key,value,时间差)  将数据保存多长时间
#会话：session

'''
random模块：


'''
import random
r = random.random()  #得到一个0 ~ 1 之间的随机小数
print(r)

r = random.randrange(1,15,2) #打印一个1~15(不包含15)的随机数，步长为2仅能打印(1,3,5,7,9,11,13)
print(r)

r = random.randint(1,10) #产生一个1~10(可包含10)的随机数
print(r)

list1 = ['Tom','Jack','Lily']
r = random.choice(list1)  #choice里放的是列表，随机打印一个列表中的元素
print(r)

pai = ['红桃K','方片A','梅花5','黑桃6']
random.shuffle(pai)  #将列表元素打乱顺序(执行洗牌的动作)
print(pai)

#验证码 大小写字母与数字组合
def func():
    code = ''
    for i in range(4):
        ran1 = str(random.randint(0,9))
        ran2 = chr(random.randint(65,90))
        ran3 = chr(random.randint(97,122))
        r = random.choice([ran1,ran2,ran3])

        code +=r
    return code
r = func()
print(r)


'''
属于标准库里的：
'''
print(chr(65))  #Unicode码---> str
print(ord('A'))   #str--->Unicode码
print(ord('中'))


'''
hashlib模块：  
加密算法---(md5,sha1,sha256)  单向加密
         ---(base64)    可加密解密
hexdigest()  加密

'''
import hashlib

msg = '哈哈哈'
md5 = hashlib.md5(msg.encode('utf-8'))
print(md5)   #输出为hash 对象 md5
print(md5.hexdigest())  #输出加密后的结果

sha1 = hashlib.sha1(msg.encode('utf-8'))
print(sha1.hexdigest())

sha256 = hashlib.sha256(msg.encode('utf-8'))
print(sha256.hexdigest())

#验证登录密码
password = '123456'
list = []
sha256 = hashlib.sha256(password.encode('utf-8'))
list.append(sha256.hexdigest())

print(list)

# pwd = input('输入密码：')
# sha256 = hashlib.sha256(pwd.encode('utf-8'))  #对密码使用同样的算法进行加密
# pwd = sha256.hexdigest()
# print(pwd)
# for i in list:
#     if pwd == i:
#         print('登录成功！')

'''
第三方模块：pillow(图片处理)  

(在Terminal,命令行)使用pip安装和管理第三方模块：pip install pillow

'''
import requests

response = requests.get('https://www.baidu.com/')
print(response.text)

response1 = requests.get('http://www.baidu.cn/')
print(response1.text)