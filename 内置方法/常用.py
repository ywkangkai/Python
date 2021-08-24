#evel

#exec 与evel类似

msg = '''
for i in range(0,5):
    print(i)
'''
#exec(msg)

#字典的创建方式
# dic = dict([(1,'1'),(2,'2')])
# #dic =dict(one=1, two=2)
# print(dic)


#zip拉链

l1 = [1,2,3,4,5]
tui = ('太白','B哥','德刚')
s1 = 'abcd'

obj = zip(l1,tui,s1)
for i in obj:
    print(i)
print(list(obj))
'''
(1, '太白', 'a') 列表中的1，tui中的太白，s1中的a
(2, 'B哥', 'b')依次类推
(3, '德刚', 'c')依次类推
'''