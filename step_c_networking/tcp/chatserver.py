from socketserver import TCPServer

from step_c_networking.handler import TCPEchoHandler

print('waiting ...')
server = TCPServer(('localhost', 20000), TCPEchoHandler)
server.serve_forever()
