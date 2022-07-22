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
        self.color = color
        self.image = pygame.Surface((50,50))
        self.rect  = self.image.get_rect()
        self.rect.x = spawn[0]
        self.rect.y = spawn[1]
        self.acceleration = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.delpos =pygame.math.Vector2() 

    def horizontal(self) :
        self.rect.delpos.x += self.velocity.x
        self.velocity.x = 0 
    def vertical(self) :
        self.rect.y += self.velocity.y
        self.velocity.y = 0 
    def move
