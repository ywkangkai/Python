import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9001))

msg = sk.recv(1024) #表示只接收1024个字节
print(msg)
sk.send(b'bbyebye') #客户端发送的消息会在服务端打印
sk.close()