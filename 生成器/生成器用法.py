def gen_fun():
    for i in range(0,5000):
        yield f'{i}号'

ret = gen_fun()
for i in range(0,200):
    print(next(ret))