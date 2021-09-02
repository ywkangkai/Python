import logging

fh=logging.FileHandler('kk.log',encoding='utf-8')
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=logging.DEBUG,
    handlers=[fh]
)
'''
asctime:时间
name：用户
 levelname：等级以及第几行
 module：哪个文件
 message信息
'''


logging.error('你好1111222222')
logging.error('asdklaklj')
logging.debug('132lasjdas d')
logging.info('p[jgkl')
