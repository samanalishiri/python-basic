from socket import socket, AF_INET, SOCK_DGRAM

client = socket(AF_INET, SOCK_DGRAM)
client.sendto(bytes('Hello', 'utf-8'), ('localhost', 20000))
data, sock = client.recvfrom(8192)
print(data.decode('utf-8'))
