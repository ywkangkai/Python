import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9001))
while True:
    msg = sk.recv(1024).decode('utf-8')#表示只接收1024个字节
    print(msg)
    if msg.upper() == 'Q':
        break
    send_msg = input('输入内容')
    sk.send(send_msg.encode('utf-8')) #客户端发送的消息会在服务端打印
    if send_msg.upper() == 'Q':
        break
sk.close()