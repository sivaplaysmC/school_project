import socket
from por  import p
from pickle import loads as lo , dumps as du

c = socket.socket()

c.connect(('localhost' ,  p))

while 1:
    print(lo(c.recv(2048)))
    c.send(du("Hi from client1"))
