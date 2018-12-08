from multiprocessing.connection import Client


c = Client(('localhost', 25000), authkey=b'peekaboo')
while True:
    message = input('->')
    c.send(message)
