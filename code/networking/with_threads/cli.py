import time

from pickle import dumps
import socket

s =socket.socket()

s.connect(("localhost" , __import__("port").p))


class player() :
    def __init__(self) -> None:
        self.x = 100
        self.y = 200

pl = player()

while True : 
    # s.send(dumps(pl))
    pl = dumps(pl)
    s.send(pl)
    # print("hola")
    print(pl)
    time.sleep(0.0000000000000000000001)
