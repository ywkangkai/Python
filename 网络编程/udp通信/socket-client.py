import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
server = ('127.0.0.1',9001)
while True:
    snedmessage = input().encode('utf-8')
    if snedmessage.upper() == 'Q':
        break
    sk.sendto(snedmessage,server)
    msg = sk.recv(1024).decode('utf=8')
    if msg.upper() == 'Q':
        break
    print(msg)