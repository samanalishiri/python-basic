from socketserver import UDPServer

from cstepthree.handler import UDPEchoHandler

print('waiting ...')
server = UDPServer(('localhost', 20000), UDPEchoHandler)
server.serve_forever()
