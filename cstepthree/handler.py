from socketserver import BaseRequestHandler, UDPServer
import time


class TCPEchoHandler(BaseRequestHandler):

    def handle(self):
        print('Got connection from', self.client_address)
        is_live = True
        while is_live:
            data = self.request.recv(8192)
            if not data:
                is_live = False
            else:
                data_string = data.decode('utf-8')
                print('client:{}'.format(data_string))

                response = 'Echo: {}'.format(data_string)
                self.request.send(bytes(response, 'utf-8'))


class UDPEchoHandler(BaseRequestHandler):

    def handle(self):
        print('Got connection from', self.client_address)
        data, sock = self.request
        data_string = data.decode('utf-8')
        print('client:{}'.format(data_string))

        response = 'Ack: {}'.format(data_string)
        sock.sendto(response.encode('utf-8'), self.client_address)
