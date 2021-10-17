import os
import time
from threading import Thread
def func(i):
    print('start%s'%i)
    time.sleep(1)
    print('end%s'%i)
if __name__ == '__main__':
    tl = []
    for i in range(10):
        t = Thread(target=func,args=(i,))
        t.start()
        tl.append(t)
    for t in tl:t.join()
    print('所有的线程都执行完了')
