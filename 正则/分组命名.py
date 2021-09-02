import re

ret = re.search('(<\w+>)(?P<number>\w+)(</\w+>)','<h1>74564asdasd785sd</h1>')
#命名规则
#(?P<变量>)  ret.group('变量名')
print(ret.group('number')) #通过名字直接获取想要的匹配的分组

