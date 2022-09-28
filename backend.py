## TODO : Remove Environment (It is not needed for detecting collisions )
##        It (the Environment surface) also interferes with the process of pickling and unpickling


import pygame 
from player import *
from utils import *
import pickle
import socket
from socket import AF_INET as AF , SOCK_STREAM as SS


class Backend_Game() :
    def __init__(self , ip = ('localhost' , 9090) ) :
        self.environment = pygame.Surface((1280 , 720))
        self.ip = ip
        self.socket = socket.socket(AF , SS)
        self.socket.bind(self.ip)
        self.socket.listen(3)
        self.players = [ Player('red' , spawn_pos = Vector(250,500) , id=0 ) , Player('blue' , spawn_pos = Vector(750,500) , id=1) ]
        self.connections = Stack()
        self.ip_addresses = Stack()
        self.id = None

    def mainloop(self) :
        
        while len( self.connections) < 2  :
            conn  , address = self.socket.accept() 
            self.connections.add(conn)
            self.ip_addresses.add(address)
            self.handle_player(self.connections.max_index() , self.connections.peek())
        self.update()
    
    def update(self) :
        self.move_players() # 
        self.position_players() # 


    def move_players(self) :
        for _ in self.players :
            _.update(0.1)

    def position_players(self) :
        for i in self.players :
            self.environment.blit(pygame.Surface((50 , 50 )) , ( i.Rect.x  , i.Rect.y ))


    def handle_player(self , player_no , conn ) :
        self.parcel = self
        self.parcel.id = player_no
        self.parcel = pickle.dumps(self)
        conn.send(self.parcel)
        while 1 : 
            clients_game = self.socket.recv(1024)
            clients_game = pickle.loads(clients_game)
            self.players[player_no] = clients_game.player
if __name__ == '__main__' :
    a = Backend_Game()
    a.mainloop()
