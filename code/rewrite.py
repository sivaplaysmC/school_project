from time import time
import pygame 
from reading_json import rect_list
from classes_and_funcs import Entity , Platform
from gamestates import Main_menu, Pause_menu , Game_world


class Stack:
    def __init__(self):
        self.stack = list()
        pass
    def pop(self) :
        self.stack.pop()
    def add(self,item):
        self.stack.append(item)
    def peek(self):
        return self.stack[-1]


class Res:
    def __init__(self , *args) -> None:
        self.x , self.y = args



class Game:
    def __init__(self , rect_list:pygame.sprite.Group) :
        self.game_state_stack = Stack()
        self.environment_surface_res = Res(1280,720)
        self.display_surface_res = Res(1408 , 736)
        self.environment =  pygame.Surface((self.environment_surface_res.x , self.environment_surface_res.y))
        self.display = pygame.display.set_mode((self.display_surface_res.x , self.display_surface_res.y))
        self.clock = pygame.time.Clock()
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
        self.dt = 0 
        self.prev = 0 

        self.running = True
        self.game_state_stack.add(Game_world(self))
    def dt_clock(self) :
        self.now = time()
        self.dt =  self.now - self.prev
        self.prev = self.now
        print(self.dt)
    def get_input(self) :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                self.running = False
                print("hi")
            
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RETURN :
                    if self.game_state_stack.peek().name == "Menu" :
                        self.game_state_stack.add(Game_world(self))
                if event.key == pygame.K_ESCAPE :
                    if self.game_state_stack.peek().name != "Pause" :
                        self.game_state_stack.add(Pause_menu(self))
                    else :
                        self.game_state_stack.pop()
                if event.key == self.Player1.move_left_key :
                    self.Player1.actions["left"] = True
                    self.Player1.actions["idle"] = False
                elif event.key == self.Player1.move_left_key :
                    self.Player1.actions["right"] = True
                    self.Player1.actions["idle"] = False
                elif event.key == self.Player1.jump_key :
                    self.Player1.actions["left"] = True
                    self.Player1.actions["idle"] = False
                elif event.key == self.Player2.move_left_key :
                    self.Player1.actions["left"] = True
                    self.Player2.actions["idle"] = False
                elif event.key == self.Player2.move_left_key :
                    self.Player1.actions["right"] = True
                    self.Player2.actions["idle"] = False
                elif event.key == self.Player2.jump_key :
                    self.Player1.actions["left"] = True
                    self.Player2.actions["idle"] = False
            if event.type == pygame.KEYUP :
                if event.key == self.Player1.move_left_key :
                    self.Player1.actions["left"] = False
                    self.Player1.actions["idle"] = True
                elif event.key == self.Player1.move_left_key :
                    self.Player1.actions["right"] = False
                    self.Player1.actions["idle"] = True
                elif event.key == self.Player1.jump_key :
                    self.Player1.actions["left"] = False
                    self.Player1.actions["idle"] = True
                elif event.key == self.Player2.move_left_key :
                    self.Player1.actions["left"] = False
                    self.Player2.actions["idle"] = True
                elif event.key == self.Player2.move_left_key :
                    self.Player1.actions["right"] = False
                    self.Player2.actions["idle"] = True
                elif event.key == self.Player2.jump_key :
                    self.Player1.actions["left"] = False
                    self.Player2.actions["idle"] = True
    def update(self) :
        self.game_state_stack.peek().update() 

    def draw(self) :
        self.display.blit(pygame.transform.scale(self.environment , (self.display_surface_res.x , self.display_surface_res.y)) , (0,0) )
        pygame.display.flip()
    def mainloop(self) :
        while self.running : 
            self.fps = self.clock.get_fps()
            self.dt = self.clock.tick(60) / 1000
            self.get_input()
            self.update()
            self.draw()
            print( self.dt ,self.fps, sep = "\t\t\t\t")


game = Game(rect_list)
game.mainloop()
# g = Game()

