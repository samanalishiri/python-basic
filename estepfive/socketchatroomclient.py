import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 15000))

while True:
    message = input('->')
    client.send(bytes(message, 'utf-8'))

