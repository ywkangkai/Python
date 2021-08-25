import re

#ret = re.findall('\d','54564asdasd78asd')  #匹配到所有结果

# ret = re.findall('7(\d)\d','74564asdasd785sd') #匹配[4,8] 有分组匹配分组中的类容

#ret = re.findall('<\w+>(\w+)</\w+>','<h1>74564asdasd785sd</h1>') #有分组表示提取分组中的类容
ret = re.findall('7(?:\d)(\d)','74564asdasd785sd')  #?:可以取消该分组的优先级，不会提取该分组中的内容
                                                       #如果不取消优先级结果为[('4', '5'), ('8', '5')]，取消后['5', '5']
print(ret)

