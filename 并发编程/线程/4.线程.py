# 线程 : 数据隔离,资源分配的最小单位,可以利用多核,操作系统调度,数据不安全,开启关闭切换时间开销大
    # multiprocessing 如何开启进程 start join
    # 进程有数据不安全的问题 Lock (抢票的例子)
    # 进程之间可以通信ipc:
        # 队列(安全) 管道(不安全)
            # 生产者消费者模型
        # 第三方工具
    # 进程之间可以通过Manager类实现数据共享(不需要会写代码)
    # 一般情况下我们开启的进程数不会超过cpu个数的两倍
# 线程(80%)
    # 什么是线程 :能被操作系统调度(给CPU执行)的最小单位
    # 同一个进程中的多个线程同时被CPU执行??? 可能
    # 数据共享,操作系统调度的最小单位,可以利用多核,操作系统调度,数据不安全,开启关闭切换时间开销小

# 在CPython中的多线程 - 节省io操作的时间
    # gc 垃圾回收机制 线程
        # 引用计数 +分代回收
    # 全局解释器锁的出现主要是为了完成gc的回收机制,对不同线程的引用计数的变化记录的更加精准
    # 全局解释器锁 GIL(global interpreter lock)
        # 导致了同一个进程中的多个线程只能有一个线程真正被cpu执行
    # 节省的是io操作的时间,而不是cpu计算的时间,因为cpu的计算速度非常快,大部分情况下,我们没有办法把一条进程中所有的io操作都规避掉








