'''
1.正则表达式的定义
正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符，
及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑。

正则表达式是对字符串（包括普通字符（例如，a到z之间的字母）和特殊字符（称为“元字符”））操作的一种逻辑公式，
就是用事先定义好的一些特定字符，及这些字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑。
正则表达式是一种文本模式，模式描述在搜索文本时要匹配的一个或多个字符串。

正则表达式，又称正规表达式，正规表示法，正规表达式，规则表达式，常规表达式（英文：Regular Expression，
在代码中常简写为regex,regexp或RE），是计算机科学的一个概念。正则表达式使用单个字符串来描述，匹配一系列及匹配某个句法规则的字符串。
在很多文本编辑器里，正则表达式通常被用来检索，替换那些匹配某个模式的文本。
Regular Expression的 “Regular” 一般被译为“正则”，“正规”，“常规”。此处的“Regular” 即是“规则”，
“规律”的意思，Regular Expression即“描述某种规则的表达式”之意。

2.正则表达式的作用和特点
给定一个正则表达式和另一个字符串，可达到以下目的：
1.给定的字符串是否符合正则表达式的过滤逻辑（称作：匹配）
2.可以通过正则表达式，从字符串中获取我们想要的特定部分

正则表达式的特点是：
1.灵活性，逻辑性和功能性很强
2.可以迅速的用极简单的方式达到字符串的复杂控制
3.对于刚接触的人来说，比较晦涩难懂

使用场景：
如何判断一个字符串是手机号呢？
判断邮箱为163或者126的所有邮件地址

假设我现在在写一个爬虫程序(虽然我还没有学到)，我得到了一个网页的HTML源码。其中有一段
<html> <body> <h1>hello world<h1> </body> </html>
我想要将这个hello world提取出来，但这时只会用字符串进行处理：

s = "<html> <body> <h1>hello world<h1> </body> </html>"
start_index = s.find('<h1>')

Python里的re模块(正则相关)
正则预定义
\A：表示从字符串的开始处进行匹配
\Z：表示从字符串的结束处匹配，如果存在换行，只匹配到换行前的结束字符串
\b：匹配一个单词边界，也就是指单词和空格间的位置。例如，’py\‘ 可以匹配”python“中的'py'，但是不能匹配”openpyxl“ 中的'py'
\B：匹配非单词边界(即单词内部的字母)。'py\b'可以匹配"openpyxl"中的'py'，但不能匹配"python"中的'py'
\d：匹配任意的数字，等价于 [0~9]
\D：匹配任意非数字字符，等价于 [^\d]
\s：匹配任意空白字符，等价于 [ \t \n \f \r]
\S：匹配任意非空白字符，等价于 [^\s]
\w：匹配任意字母数字及下划线，等价于 [a-z  A-Z  0-9]
\W：匹配任意非字母数字及下划线，等价于 [^\w]
\\：匹配原义的反斜杠\

'''
# 正则表达式可用来  快速的  检验号码格式的准确性

'''
match(从头匹配)  可以拿一个正则模板同字符串头部进行匹配；匹配成功返回match对象，否则返回值为空


'''
import re

msg = '玛尔扎哈赛恩德莱厄斯'

pattern = re.compile('玛尔扎哈')
print(pattern)
result = pattern.match(msg)  # 没有匹配到时，值为空
print(result)

###使用正则re模块的方法：match
s = '泰达米尔卡特琳娜德莱文'

result = re.match('泰达米尔', s)  # 第一个参数为为正则式，第二个参数为字符串
print(result)  # match 头部匹配

###使用正则re模块的方法：search
result = re.search('卡特', s)  # 第一个参数为为正则式，第二个参数为字符串
print(result)  # search  查找匹配，找到一个后返回
print(result.span())  # 返回匹配到的字符串位置

print(result.group())  # 提取到匹配的内容

'''
#正则符号（量词）
.    #用于匹配除换行符(\n)之外的所有字符
^    #用于匹配字符串的开始，即行首
$    #用于匹配字符串的末尾(末尾如果有换行符\n，就匹配\n前面的那个字符)，即行尾
*    #用于将前面的模式匹配0次或多次(贪婪模式，即尽可能多的匹配)   >=0
+    #用于将前面的模式匹配1次或多次(贪婪模式)   >=1
?    #用于将前面的模式匹配0次或1次(贪婪模式)  0，1
*?，+?，??    #即上面三种特殊字符的非贪婪模式(尽可能少的匹配)
{m}     #用于验证将前面的匹配m次
{m.}    #用于验证将前面的匹配m次或多次(>=m)
{m,n}     #用于将前面的模式匹配m次到n次(贪婪模式)，即最小匹配m次，最多匹配n次
{m,n}?    #即上面{m,n}的非贪婪版本

[]    #用于标示一组字符，如果^是第一个字符，则标示的是一个补集。比如[0-9]表示所有的数字，[^0-9]表示除了数字外的字符
|    #比如A|B，用于匹配A或B
(...)   #用于匹配括号中的模式，可以在字符串中检索或匹配我们所需要的内容。

'''
# 复杂字符串序列
msg = 'a2bc5d98s iui1200'

