import re

ret = re.search('<(?P<tag>\w+)>.*?</(?P=tag)>' ,'<abc>74564asdasd785sd</abc>') #表示前后标签要为一致
#命名规则
#(?P<变量>)  ret.group('变量名')
print(ret.group()) #通过名字直接获取想要的匹配的分组

