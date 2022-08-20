import pygame
from pickle import loads as lo , dumps as du 
import socket
from entity import GEntity
from por import p



def on_connect(c: socket.socket) : 
    g.player1 = c.recv(2048)



class Game():
    """docstring for Game."""
    def __init__(self):
        super(Game, self).__init__()

        ##NETWOEKING
        self.s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

        self.s.bind(('localhost' , p) )
        self.s.listen( )

        self.players = list[socket.socket]()
        self.ip_addresses = list()



        ## Game

        self.environment = pygame.Surface((1280 , 720 ))
        self.dt = 0.0166
        self.player1 = GEntity('blue')
        self.player2 = GEntity('blue')
        self.objs = list[GEntity]()
        self.objs.extend([self.player1 , self.player2])

        

    def mainloop(self) : 
        while True : 
            while len(self.players) < 2 : 
                self.c , self.a  = self.s.accept()
                self.players.append(self.c)
                self.ip_addresses.append(self.a)
            print("Byrr")
            self.get_players()
            self.update()
            self.send_players()

    def get_players(self) : 
        try : 
            self.player1 = lo(self.players[0].recv(2048))
            print("GOT PLAYER 1 ")
            self.player2 = lo(self.players[1].recv(2048))
            print("GOT PLAYER 2 ")
        except EOFError as e  : 
            print(e)
        except BrokenPipeError as b  : 
            print(b)
        print(__name__)
            
            
    def send_players(self) : 
        print(__name__)
        self.player1.image = None
        self.player2.image = None
        
        try : 
            self.players[0].send(du(self.player1))
            print("sent pl1 to pl1 ")
            self.players[0].send(du(self.player2))
            print("sent pl2 to pl1 ")
            
            self.players[1].send(du(self.player1))
            print("sent pl1 to pl2 ")
            self.players[1].send(du(self.player2))
            print("sent pl2 to pl2 ")
            
        except BrokenPipeError as b  : 
            print(b)


    def update(self) :
        
        print(__name__)
        self.environment.fill("white")
        self.player1.move(self.dt)
        self.player2.move(self.dt)
        
            
g = Game()
g.mainloop()
        
