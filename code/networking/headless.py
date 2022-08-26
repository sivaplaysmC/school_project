import pygame
import socket
from utils import Res , Stack
from reading_json import rect_list
from entity import Platform,  Entity
from gamestates import Main_menu 

class headless_process:
    def __init__(self , rect_list:list) :
        self.game_state_stack = Stack()
        self.environment_surface_res = Res(1280,720)
        self.display_surface_res = Res(1408 , 736)
        self.environment = pygame.Surface((self.environment_surface_res.x , self.environment_surface_res.y ))
        self.clock = pygame.time.Clock()
        self.dt = 0 
        self.prev = 0 
        self.rect_list = rect_list
        
        self.player1 = Entity("blue")
        self.player1.name = "Player1"
        self.player2 = Entity("blue")
        self.player2.name = "Player1"

        self.all_objects =pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        
        self.players.add(self.player1)
        for i in self.rect_list :
            self.platforms.add(Platform(i.x , i.y  , i.w , i.h ,"black"))

        self.player1.collidelist.add(*self.platforms.sprites())

        self.running = True
        self.game_state_stack.add(Main_menu(self))
    def update(self) :
        self.game_state_stack.peek().update() 

    def merge(self, branch):
        self.player1.actions = branch.actions
    def mainloop(self) :
        while self.running : 
            self.player1.move(0.0166)
            self.player2.move(0.0166)
            print(self.dt)
            self.update()

g1 = headless_process(rect_list=rect_list)
g1.mainloop()


