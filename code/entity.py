from typing import Tuple
import pygame

class Entity(pygame.sprite.Sprite) :
    def __init__(self , color , spawn : Tuple) -> None:
        self.color = color
        self.image = pygame.Surface((50,50))
        self.rect  = self.image.get_rect()
        self.rect.x = spawn[0]
        self.rect.y = spawn[1]
        self.acceleration = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.delpos = 1

class Simple (pygame.sprite.Sprite) :
    
    def __init__(self , color , spawn : Tuple) -> None:
        super().__init__()
        self.spawn = spawn
        self.color = color
        self.image =pygame.image.load(r"console.png").convert_alpha() 
        self.image = pygame.transform.scale(self.image , (50 , 50 ))
        self.rect  = self.image.get_rect()
        self.rect.x = spawn[0]
        self.rect.y = spawn[1]
        self.acceleration = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.delpos =pygame.math.Vector2() 
        self.velocity.x , self.velocity.y = 0 , 0 
        self.actions = {"right" : False , "left" : False}

    def horizontal(self, dt) :
        self.rect.x += self.velocity.x * dt 
        self.velocity.x = 0 
    def vertical(self, dt) :
        self.rect.y += self.velocity.y * dt 
        self.velocity.y = 0 
    def move(self,dt) :
        if self.actions["right"] : self.velocity.x += 200
        if self.actions["left"] : self.velocity.x -= 200
        self.horizontal(dt)
        self.vertical(dt)
        self.velocity.x  ,self.velocity.y = 0 , 0 
