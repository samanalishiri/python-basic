from concurrent.futures import ThreadPoolExecutor
from socket import AF_INET, SOCK_STREAM, socket


class ChatRoomServer:

    def __init__(self, host):
        self.__pool = ThreadPoolExecutor(max_workers=128)
        self.__connection = self.create_connection(host)
        self.is_live = True

    def create_connection(self, host):
        connection = socket(AF_INET, SOCK_STREAM)
        connection.bind(host)
        connection.listen(5)
        return connection

    def execute(self):
        while True:
            client, address = self.__connection.accept()
            self.__pool.submit(self.client_handler, client, address)

    def client_handler(self, client, address):
        print('Got connection from', address)
        while self.is_live:
            data = client.recv(65536)
            if not data:
                self.is_live = False
            else:
                print('{}:{}'.format(address, data.decode('utf-8')))

        print('Client closed connection')
        client.close()


if __name__ == '__main__':
    ChatRoomServer(('localhost', 15000)).execute()