result = re.match('[a-z][0-9][a-z]', msg)
print(result.group())

result = re.findall('[a-z][0-9][a-z]', msg)  # findall 找到所有匹配的字符
print(result)  # 以列表形式返回

# a7a  a88a a7878a a78787878a    中间是数字，被字母包裹
msg = 'a7aa88aa7878aa78787878a'

result = re.findall('[a-z][0-9]+[a-z]', msg)
print(result)

##qq 号码验证  5~11  纯数字，没有字母 开头不为0
qq = '25420745800'
result = re.match('[1-9][0-9]{4,10}$', qq)  # 使用$来指明尾部
print(result)

##验证用户名  用户名可以是字母或者数字，不能是数字开头，用户名长度必须6位以上[0-9a-zA-Z]

n = 'jj001admin'
result = re.match('[a-zA-Z][0-9a-zA-Z]{5,}$', n)  # 由于验证的是一个整体单位
print(result)

msg = 'aa.py as.txt jkl.py sd.png km.py'
result = re.findall(r'\w+.py\b', msg)
print(result)

'''
总结：
    . 任意字符除(\n)
    ^  开头
    $  结尾
    [] 范围 [abc]  [a-z]  [a-z]
    
    正则预定义：
    \s 空白
    \b 边界
    \d 数字
    \w 字母+_
    
    大写为取反
    \S  非空格   
    \D  非数字
    量词：
    * >=0
    + >=1
    ? 0,1
'''
####案例
# 匹配数字 0-100 之间
n = '100'

result = re.match(r'[1-9]?\d?$|100$', n)
print(result)

# 小括号里字符串(或者时)可作整体，而方括号里(或者时)作为单个字符
# 验证邮箱 163 126 qq
email = '321456987@qq.com'
result = re.match('\w{5,20}@(qq|126|163)\.(com|cn)$', email)
print(result)

##不是以4，7结尾的手机号码(11位)
phone = '12345678910'
result = re.match('1\d{9}[0-35-689]', phone)
print(result)

# 分组 (爬虫相关)
phone = '010-12345678'
result = re.match('(\d{3}|\d{4})-(\d{8}$)', phone)
print(result)

# 分别提取
print(result.group(1))  # 输出第一组
print(result.group(2))  # 输出第二组
print(result.group())  # 输出全部

##标签(爬虫相关)
msg = '<html>asd</html>'
msg1 = '<h1>hello</h1>'

result = re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>$', msg1)
print(result)
print(result.group(1))

# number   \1是引用第一组的内容
result = re.match(r'<([0-9a-zA-Z]+)>(.+)</\1>$', msg1)
print(result)
print(result.group(1))
print(result.group())

#
msg = '<html><h1>asdasd</h1></html>'
result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$', msg)
print(result)
print(result.group(1))
print(result.group(2))
print(result.group(3))

import re

# 起名的方式  使用 ?P 对标签起名   (?P<名字>正则)   (?P = 名字)
msg = '<html><h1>asd</h1></html>'
result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>', msg)
print(result.group())
print(result)

'''
分组：()    result.group(1)  获取组中的匹配内容

不需要引用分组内容：
result = re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>$',msg1)
引用分组匹配内容：
    1.number
    result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$',msg)
    2.(?P<name>正则内容)  (?P=name)
    result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>',msg)
    
re模块函数：
    match
    search
    findall
    sub(正则表达式，'新内容',string)
    split  在字符串中搜索如果遇到，就会分割，将分割出的内容保留在列表中
'''


def func(temp):
    num = temp.group()
    num1 = int(num) + 1
    return str(num1)
result = re.sub(r'\d+', '90', 'java:95,pathon:99')  # 替换后面字符串满足条件的内容
print(result)

result = re.sub(r'\d+', func, 'java:95,pathon:99')  # 利用函数+正则来实现对字符串内容的修改
print(result)

result = re.split('[:,]','java:95,pathon:99')  #被切除的元素就没有了
print(result)

'''
贪婪模式：
Python里的数量词默认是贪婪的(在少数语言里可能默认为非贪婪)
总是尝试匹配更多的字符；非贪婪是尽可能的匹配更少的内容
[] 范围
() 一组

'''
#默认为贪婪的，\d+ 会一直匹配数字
#将贪婪模式变为非贪婪模式  \d+?
msg = 'asdasddsa123'
result = re.search(r'dsa(\d+?)',msg)
print(result)

path = '<img class="hg-qrcode-img" src="https://hellogithub.com/img/hg-qrcode.jpg">'
result = re.match(r'<img class="hg-qrcode-img" src="(.+)"',path)
print(result.group(1))

image_path = result.group(1)
import requests
response = requests.get(image_path)

# with open('aa.jpg','wb') as wstream:
#         wstream.write(response.content)



