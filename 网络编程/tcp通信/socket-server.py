import socket

'''
模拟c/s架构，要先运行服务端，再运行客户端
'''

sk = socket.socket()
sk.bind(('127.0.0.1', 9001))  #申请操作系统资源
sk.listen() #监听

conn,addr = sk.accept()  #conn里存储的是一个客户端和server端的连接信息
conn.send(b'hello') #服务端发送的消息会在客户端打印
msg = conn.recv(1024) #表示只接收1024个字节
print(msg)
conn.close()  #挥手断开连接

sk.close()  #归还申请的操作系统的资源