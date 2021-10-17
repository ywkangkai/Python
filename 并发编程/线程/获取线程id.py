import os
import time
from threading import Thread,current_thread,enumerate,active_count
def func(i):
    print('start%s'%i,current_thread().ident)
    time.sleep(1)
    print('end%s'%i)
if __name__ == '__main__':
    tl = []
    for i in range(10):
        t = Thread(target=func,args=(i,))
        t.start()
        print(t.ident,os.getpid())
        tl.append(t)
    print(enumerate(),active_count())
    for t in tl:t.join()
    print('所有的线程都执行完了')