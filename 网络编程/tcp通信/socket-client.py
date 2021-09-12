import socket
import os
import json,struct
path = r'E:\老男孩python老版本\老男孩22期（不加密）\老男孩开发22期\阶段01  基础篇\day14 课上视频\04 python fullstack s22 day14 装饰器的应用.mp4'
#客户端想服务端发送文件
sk = socket.socket()
sk.connect(('127.0.0.1',9001))
#file_path = r'F:\Python\网络编程\tcp\tmp.txt'
filename = os.path.basename(path)
filesize = os.path.getsize(path)
dic = {"filename": filename, "filesize": filesize}
str_dict = json.dumps(dic)

b_dic = str_dict.encode('utf-8')
mlen = struct.pack('i', len(b_dic))
sk.send(mlen) #4个字节表示字典转成字节之后的长度
sk.send(b_dic) #具体的字典数据

with open(path,mode='rb')as f:
    while filesize > 0:
        content = f.read(1024)
        filesize -= 1024
        sk.send(content)
sk.close()