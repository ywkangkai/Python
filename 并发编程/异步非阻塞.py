import os
import time
from multiprocessing import Process

def func(name,age):
    print('%s start'%name)
    time.sleep(1)
    print(os.getpid(),os.getppid(),name,age)

if __name__ == '__main__':
    # 只会在主进程中执行的所有的代码你写在name = main下
    print('main :',os.getpid(),os.getppid())
    arg_lst = [('alex',84),('太白', 40),('wusir', 48)]
    for arg in arg_lst:
        p = Process(target=func,args=arg)
        p.start()  # 异步非阻塞：启动一个程序不需要等待结果(异步)，但可以继续执行后续程序(非阻塞)








