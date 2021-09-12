import time,socketserver

#此时client可以启动多个与服务端进行交互
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        while True:
            try:
                content = conn.recv(1024).decode('utf-8')
                conn.send(content.upper().encode('utf-8'))
                time.sleep(0.5)
            except ConnectionError:
                break

server = socketserver.ThreadingTCPServer(('127.0.0.1',9001),Myserver)
server.serve_forever( )
