
list1 = ['123','1321','asd','fgd',5,6]

###列表删除#####
list.insert(1,'asd') # 索引1后增加asd

list.pop(1) #删除索引1的元素并会返回删除的值

list1.remove('asd') #如果有多个asd的同名元素只会删除第一个

list1.clear() #清空列表


del list1[2] #按索引删

del list1[::2]  #按切片删除


#获取值的索引
print(list1.index('asd'))