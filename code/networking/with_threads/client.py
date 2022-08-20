import socket
import time
import pickle
from port import p


s = socket.socket()

s.connect(('localhost' , p))

data = list[int]()

data.extend([1,2,3,4])

class entity : 
    def __init__(self) -> None:
        self.actions = [True , True , True]


while True :
    print("sent data :"  , data)
    s.send(pickle.dumps(data))
    data = s.recv(6400)
    data = pickle.loads(data)
    print("recieved data : " , data)


        
        
