import pygame
from entity import Entity, Platform
# from pygame.display import update

class GameState :
    def __init__(self  , Game:"Game") :
        self.color = "blue"
        self.Game = Game
        # self.win = self.game.environment
        self.environment : "pygame.Surface" = self.Game.environment
    def main(self):
        self.environment.fill(self.color)

class Pause_menu(GameState):
    
    def __init__(self , Game):
        super().__init__(Game)
        self.name = "Pause"
        self.environment : "pygame.Surface" = self.Game.environment

    def update(self) :
        self.Game.environment.fill("white")
        self.Game.environment.blit(pygame.transform.scale(pygame.image.load("pause_menu.png"), (self.Game.environment.get_width(), self.Game.environment.get_height() )), (0,0))

class Main_menu(GameState) :
    def __init__(self, Game):
        super().__init__(Game)
        self.name = "Main"
        self.environment : "pygame.Surface" = self.Game.environment
    def update(self) :
        self.Game.environment.fill((100,100,100))


class mini(GameState) :
    def __init__(self , Game):
        super().__init__(Game)
        self.name = "mini"
        self.environment : "pygame.Surface" = self.Game.environment
        self.plat = Platform(100,500,100,100,"black")
        self.ground = Platform(0 , 720 , 5000 , 5000 , "blue")
        self.collide_list = pygame.sprite.Group()
        self.collide_list.add(self.plat , self.ground)
        
    def update(self) :
        self.environment.fill("white")
        self.Game.player.move(self.Game.dt  , self.collide_list)
        # self.environment.blit(self.plat.image , (self.plat.rect.x , self.plat.rect.y))
        for i in self.collide_list : 
            self.environment.blit(i.image , (i.rect.x , i.rect.y))
        self.environment.blit(self.Game.player.image , (self.Game.player.rect.x , self.Game.player.rect.y))

class basic(GameState):
    vec = pygame.Vector2
    def __init__(self , Game) :
        super().__init__(Game)
        self.name = "basic"
        self.environment : "pygame.Surface" = self.Game.environment
        self.player = Entity("blue")
        self.player.name = "Player1"
        self.player.jump_key = pygame.K_UP
        self.other_player_name = "Player2"



        self.all_objects =pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        
        self.players.add(self.player)
        for i in self.Game.rect_list :
            self.platforms.add(Platform(i.x , i.y  , i.w , i.h ,"black"))

        self.player.collidelist.add(*self.platforms.sprites())
        
    def update(self) :
        self.environment.fill("white")
        self.player.move(self.Game.dt)
        for i in self.platforms :
            self.environment.blit(i.image , (i.rect.x , i.rect.y))
        self.environment.blit(self.player.image , (self.player.rect.x , self.player.rect.y))


            
class Game_world(GameState) :
    def __init__(self, Game: "Game"):
        super().__init__(Game)
        self.name = "World"
    def update(self) :
        if self.Game.Player2.actions["right"] : self.Game.Player2.acceleration.x += 1
        if self.Game.Player2.actions["right"] : self.Game.Player2.acceleration.x += 1
        if self.Game.Player1.actions["left"] : self.Game.Player1.acceleration.x -= 1
        if self.Game.Player1.actions["left"] : self.Game.Player1.acceleration.x -= 1
        self.Game.environment.fill((255,255,255))
        self.Game.Player1.move(self.Game.dt)
        self.Game.Player2.move(self.Game.dt)
        self.Game.players.draw(self.Game.environment)
        self.Game.platforms.draw(self.Game.environment)
