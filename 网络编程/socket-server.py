import socket

'''
模拟c/s架构，要先运行服务端，再运行客户端
'''

sk = socket.socket()
sk.bind(('127.0.0.1', 9001))
sk.listen() #监听

conn,addr = sk.accept()
conn.send(b'hello') #服务端发送的消息会在客户端打印
msg = conn.recv(1024) #表示只接收1024个字节
print(msg)
conn.close()

sk.close()