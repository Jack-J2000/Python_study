'''
文件的复制：(读写操作的综合使用)
原文件 D:\python\PyCharm\PY.png
目标文件 D:\python\PyCharm\test\PY.png

在写操作时：with 结合 open使用，可以帮我们自动释放资源
'''

# stream = open('D:\python\PyCharm\PY.png',rb)

# with open('D:\python\PyCharm\PY.png','rb') as rstream:
#     container = rstream.read()  #读取文件内容
#
#     with open(r'D:\python\PyCharm\test\PY.png','wb') as wstream:
#         wstream.write(container) #写入
# print('文件复制完成！')


'''
os模块(operatng system)： 
os.path  
os.path.dirname(__file__)   #获取当前文件所在的文件目录（绝对路径）
os.path.join(path,'')   #返回一个拼接后的新路径
'''
import os

print(os.path)
path = os.path.dirname(__file__)  # 当前文件绝对路径
print(path)
print(type(path))
# print(os.path.dirname(__file__))   #打印当前文件绝对路径

result = os.path.join(path, 'PY.png')  # 添加完成后，需有参数接住返回值
print(result)

with open(r'D:\python\PyCharm\PY.png', 'rb') as rstream:
    container = rstream.read()  # 读取文件内容
    file = rstream.name  # 获取读取文件的路径
    filename = file[file.rfind('\\') + 1:]  # 截取文件名
    print(filename)

    path = os.path.dirname(__file__)
    result = os.path.join(path, 'PY.png')
    with open(result, 'wb') as wstream:
        wstream.write(container)  # 往当前目录下写入
print('文件复制完成！')

'''
获取路径问题（os.path）：
absolute 绝对路径
相对路径是以当前文件为参照点，往上级或下级的递进
'''
r = os.path.isabs('D:\python\PyCharm\PY.png')  # 判断是否为绝对路径
print(r)

r = os.path.isabs('../image/PY.png')  # 表示返回到上一级，找与上一级同级的image下的PY.png
print(r)

r = os.path.isabs('image/PY.png')  # 表示找与当前文件同级的image下的PY.png
print(r)

# 获取当前文件夹的路径
path = os.path.dirname(__file__)
print(path)

# 通过相对路径得到绝对路径
path = os.path.abspath('PY.png')
print(path)

# 获取当前文件的绝对路径
path = os.path.abspath(__file__)
print(path)

#获取当前文件夹路径
path = os.getcwd()
print(path)

#os.path
path = r'D:\python\PyCharm\Study-project\Python-project\27_文件的复制和OS模块.py'
result = os.path.split(path)    #切一刀，返回一个元组，第一个元素是目录，第二个元素是文件名
print(result)
print(result[1]) #文件名

result = os.path.splitext(path) #分割文件与文件扩展名
print(result)
print(result[1]) #文件扩展名

result = os.path.getsize(path)
print(result) #返回字节个数

result = os.path.exists('D:\测试(test)文件夹\PY.png')
print(result)

result = os.path.dirname('D:\测试(test)文件夹\PY.png')
print(result)

'''
dirname()
join()
listdir()  列出文件夹下的文件名；使用时os.listdir()
split()
splitext()
getsize()

isabs()
isfile()
isdir()

exists()
mkdir()
rmdir()   删文件夹
remove() 删文件
chdir()  切换目录
'''
result = os.path.join(os.getcwd(),'file') #在当前文件目录下，加入文件file
print(result)

result = os.listdir(r'D:\python\PyCharm\Study-project\Python-project')  #返回指定目录下的所有文件和文件夹，保存到列表里
print(result)

if not os.path.exists('D:\python\PyCharm\Study-project\Python-project\code'):
    os.mkdir('D:\python\PyCharm\Study-project\Python-project\code')
else:
    os.rmdir('D:\python\PyCharm\Study-project\Python-project\code')

#mkdir创建文件夹操作  文件夹存在时报错，没有返回值
# f = os.mkdir('D:\python\PyCharm\Study-project\Python-project\code')
# print(f)

#rmdir 删除 空文件夹  操作，文件夹不存在时报错，没有返回值
# f = os.rmdir('D:\python\PyCharm\Study-project\Python-project\code')
# print(f)

   # ##删除一个文件夹及其所含文件###
# path = ''  #文件夹路径
# filelist = os.listdir(path)  #将该文件夹下的文件放在一个列表里
# for file in filelist:
#     filepath = os.path.join(path,file)   #拼接文件的路径
#     os.remove(filepath)                  #删除文件
# else:
#     os.rmdir(path)                     #删除文件夹

path = os.getcwd()   #返回当前文件夹的路径
print(path)
f = os.chdir('D:\python')   #切换目录
print(f)

'''
os模块下的方法：
os.getcwd()
os.mkdir()
os.rmdir()
os.listdir()
os.remove()
os.chdir()   
写一个函数，完成复制文件的功能
'''
src_path = r'D:\python\PyCharm\test'
target_path = r'D:\测试(test)文件夹'
def copy(src,target):
    if os.path.isdir(src) and os.path.isdir(target):
        filelist = os.listdir(src)
    for file in filelist:
        filepath = os.path.join(src,file)
        targetfile = os.path.join(target,file)
        with open(filepath,'rb') as rstream:
            container = rstream.read()
            with open(targetfile,'wb') as wstream:
                wstream.write(container)
    else:
        print('复制完成！')

copy(src_path,target_path)
