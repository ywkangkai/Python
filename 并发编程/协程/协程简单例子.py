from gevent import monkey
monkey.patch_all() #要使用协程这两句话必须要写在顶部
import gevent
import time
def func():    # 带有io操作的内容写在函数里,然后提交func给gevent
    print('start func')
    gevent.sleep(1)
    time.sleep(1)
    print('end func')

g1 = gevent.spawn(func)
g2 = gevent.spawn(func)
g3 = gevent.spawn(func)
gevent.joinall([g1,g2,g3])  #只有阻塞的时候，协程才会跳入到去执行函数  场景：一个请求需要等会很久才返回，可以利用协程在等待请求的时候去执行其他逻辑

# g1.join()   # 阻塞 直到协程g1任务执行结束
# g2.join()   # 阻塞 直到协程g1任务执行结束
# g3.join()   # 阻塞 直到协程g1任务执行结束

