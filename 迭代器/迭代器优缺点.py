'''
优点
    节省内存
缺点
    速度慢
'''

s1 = 'asda'
obj = iter(s1)
print(next(obj))
print(next(obj))



#使用迭代器会记住上一次循环后的位置，注意有些场景可以用
li = [11,22,33,44,55,66,77,88,99]
obj = iter(li)
for i in range(0,3):
    print(next(obj))
print('会记住上一次位置')
for i in range(0,3):
    print(next(obj))
