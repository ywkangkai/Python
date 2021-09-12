import socket
import json,struct


sk = socket.socket()
sk.bind(('127.0.0.1', 9001))  #申请操作系统资源
sk.listen() #监听

conn,_ = sk.accept()  #conn里存储的是一个客户端和server端的连接信息

msg_len = conn.recv(4)
dic_len = struct.unpack('i',msg_len)[0]
msg = conn.recv(dic_len).decode('utf-8')
msg = json.loads(msg)


with open('tmp2.mp4','wb')as f:
    while msg['filesize'] > 0:
        content = conn.recv(1024)
        msg['filesize'] -= len(content)
        f.write(content)

conn.close()  #挥手断开连接
sk.close()  #归还申请的操作系统的资源