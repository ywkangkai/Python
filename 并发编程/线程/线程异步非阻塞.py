from threading import Thread,current_thread,enumerate,active_count
import time

def func(i):
    print('start%s'%i,current_thread().ident)
    time.sleep(1)
    print('end%s'%i)
if __name__ == '__main__':
    for i in range(10):
        Thread(target=func,args=(i,)).start()
    print('所有的线程都执行完了')