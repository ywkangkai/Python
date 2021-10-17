from threading import Thread

n = 100

def func():
    global n
    n -= 1

t_l = []
for i in range(100):
    t = Thread(target=func)
    t.start()
    t_l.append(t)
for t in t_l:
    t.join()
print(n)