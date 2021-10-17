import json
import time
from multiprocessing import Process,Lock

#需求：10个并发，剩余3张票，抢到一张就减1

def search(i):
    with open('ticket.txt',encoding='utf-8') as f:
        ticket = json.load(f)
    print('%s :当前的余票是%s张'%(i,ticket['count']))

def buy_ticket(i):
    with open('ticket.txt',encoding='utf-8') as f:
        ticket = json.load(f)
    if ticket['count']>0:
        ticket['count'] -= 1
        print('%s买到票了'%i)
    time.sleep(1)
    with open('ticket.txt', mode='w',encoding='utf-8') as f:
        json.dump(ticket,f)

def get_ticket(i,lock):
    search(i)
    with lock:   # 代替acquire和release 并且在此基础上做一些异常处理,保证即便一个进程的代码出错退出了,也会归还钥匙
        buy_ticket(i)


if __name__ == '__main__':
    lock = Lock()     # 互斥锁
    for i in range(10):
        Process(target=get_ticket,args=(i,lock)).start()

        




