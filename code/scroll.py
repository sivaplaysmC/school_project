
# from ctypes import sizeof
from utils import Res , Stack
from time import time
import pygame 
from reading_json import rect_list
from entity import Platform,  Entity
from gamestates import Main_menu, Pause_menu, basic 



class Game:
    def __init__(self , rect_list:list) :
        self.game_state_stack = Stack()
        self.environment_surface_res = Res(1408 , 736)
        self.display_surface_res = Res(1408 , 736)
        self.environment =  pygame.Surface((self.environment_surface_res.x , self.environment_surface_res.y))
        self.display = pygame.display.set_mode((self.display_surface_res.x , self.display_surface_res.y) , pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.dt = 0 
        self.prev = 0 
        self.rect_list = rect_list
        
        self.player1 = Entity(self , "blue" )
        self.player1.name = "Player1"
        self.player1.jump_key = pygame.K_UP
        self.other_player_name = "Player2"


        self.player2 = Entity(self , "red" )
        self.player2.name = "Player1"
        self.player2.move_left_key = pygame.K_a
        self.player2.move_right_key = pygame.K_d
        self.player2.jump_key = pygame.K_SPACE 
        self.other_player_name = "Player2"

        self.all_objects =pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        
        self.players.add(self.player1)
        for i in self.rect_list :
            self.platforms.add(Platform(i.x , i.y  , i.w , i.h ,"black"))

        self.player1.collidelist.add(*self.platforms.sprites())

        self.running = True
        # self.game_state_stack.add(mini(self))
        self.game_state_stack.add(Main_menu(self))
    def dt_clock(self) :
        self.now = time()
        self.dt =  self.now - self.prev
        self.prev = self.now
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
                if self.event.key == self.player1.move_right_key :
                    self.player1.actions["right"] = True

                if self.event.key == self.player1.jump_key :
                    self.player1.actions["up"] = True
                if self.event.key == self.player1.move_left_key:
                    self.player1.actions["left"] = True
                if self.event.key == pygame.K_INSERT :
                    self.player1.actions["punch" ]= True
            

                if self.event.key == self.player2.move_right_key :
                    self.player1.actions["right"] = True
                if self.event.key == self.player2.jump_key :
                    self.player1.actions["up"] = True
                if self.event.key == self.player2.move_left_key:
                    self.player1.actions["left"] = True
                if self.event.key == pygame.K_INSERT :
                    self.player1.actions["punch" ]= True

            
            if self.event.type == pygame.KEYUP :
                if self.event.key == self.player1.move_right_key :
                    self.player1.actions["right"] = False
                if self.event.key == self.player1.move_left_key:
                    self.player1.actions["left"] = False
                if self.event.key == self.player1.jump_key :
                    self.player1.actions["up"] = False
                if self.event.key == pygame.K_SPACE :
                    self.player1.actions["punch" ]= False

                if self.event.key == self.player2.move_right_key :
                    self.player1.actions["right"] = False
                if self.event.key == self.player2.move_left_key:
                    self.player1.actions["left"] = False
                if self.event.key == self.player2.jump_key :
                    self.player1.actions["up"] = False
                if self.event.key == pygame.K_SPACE :
                    self.player1.actions["punch" ]= False

    
    def update(self) :
        self.game_state_stack.peek().update() 

    def draw(self) :
        self.display.blit(pygame.transform.scale(self.environment , (self.display.get_width() , self.display.get_height())) , (0,0) )
        pygame.display.flip()
    def mainloop(self) :
        while self.running : 
            self.fps = self.clock.get_fps()
            self.dt = self.clock.tick(60) / 1000
            self.get_input()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game(rect_list)
    game.mainloop()
    print(game.all_objects)
