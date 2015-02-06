#!/usr/bin/env python3

import sys
import socketserver
import socket

banner = "[Default banner]"

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            while True:
                self.data = self.request.recv(1024).strip()
                if not self.data: return
                answer = "{}\nMessage sent by {}:{} to {}:\n{}\n".format(banner,
                                                                         self.client_address[0],
                                                                         self.client_address[1],
                                                                         socket.gethostbyname(socket.gethostname()),
                                                                         str(self.data))
                print(answer)
                self.request.sendall(bytes(answer, 'UTF-8'))
        finally:
            self.request.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        banner = sys.argv[1]
    HOST, PORT = '', 8000
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.serve_forever()
