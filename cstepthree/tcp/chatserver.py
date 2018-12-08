from socketserver import TCPServer

from cstepthree.handler import TCPEchoHandler

print('waiting ...')
server = TCPServer(('localhost', 20000), TCPEchoHandler)
server.serve_forever()
