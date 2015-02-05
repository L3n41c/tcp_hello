#!/usr/bin/env python3

import socketserver
import socket

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        answer = "Message sent by {}:{} to {}:\n{}\n".format(self.client_address[0],
                                                             self.client_address[1],
                                                             socket.gethostname(),
                                                             str(self.data))
        print(answer)
        self.request.sendall(bytes(answer, 'UTF-8'))

if __name__ == "__main__":
    HOST, PORT = '', 8000
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
