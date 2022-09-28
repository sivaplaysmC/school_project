import pickle
import pygame 
from player import *
from utils import *
import socket
# from socket import AF_INET as AF , SOCK_STREAM as SS


class Frontend_Game() :
    def __init__(self , ip = ('localhost' , 9090) ) :
        self.environment = pygame.Surface((1280 , 720))
        self.ip = ip 
        self.socket = socket.socket()
        self.socket.connect(self.ip)
        self.display = pygame.display.set_mode((1280,720))
        self.backend_game = self.socket.recv(1024)
        self.backend_game = pickle.loads(self.backend_game)
        self.players = self.backend_game.players
        self.current_player = [i for i in self.players if i.id == self.backend_game.id][0]

    def update(self) :
        self.get_input() #
        self.move_players() # 
        self.position_players() #
        self.draw_players() # 
            
    def get_input(self) :
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RIGHT :
                    self.current_player.actions['right'] = True
                if event.key == pygame.K_LEFT :
                    self.current_player.actions['left'] = True
                if event.key == pygame.K_UP :
                    self.current_player.actions['up'] = True
                if event.key == pygame.K_DOWN :
                    self.current_player.actions['down'] = True
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_RIGHT :
                    self.current_player.actions['right'] = False
                if event.key == pygame.K_LEFT :
                    self.current_player.actions['left'] = False
                if event.key == pygame.K_UP :
                    self.current_player.actions['up'] = False
                if event.key == pygame.K_DOWN :
                    self.current_player.actions['down'] = False
    def draw_players(self) :
        # for i in self.players :
        #     self.environment.blit(i.image , ( i.Rect.x , i.Rect.y ))
        # self.display.blit(_ , (self.current_player.pos.x , self.current_player.pos.x))
        self.display.blit(self.environment , (0,0))

    def position_players(self) :
        for i in self.players :
            self.environment.blit(i.image , ( i.Rect.x , i.Rect.y ))

    def move_players(self) :
        for _ in self.players :
            _.update(0.1)

if __name__ == '__main__' :
    a = Frontend_Game()
