import os
import time
from threading import Thread,current_thread,enumerate,active_count

class MyThread(Thread):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        super().__init__()

    def run(self):
        print(self.ident)

t = MyThread(1,2)
t.start()  # 开启线程 才在线程中执行run方法
print(t.ident)