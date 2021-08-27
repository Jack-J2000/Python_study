'''
语法错误和异常
object--->BaseException---->Eception---->以树状型分支的各种Error
异常：程序运行的时候报出来的，XXXError，也是类的形式
          可以用级别高的异常来作出包括一系列异常的反应动作
          当出现异常时，程序自动自上向下的寻找适合的exception，进而执行里面的动作
          如果是多个except，异常类型的顺序应该注意，最大的Except要放在最下面
格式：
try:
      可能出现异常的代码
except:
      如果有异常执行的代码
[finally]:
      无论是否有异常都会被执行的代码

情况1：
try:
      可能出现异常的代码
except 异常类型1:
      如果有异常执行的代码
except 异常类型2:
       如果有异常执行的代码

情况2：获取Exception的错误原因
try:
     可能出现异常的代码
except Exception as err:
      print(err)

情况3：
try:
      可能出现异常的代码
except 异常类型1:
      pass
except 异常类型2:
       如果有异常执行的代码
else:
       如果try中没有发生异常则进入的代码
注意：如果使用else，则在try代码范围内不能出现return

情况4：
try:
    pass
except:
    pass
finally:
    无论是否有异常都会被执行的代码（比如无论是否出现异常都要关闭管道）
'''


# def func():
#     try:
#         n1 = int(input('输入第一个数字：'))
#         n2 = int(input('输入第二个数字：'))
#         result = input('输入一个运算符(+ - * /)：')
#         if result =='+':
#             num = n1 + n2
#             print('和是：',num)
#         elif result=='-':
#             num = n1-n2
#             print('差是：',num)
#         elif result =='*':
#             num = n1*n2
#             print('积是：',num)
#         elif result=='/':
#             num = n1/n2
#             print('商是：',num)
#         else:
#             print('请输入正确的运算符！')
#
#         with open(r'D:\测试(test)文件夹\Test1\result.txt','w') as wstream:
#             wstream.write('结果是:{}'.format(num))
#         with open(r'D:\测试(test)文件夹\Test1\result.txt') as rstream:
#             result = rstream.read()
#             print(result)
#
#     except ValueError:
#         print('必须输入数字！')
#     except ZeroDivisionError:
#         print('除数不能为0！')
#     except FileNotFoundError:
#         print('在D:\测试(test)文件夹\Test1下没有找到result文件')
#     except Exception as err: #Exception应该放在代码的下部分，因为它的权力很大
#         print('出错了！',err)
#
# func()

def func():
    stream = None
    try:
        stream = open(r'D:\测试(test)文件夹\Test1\books.txt', encoding='utf-8')
        print(stream)
        container = stream.read()
        print(container)
        return 1    #遇到finally时不会立刻返回
    except Exception as err:
        print(err)
        return 2
    finally:
        print('-----finally-----')
        if stream:  # 如果stream占用内存
            stream.close()
        return 3  #最终还是要返回finally的值


x = func()  #最终返回3，由于finally优先级高于return
print(x)

'''
抛出异常（自定义异常）：raise

'''
#注册函数 用户名必须大于6位
def register():
    username = input('请输入用户名：')
    if len(username)<6:
        raise Exception('用户长度必须6位以上')
    else:
        print('输入的用户名是：',username)
register()

