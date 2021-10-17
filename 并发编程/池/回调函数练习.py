# 回调函数 : 效率最高的
import time,random,requests
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor

def func(url):
    res = requests.get(url)
    return {'url': url, 'res': res.text}

def print_func(res):
    res = res.result()
    content = f'url是{res["url"]}, 内容长度{len(res["res"])}'
    print(content)
    with open('url.txt', 'a') as f:
        f.write(content)


if __name__ == '__main__':
    urls = ['https://www.baidu.com', 'https://www.python.org', 'https://www.sina.com.cn', 'https://help.github.com']
    tp = ThreadPoolExecutor(3)
    for url in urls:
        ret = tp.submit(func, url)
        ret.add_done_callback(print_func)  # ret这个任务会在执行完毕的瞬间立即触发print_func函数,并且把任务的返回值对象传递到print_func做参数
        # 异步阻塞 回调函数 给ret对象绑定一个回调函数,等待ret对应的任务有了结果之后立即调用print_func这个函数
        # 就可以对结果立即进行处理,而不用按照顺序接收结果处理结果