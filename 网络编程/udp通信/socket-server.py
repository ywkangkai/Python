import socket

sk = socket.socket(type=socket.SOCK_DGRAM)  #不同的type代表不同的协议，默认是tcp协议
sk.bind(('127.0.0.1', 9001))

while True:
    msg,addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
    snedmessage = input().encode('utf-8')
    sk.sendto(snedmessage,addr)
