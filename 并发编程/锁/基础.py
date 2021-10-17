import time
from multiprocessing import Process,Lock
def fun(i,lock):
    lock.acquire() #拿钥匙，
    print('被锁起来的代码',i)
    time.sleep(2)
    lock.release()  #还钥匙

if __name__=='__main__':
    lock = Lock()
    for i in range(0,10):
        p = Process(target=fun,args=(i,lock))
        p.start()
