'''
文件操作：
文件上传    网上的电影--->网盘
文件下载    网盘文件--->自己电脑硬盘
保存log

系统函数：
open()
参数：file(文件名)，mode，buffering(缓存)，encoding(编码)
mode分为：r,w --->纯文本
binary(二进制   字节)        rb,wb ---->纯文本，图片，音乐，影像
read：指文件向pycharm输入
write：指pycharm输出给文件

读：
     open(path/filename, 'rt' ) --->返回值：stream (管道)
     container = stream.read() ---->读取管道中的内容
     注意：如果传递的path/filename有误，则会报错：FileNotFoundError

     默认读取方式为，mode = rt  (读取纯文本)
     如果读取图片，则不能使用默认的读取方式，mode = 'rb'  (二进制形式读取)
     read() 读取所有内容
     readline() 每次读取一行内容(每行换行)
     readlines() 读取所有行内容保存在列表里(每行换行)
     readable() 判断是否可读

'''
#读取一个写好的文本文件：D:\python\PyCharm\test.txt    #如果文件里含中文，报错
stream = open(r'D:\python\PyCharm\test.txt') #建立通道的动作；防止转义字符，在文件参数上加r

# container = stream.read() #读出文件
result = stream.readable() #判断该文件是否可读
# result1 = stream.readline() #若读取过该文件，则返回空行

# print(result1)
# print(container)
print(result)

# while True:
#     line = stream.readline()  #每次读取后，出现换行符
#     print(line)
#     if line=='':
#         break

lines = stream.readlines() #必须是没有读取过的文件
print(lines)
for i in lines:
    print(i)

#读图片时，要注意mode
stream = open(r'D:\python\PyCharm\PY.png','rb') #rb指以二进制方式读出

container = stream.read()
print(container)




