import pygame
import socket
from socket import SOCK_STREAM as SS  , AF_INET as AF



from entity  import Entity , Platform
from reading_json import rect_list



class server():
    def __init__(self,rect_list):
        self.connections = list()
        self.socket = socket.socket(SS , AF)
        self.socket.listen(3)
        self.player1 = Entity("blue")
        self.rect_list = rect_list
        self.platforms = pygame.sprite.Group()
        for i in self.rect_list :
            self.platforms.add(Platform(i.x , i.y  , i.w , i.h ,"black"))

        self.player2 = Entity("red")
        
        self.player2.collidelist.add(self.player1 , self.platforms.sprites())
        self.player1.collidelist.add(self.player2 , self.platforms.sprites())

        self.recieved_players = {"player1" : self.player1 , "player2" : self.player2}
    def get_connections(self) :
        
        while len(self.connections) < 2 :
            self.connections.append({("player" + str( len(self.connections) + 1)) : self.socket.accept()})

        for _ in self.connections  : 
            pass
