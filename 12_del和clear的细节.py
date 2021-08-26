# 删除del()
list1 = ['1', '2', '3', '4', '5', '6']
del list1[3]
print(list1)

list1.pop(3)
print(list1)

list1.clear()  # 清空列表
print(list1)

list2 = ['赛恩', '泰达米尔', '维嘉', '维嘉', '莫德凯撒']
list1 = list2  # !!!!!!!!!!!!!!当列表1 = 列表2 ，表示它们的地址一样，其中一个改变，另一个也会改变

# del list2  #把list2的指针断掉，这个列表消失了，无法clear
# print(list1)
list2.clear()
print(list1)  # 对list2清空,相当于把地址中的值清除。而list1和list2地址一样，故都没有值

a = 'hello'
b = a
c = a
print(id(b),id(c),id(a)) #其地址一样
del a #删去a的指针，不存在a，也就更加没有所对应的值
print(b, c)

a = ['1','2',3,4]
b = a
c = a
# del a   #同上 一样的效果
b.clear()
print(a,c)
