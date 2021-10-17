from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from threading import current_thread
import time
def func(a,b):
    print(current_thread().ident, '开始',a,b)
    time.sleep(2)
    print(current_thread().ident, '结束',a,b)

tp = ThreadPoolExecutor(4)  #会默认启动4个进程
for i in range(20):  #一个线程处理一次循环，因为上面睡了2秒，所以需要4个线程，如果不睡2秒，或许1-2个线程可以完成20次循环
    tp.submit(func,i,2)