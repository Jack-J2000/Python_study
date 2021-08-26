'''
模拟文件上传：
键盘输入上传文件的名称(abc.jpg)，判断文件名是否大于6位以上，扩展名是否是：jpg,gif,png格式
如果不是则提示上传失败，如果名字不满足条件，而扩展名满足条件则随机生成一个6位数字组成的文件名
打印成功上传xxxxxx.png
'''
import random

# file = input('输入上传的文件名：')
# if file.endswith('jpg') or file.endswith('gif') or file.endswith('png') :   #判断字符是否正确
#     t = file.find('.')    #查找位置
#     if len(file[:t])>=6:  #切片
#         print('成功上传%s' %file)
#     else:
#         ran = random.randint(100000,999999)
#         #重新构建名字
#         new_name = str(ran) + file[t:]
#         print('成功上传%s'%new_name)
# else:
#     print('上传失败')

# 随机产生字母和数字的组合  (验证码)  ！！！！！！！！
filename = ''
s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
for i in range(6):
    ran = random.randint(0, len(s) - 1) #对字符串里的字符进行random
    filename += s[ran]
print(filename)

'''
# 用户名或者手机号登录+密码
用户名：全部小写，首字母不能是数字，长度必须6位以上
手机号码 ：纯数字  长度11
密码必须是6位数字

以上符合条件则进入下层验证
判断用户名+密码  正确就登录成功；否则登陆失败
'''
# while True:
#     login = input('请选择登录方式(用户名/手机号码)：')
#     if login=='用户名':
#         name = input('请输入用户名：')
#         password = input('请输入密码：')
#         if name.islower() and name[0].isdigit()==False and len(name)>6 and len(password)==6:
#             print('----------------开始验证...-----------------')
#             print('成功登录！')
#             break
#         else:
#             print('登录失败！')
#
#     elif login=='手机号码':
#         number = input('请输入手机号码：')
#         password = input('请输入密码：')
#         if number.isdigit() and len(number)==11 and len(password)==6:
#             print('--------------开始验证...----------------')
#             print('成功登录！')
#             break
#         else:
#             print('登陆失败！')
#     else:
#         print('格式错误！')

'''
模拟论坛：

'''
msg = input('输入一个议题：')
print('---'*15)
print('以下为回复信息：')
while True:
    name = input('输入用户名：')
    while True:
        comment = input('请输入回复内容：')
        comment = comment.strip()
        if len(comment)!=0:
            if len(comment)<=20:
                #是否存在敏感词汇
                comment = comment.replace('丑陋','**')
                print('{}发表的评论是：\n{}'.format(name,comment))
                break
            else:
                print('不能超出20字！')
        else:
            print('评论内容不能为空！')




