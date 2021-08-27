# 持久化保存：文件
# list ，元组，字典 ---->内存里，不属于持久化保存
# 存储数据  D:\测试(test)文件夹\Test1
# 用户注册
def register():
    username = input('输入用户名：')
    password = input('输入密码：')
    repassword = input('确认输入密码：')

    if password == repassword:
        # 保存信息
        with open(r'D:\测试(test)文件夹\Test1\user.txt', 'a') as wstream:
            wstream.write('{} {}\n'.format(username, password))
            # wstream.writelines([username+' ',password+'\n'])
        print('注册成功！')
    else:
        print('两次输入密码不一致，请再次尝试注册！')
        register()


def login():
    username = input('输入用户名：')
    password = input('输入密码：')

    if username and password:
        with open(r'D:\测试(test)文件夹\Test1\user.txt', 'r') as rstream:
            while True:
                user = rstream.readline()
                input_user = '{} {}\n'.format(username, password)

                if input_user == user:
                    print('登录成功！')
                    show_books()
                    add_books()
                    break
            else:
                print('用户名或密码错误，请重新登录！')
                login()


def show_books():
    print('------图书馆里的书有------')
    with open(r'D:\测试(test)文件夹\Test1\books.txt', encoding="utf-8") as  rstream:
        booklist = rstream.readlines()
        for book in booklist:
            print(book, end='')


def add_books():
    choice = input('请选择你要借阅的书籍：')
    choice = choice + '\n'
    with open(r'D:\测试(test)文件夹\Test1\books.txt', encoding="utf-8") as  rstream:
        booklist = rstream.readlines()
        print(booklist)
        if choice in booklist:
            print('借阅成功！')
        else:
            print('查无此书！')


# register()
# show_books()
login()
