### GOAL : Get input from one client , then the other , process it and send player
           # location metadata




import pickle
import pygame
import socket
from por  import p


def error_check( func) :
    def inner(*args , **kwargs) :
        try :
            print(*args)
            print(**kwargs)
            return func( *args)
        except BrokenPipeError as B :
            print(B)
        except EOFError as E  :
            print(E)
    return inner()

class Server():
    global socket
    def __init__(self , ip , port ):
        self.sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

        self.sock.bind((ip , port) )
        self.sock.listen(2)
        self.connections = list[socket.socket]()
        self.ip_addresses = list()
        self.client1 = None
        self.client2 = None
        self.jobs = list()


        ### GAME PART STARTS HERE
        self.environment = pygame.Surface((1280 , 720))

    def send_data(self):
        try :
            self.connections[1].send(self.client1)
        except EOFError :
            print("EOFError")
        except BrokenPipeError :
            print("Broken Pipe Error")
            self.connections.pop(1)
        try :
            self.connections[0].send(self.client2)
        except EOFError :
            print("EOFError")
        except BrokenPipeError :
            print("Broken Pipe Error")
            self.connections.pop(0)

    def mainloop(self) :
        while True  :
            while len(self.connections) < 2 :
                _c ,_i = (self.sock.accept())
                self.connections.append(_c)
                self.ip_addresses.append(_i)
                print("Waiting for players ")
            self.client1 = self.connections[0].recv(2048)
            print(pickle.loads(self.client1))
            try :
                print(pickle.loads(self.client2))
            except : pass
            self.client2 = self.connections[1].recv(2048)
            self.send_data()


servo = Server(ip="localhost" , port=p)

servo.mainloop()
