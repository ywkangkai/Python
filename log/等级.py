import logging
#默认只显示waring及以上级别的信息，控制台不会显示debug与info的打印信息
logging.debug('调试')
logging.info('信息')
logging.warning('警告')
logging.error('错误')

logging.basicConfig(level=logging.DEBUG) #改变日志输出的等级