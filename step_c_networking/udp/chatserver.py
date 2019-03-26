from socketserver import UDPServer

from step_c_networking.handler import UDPEchoHandler

print('waiting ...')
server = UDPServer(('localhost', 20000), UDPEchoHandler)
server.serve_forever()
