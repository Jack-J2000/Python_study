'''
元组：与列表类似，不同之处在于元组的元素不能修改（增删改）。
 元组使用小括号()，列表使用方括号[]
 list      列表
 tuple   元组
 list(tuple)   ---->元组转成列表
tuple(list)    ---->列表转成元组
定义：
元组名字 = ()
注意：如果元组里只有一个元素，必须加逗号 ('aa',)
可以使用下标+切片

'''
t1 = ()
print(type(t1))

t2 = ('jsy')  #此时不表示元组
print(type(t2))
print(t2)

t3 = ('jsy',) #如果元组里只有一个字符串，需要在字符串后加逗号，才表示元组
print(type(t3))
print(t3)

#下标和切片    字符串，列表，元组使用方法类似 ---->注意下标越界
t4 = ('aa','bb','cc','aa')
print(t4[0])
print(t4[::-1]) #倒序输出
print(t4.count('aa')) # 元素计数
print(t4.index('aa')) #从左向右找字符串
index = t4.index('aa',1,4) #在索引1号位和索引4号位之间找'aa'   ；不包括4号位
print(index)

l = len(t4) #求元组长度
print(l)

#in 和 not in
if 'cc' in t4:
    print('存在')
else:
    print('不存在')

#支持for...in循环
for i in t4:
    print(i)

#元组列表转换，然后就可以往里面添加元素了
t4 = ()
t4 = list(t4)
print(type(t4))

t4.append('jsy')
print(t4)