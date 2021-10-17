import os
import time
from multiprocessing import Process

def func(name,age):
    print('给%s 发送邮件'%name)
    time.sleep(1)
    print('发送完毕')

if __name__ == '__main__':
    # 只会在主进程中执行的所有的代码你写在name = main下

    arg_lst = [('alex',84),('太白', 40),('wusir', 48)]
    plist = []
    for arg in arg_lst:
        p = Process(target=func,args=arg)
        p.start()
        plist.append(p)
    for p in plist:
        p.join()  # join为同步阻塞，需要等待程序执行出结果后才能继续执行后续代码
    print('所有邮件发送完毕')







