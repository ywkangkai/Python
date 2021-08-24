def fun():
    yield 1
    yield 2
    yield 3

ret = fun()
print(next(ret))
print(next(ret))

'''
:return与yield的区别
return用于结束函数
yield是生成器不是函数，生成器函数中可以存在多个yield，一个yield对应一个next
'''