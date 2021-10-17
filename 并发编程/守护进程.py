# import time
# from multiprocessing import Process
#
# def son1():
#     while True:
#         print('--> in son1')
#         time.sleep(1)
#
# def son2():   # 执行10s
#     for i in range(10):
#         print('in son2')
#         time.sleep(1)
#
# if __name__ == '__main__':    # 3s
#     p1 = Process(target=son1)
#     p1.daemon = True    # 表示设置p1是一个守护进程
#     p1.start()
#     p2 = Process(target=son2,)
#     p2.start()
#     time.sleep(3)
#     print('in main')


# 主进程会等待所有的子进程结束,是为了回收子进程的资源
# 守护进程会等待主进程的代码执行结束之后再结束
# 主进程的代码什么时候结束,守护进程就什么时候结束,和其他子进程的执行进度无关

# 要求守护进程p1必须在p2进程执行结束之后才结束
# import time
# from multiprocessing import Process
#
# def son1():
#     while True:
#         print('--> in son1')
#         time.sleep(1)
#
# def son2():   # 执行10s
#     for i in range(10):
#         print('in son2')
#         time.sleep(1)
#
# if __name__ == '__main__':    # 3s
#     p1 = Process(target=son1)
#     p1.daemon = True    # 表示设置p1是一个守护进程
#     p1.start()
#     p2 = Process(target=son2,)
#     p2.start()
#     time.sleep(3)
#     print('in main')
#     p2.join()    # 等待p2结束之后才结束

# 等待p2结束 --> 主进程的代码才结束 --> 守护进程结束

# Process类拾遗
    # 开启进程的另一种方法
        # 面向对象的方法,通过继承和重写run方法完成了启动子进程
        # 通过重写init和调用父类的init完成了给子进程传参数
    # Process类的一些其他方法\属性
        # name pid ident daemon
        # terminate() isalive()
    # 守护进程
        # 在start一个进程之前设置daemon = True
        # 守护进程会等待主进程的代码结束就立即结束
            # 为什么守护进程只守护主进程的代码?而不是等主进程结束之后才结束
                # 因为主进程要最后结束,为了给守护进程回收资源
            # 守护进程会等待其他子进程结束么? 不会
# 进程同步 -- Lock 锁  *****
    # 进程之间数据安全的问题

# 进程之间通信 -- 队列 ***
# 进程之间的数据共享 -- Manager *