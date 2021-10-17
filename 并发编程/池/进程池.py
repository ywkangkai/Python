from concurrent.futures import ProcessPoolExecutor
from threading import current_thread
import time,os
def func(a,b):
    print(os.getpid(), '开始',a,b)
    time.sleep(2)
    print(os.getpid(), '结束',a,b)


if __name__ == '__main__':
    tp = ProcessPoolExecutor(4)
    for i in range(20):
        tp.submit(func,i,2)