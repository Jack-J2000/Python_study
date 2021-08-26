'''
王者荣耀角色管理

角色：姓名，性别，职业
添加角色
删除角色
修改角色 （支持修改，不能使用元组）
查询角色
显示角色
退出系统
'''
import time
all_role = [] #存放所有角色的容器
print('~~~~~~~~~~~~~~~~~欢迎进入王者荣耀角色管理系统~~~~~~~~~~~~~~~~~')
while True:
    choice = input('请选择功能：\n1.添加角色\n2.删除角色\n3.修改角色\n4.查询角色\n5.显示角色\n6.退出系统')
    if choice=='1':
        print('添加角色：\n')
        name = input('角色名：')
        sex = input('性别：')
        job = input('职业：')
        role = [name,sex,job]
        #添加到all_role
        all_role.append(role)
        print('成功添加{}到王者荣耀系统！\n'.format(name))

    elif choice=='2':
        print('删除角色：\n')
        role_name = input('输入要删除的角色名：')
        for role in all_role:
            if role_name in role:
                answer = input('是否确定删除%s?'% role_name)
                if answer=='是':
                    all_role.remove(role)
                    print('成功删除%s' %role_name)
                    break
                else:
                    break
        else:
            print('本系统不存在角色{}'.format(role_name))

    elif choice == '3':
        print('修改角色模块\n')
        role_name = input('要修改的角色：')
        for role in all_role:
            if role_name in role:
                role.clear()
                rname = input('输入修改后的角色名：')
                rsex = input('输入修改后的性别：')
                rjob = input('输入修改后的职业：')
                role.append(rname)
                role.append(rsex)
                role.append(rjob)
                print('修改成功！')
                break
    elif choice == '4':
        print('查询角色模块\n')
        role_name = input('输入查询的角色名称：')
        for role in all_role:
            if role_name in role:
                print('角色存在，信息如下:')
                print('{}{}{}'.format('名称'.center(10), '性别'.center(10), '职业'.center(10)))
                print(role[0].center(10), end='')
                print(role[1].center(10), end='')
                print(role[2].center(10))
            else:
                print('角色信息不存在！')
    elif choice == '5':
        print('显示所有角色：')
        print('{}{}{}'.format('名称'.center(10),'性别'.center(10),'职业'.center(10)))
        for role in all_role:
            print(role[0].center(10),end='')
            print(role[1].center(10),end='')
            print(role[2].center(10),end='')
            print()
    elif choice == '6':
        print('正在退出系统...')
        time.sleep(3) #表示休眠3秒
        print('成功退出！')
        break
    else:
        print('选择错误！')
