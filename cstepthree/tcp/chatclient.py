from socket import socket, AF_INET, SOCK_STREAM

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 20000))
print('connect to server!')
client.send(bytes('Hello', 'utf-8'))
response = client.recv(8192).decode('utf-8')
print(response)