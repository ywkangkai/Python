from multiprocessing import Process

import os

def fun():
    print(os.getpid(),os.getppid())

#window中使用进程必须要加上if __name__ == '__main__': 这句话才不会报错
if __name__ == '__main__':
    print('main:',os.getpid(),os.getppid())
    p = Process(target=fun)
    p.start()