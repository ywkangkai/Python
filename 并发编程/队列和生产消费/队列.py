import random
from multiprocessing import Queue,Process
import time

def consumer(q, name):
    while True:
        food = q.get()
        if food:
            print(f'{name}吃了{food}')
        else:
            break

def producer(q, name, food):
    for i in range(10):
        print(f'{name}生产了水果{food}')
        time.sleep(random.random())
        q.put(food)
if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=producer, args=(q,'kk1', '香蕉'))
    p1.start()

    p2 = Process(target=producer, args=(q, 'yy1', '苹果'))
    p2.start()

    c = Process(target=consumer, args=(q, '老王'))
    c.start()

    p1.join()
    p2.join()

    q.put(None)