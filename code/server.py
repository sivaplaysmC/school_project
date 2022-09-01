import pickle
import socket
import pygame
from pygame.math import Vector2
from _thread import start_new_thread
from porto import pair


class simple : 
    def __init__(self , color , x=100 , y = 100 ) -> None:
        self.color = color
        self.image = None
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x , self.y , 50,50)
        self.actions = {"left" : False , "right" : False , "up" : False}
        self.velocity = Vector2()
    def move(self):
        self.velocity.x  = 0
        if self.actions["left"] :
            self.velocity.x += 4
        if self.actions["left"] :
            self.velocity.x -= 4
        self.rect.move_ip(self.velocity.x , 0 )

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind(pair)
s.listen(2)

players = [simple('blue') , simple('red' , 300,300)]

current_player = 0 

def threa(c:socket.socket, current_player:int) -> None : 
    while 1 : 
        print("Handling player" , current_player + 1 )
        players[current_player] = pickle.loads(c.recv(512))
        c.send(pickle.dumps(players[1 if current_player == 0 else 0 ]))
             
    

while 1 :
    c , a = s.accept()
    # c.send(pickle.loads(players[0])
    c.send(pickle.dumps(players[current_player]))
    start_new_thread(threa , (c,current_player))
    current_player += 1 
