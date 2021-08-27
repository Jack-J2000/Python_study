'''
语法错误和异常

异常：程序运行的时候报出来的，XXXError
异常处理：
try:
      可能出现异常的代码
except:
      如果有异常执行的代码
finally:
      无论是否有异常都会被执行的代码
'''


def func():
    try:
        n1 = int(input('输入第一个数字：'))
        n2 = int(input('输入第二个数字：'))
        result = input('输入一个运算符(+ - * /)：')
        if result =='+':
            sum = n1 + n2
            print('和是：',sum)
        elif result=='-':
            sub = n1-n2
            print('差是：',sub)
        elif result =='*':
            mul = n1*n2
            print('积是：',mul)
        elif result=='/':
            div = n1/n2
            print('商是：',div)
        else:
            print('请输入正确的运算符！')
    except ValueError:
        print('必须输入数字！')
    except ZeroDivisionError:
        print('除数不能为0！')


func()

