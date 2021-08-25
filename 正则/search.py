import re

#ret = re.search('\d','54564asdasd78asd')  #找到第一个结果就返回
#ret = re.search('7(\d)\d','74564asdasd785sd') #匹配到第一个内容，但是给group传参可以获取具体低几个内容

ret = re.search('(<\w+>)(\w+)(</\w+>)','<h1>74564asdasd785sd</h1>')
print(ret.group()) #整体
print(ret.group(1)) #第二个分组

a = '2-3*(5+6)'
b = re.search('(\d-\d)\*(\(\d\+\d\))',a)
print(b.group())
print(b.group(1))
print(b.group(2))