import os
import time,random
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
def func(a,b):
    print(os.getpid(),'start',a,b)
    time.sleep(random.randint(1,4))
    print(os.getpid(),'end')
    return a*b

if __name__ == '__main__':
    tp = ProcessPoolExecutor(4)
    futrue_l = {}
    for i in range(20):         # 异步非阻塞的
        ret = tp.submit(func,i,b=i+1)
        futrue_l[i] = ret
        # print(ret.result())   # Future未来对象   result()内置方法，获取执行对象结果的返回值
    for key in futrue_l:       # 同步阻塞的
        print(key,futrue_l[key].result())