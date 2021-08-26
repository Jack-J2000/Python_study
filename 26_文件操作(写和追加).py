'''
(write)写：相当于用Pycharm往文件里写内容，覆盖原文件内容
       mode 是  ‘w’  表示写操作
       mode 是  'a'  表示接原文件后写入，追加操作
writelines(Iterable)  没有换行效果；需加换行符\n

'''
stream = open(r'D:\python\PyCharm\test1.txt','a')

result = stream.writable() #判断文件的可修改性
print(result)

s = '''
你好！
      欢迎来到德莱联盟！
'''
update = stream.write(s)
print(update)  #打印出数字
update1 = stream.write('德莱文-SSS\n')
print(update1)

stream.writelines(['德莱厄斯—SSS\n','卡特琳娜\n'])

stream.write('赛恩')
stream.close() #每次写操作结束后要关闭流，关闭之后无法写入