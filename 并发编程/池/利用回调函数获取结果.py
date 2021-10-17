# 回调函数 : 效率最高的
import time,random
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor

def func(a,b):
    print(current_thread().ident,'start',a,b)
    time.sleep(random.randint(1,4))
    print(current_thread().ident,'end',a)
    return (a,a*b)

def print_func(ret):       # 异步阻塞
    print(ret.result())

if __name__ == '__main__':
    tp = ThreadPoolExecutor(4)
    futrue_l = {}
    for i in range(20):         # 异步非阻塞的
        ret = tp.submit(func,i,b=i+1)
        ret.add_done_callback(print_func)  # ret这个任务会在执行完毕的瞬间立即触发print_func函数,并且把任务的返回值对象传递到print_func做参数
        # 异步阻塞 回调函数 给ret对象绑定一个回调函数,等待ret对应的任务有了结果之后立即调用print_func这个函数
        # 就可以对结果立即进行处理,而不用按照顺序接收结果处理结果