import time
import logging
from logging import handlers

# 表示日志满1024个字节后就切割到新的文件中去，当达到5个日志文件后，删除最开始的那个，一直保留5个文件
rh = handlers.RotatingFileHandler('myapp.log', maxBytes=1024,backupCount=5)

#表示每5秒就切割一次日志文件，生成一个新的日志文件进行记录
fh = handlers.TimedRotatingFileHandler(filename='x2.log', when='s', interval=5, encoding='utf-8')
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    handlers=[fh,rh],
    level=logging.ERROR
)

# for i in range(1,100000):
#     time.sleep(1)
#     logging.error('KeyboardInterrupt error %s'%str(i))