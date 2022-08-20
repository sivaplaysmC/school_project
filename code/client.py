import pygame

from utils import Stack 

from entity import Entity

class window_client():
    def __init__(self) -> None:
        self.player = Entity("blue" , self)
        self.game_state_stack = Stack() 
        self.inputs = list()
        self.display = pygame.display.set_mode((960,540) , pygame.RESIZABLE)
    def get_input(self) :
        
        for self.event in pygame.event.get() :
            if self.event.type == pygame.QUIT :
                self.running = False
            
            if self.event.type == pygame.KEYDOWN :
                if self.event.key == pygame.K_RETURN :
                    self.inputs.append(pygame.K_RETURN)
                if self.event.key == pygame.K_ESCAPE :
                    self.inputs.append(pygame.K_ESCAPE)
                if self.event.key == pygame.K_RIGHT :
                    self.player.actions["right"] = True

                if self.event.key == pygame.K_UP :
                    self.player.actions["up"] = True
                if self.event.key == pygame.K_LEFT :
                    self.player.actions["left"] = True
            if self.event.type == pygame.KEYUP :
                if self.event.key == pygame.K_RIGHT :
                    self.player.actions["right"] = False
                if self.event.key == pygame.K_LEFT :
                    self.player.actions["left"] = False
                if self.event.key == pygame.K_UP :
                    self.player.actions["up"] = False
    def update()
