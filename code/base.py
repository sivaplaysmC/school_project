import pygame , random
from pygame import Vector2 as vec
from copy import copy

pygame.init()
WIDTH = 1280
HEIGHT = 720
win = pygame.display.set_mode((WIDTH , HEIGHT))
clock = pygame.time.Clock()
border = pygame.Rect(0,0,WIDTH , HEIGHT)

class Platform(pygame.sprite.Sprite) :
    def __init__(self , x , y , w , h ):
        super().__init__()
        self.image = pygame.Surface((w , h))
        self.image.fill((255,20,0))

        self.rect = self.image.get_rect()
        self.rect.update(x , y , w , h )

class Entity(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill((0,255,255))

        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500

        self.position = vec(500,500)
        self.delpos = vec(0,0)
        self.velocity = vec(0,0)
        self.acceleration = vec(0,0)
        self.do_gravity = True
        # self.mass = 1

    def move(self) :

        if self.position.y - (self.rect.h + 10) > 720 :
            self.position.y = 720 - (self.rect.h + 10)
            self.do_gravity = False

        if self.do_gravity :
            self.acceleration.y = 0.9
        else :
            self.acceleration.y = 0
        self.acceleration.x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] :
            self.acceleration.x += 10
        if keys[pygame.K_LEFT] :
            self.acceleration.x -= 10
        if keys[pygame.K_SPACE] :
            self.velocity.y += -1
        if self.position.y - (self.rect.h + 10) > 720 :
            self.position.y = 720 - (self.rect.h + 11)
            self.acceleration.y = 0

        self.acceleration.x += self.velocity.x * -0.2
        self.velocity += self.acceleration * dt
        self.position += self.velocity *dt + ((self.acceleration *0.5) * (dt * dt))
        
            # self.velocity.y = 0
        self.rect.topleft = self.position

    def collision(self) :
        if self.delpos >  
run = True
player = Entity()

while run :
    # clock.tick(120)
    dt = (clock.tick(60) /1000) * 60

    player.move()

    win.fill((255,255,255))
    win.blit(player.image , player.rect)
    pygame.display.flip()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b :
            print(player.rect.topleft , player.position , player.velocity , player.acceleration , sep = "\t")
