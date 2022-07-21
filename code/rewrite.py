from time import time
import pygame 
from reading_json import rect_list
from classes_and_funcs import Entity , Platform
class Res:
    def __init__(self , *args) -> None:
        self.x , self.y = *args
class Game:
    def __init__(self , rect_list) -> None:
        self.environment_surface = Res(1280,720)
        self.display_surface = Res(1408 , 736)
        self.Player1 = Entity("blue")
        self.Player1.name = "Player1"

        self.Player1.jump_key = pygame.K_UP
        self.Player1.other_player_name = "Player2"
        self.Player2 = Entity("red")
        self.Player2.name = "Player2"
        self.Player2.move_right_key = pygame.K_d
        self.Player2.move_left_key = pygame.K_a
        self.Player2.jump_key = pygame.K_w
        self.Player2.other_player_name = "Player1"
        self.players = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.players.add(self.Player1 , self.Player2)
        self.rect_list = rect_list
        for i in self.rect_list :
            self.platforms.add(Platform(i.x, i.y, i.w, i.h, "black"))
        self.Player1.collidelist.add(self.Player2 , *self.platforms.sprites())
        self.Player2.collidelist.add(self.Player1 , *self.platforms.sprites())
        self.prev = 0 
    def dt(self) :
        self.now = time()
        self.dt =  self.now - self.prev
        self.prev = self.now
    def get_input(self) :
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                
