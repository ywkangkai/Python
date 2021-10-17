import queue   # 线程之间数据安全的容器队列
from queue import Empty  # 不是内置的错误类型,而是queue模块中的错误
# q = queue.Queue(4)   # fifo 先进先出的队列
# q.get()
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# print('4 done')
# q.put_nowait(5)
# print('5 done')
# try:
#     q.get_nowait()
# except Empty:pass
# print('队列为空,继续其他内容')