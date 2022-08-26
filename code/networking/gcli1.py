# TODO ADD BLIT PLAYERS ONTO SCREEN FUNCTIONALITY
# TODO ADD MAINLOOP




import socket
from por import p
from pickle import loads as lo , dumps as du


import pygame
import time
from entity import GEntity
from gamestates import basic , Main_menu , Pause_menu
from utils import Stack



class client():
    """docstring for client."""
    def __init__(self):
        super(client, self).__init__()

        ### NETWORKING hahahahahaha
        self.s = socket.socket()
        print("CONNECTING")
        self.s.connect(('localhost' , p ))
        print("CONNECTED")



        ### GAME hahahahahaha
        self.display = pygame.display.set_mode((1280,720) , pygame.RESIZABLE)
        self.environment = pygame.Surface((1280 , 720 ))
        self.player1 = GEntity('blue')
        self.player2 = GEntity('blue')
        self.game_state_stack = Stack()
        self.game_state_stack.add(Main_menu(self))
        self.players = list[GEntity]()
        self.players.append(self.player1)
        self.players.append(self.player2)

    def mainloop(self) :
        while True :
            print("GOT get_input")
            self.get_input()
            print("GOT send_players")
            self.send_players()
            print("GOT get_players")
            self.get_players()
            print("GOT draw_players")
            self.draw_players()
            time.sleep(0.0166)
            print("COMPLETED ONE CYCLE ")



    def get_input(self) :
        for self.event in pygame.event.get() :
            if self.event.type == pygame.QUIT :
                self.running = False

            if self.event.type == pygame.KEYDOWN :
                if self.event.key == pygame.K_RETURN :
                    if self.game_state_stack.peek().name == "Main" :
                        self.game_state_stack.add(basic(self))
                if self.event.key == pygame.K_ESCAPE :
                    if self.game_state_stack.peek().name != "Pause" :
                        self.game_state_stack.add(Pause_menu(self))
                    else :
                        self.game_state_stack.pop()
                if self.event.key == pygame.K_RIGHT :
                    self.player1.actions["right"] = True

                if self.event.key == pygame.K_UP :
                    self.player1.actions["up"] = True
                if self.event.key == pygame.K_LEFT :
                    self.player1.actions["left"] = True
                if self.event.key == pygame.K_SPACE :
                    self.player1.actions["punch" ]= True
            if self.event.type == pygame.KEYUP :
                if self.event.key == pygame.K_RIGHT :
                    self.player1.actions["right"] = False
                if self.event.key == pygame.K_LEFT :
                    self.player1.actions["left"] = False
                if self.event.key == pygame.K_UP :
                    self.player1.actions["up"] = False
                if self.event.key == pygame.K_SPACE :
                    self.player1.actions["punch" ]= False

    def send_players(self)  :
        self.player1.image = None
        self.s.send(du(self.player1))


    def get_players(self) :
        self.player1 : GEntity = lo(self.s.recv(20480))
        print("GOT player1") 
        self.player2 : GEntity = lo(self.s.recv(20480))
        print("GOT player2") 

        self.player1.image = pygame.Surface((50,50))
        self.player1.image.fill(self.player1.color)

        self.player2.image = pygame.Surface((50,50))
        self.player2.image.fill(self.player2.color)

    def draw_players(self) :
        self.environment.blit(self.player1.image , (self.player1.rect.x , self.player1.rect.y))
        self.environment.blit(self.player2.image , (self.player2.rect.x , self.player2.rect.y))
        self.display.blit(pygame.transform.scale(self.environment , (self.display.get_height() , self.display.get_width())  ), (0,0))
        self.display.fill('white')
        pygame.display.flip()

c = client()
c.mainloop()
