import traceback
from multiprocessing.connection import Listener


class ChatRoomServer:

    def __init__(self, address, authkey):
        self.__address = address
        self.__authkey = authkey

    def execute(self):
        server = Listener(address=self.__address, authkey=self.__authkey)
        is_live = True

        while is_live:
            print('chat room! please connect')
            try:
                client = server.accept()
                self.client_handler(client)
            except Exception:
                traceback.print_exc()

    def client_handler(self, connection):
        print('Got connection from', self.__address)
        is_live = True
        while is_live:
            try:
                message = connection.recv()
                print('{}:{}'.format(self.__address, message))
            except EOFError:
                print('Connection closed')
                is_live = False
            except ConnectionResetError:
                print('disconnect')
                is_live = False


if __name__ == '__main__':
    ChatRoomServer(('localhost', 25000), authkey=b'peekaboo').execute()
