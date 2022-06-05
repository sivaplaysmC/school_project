import pygame , random
from pygame import Vector2 as vec
from copy import copy

pygame.init()
WIDTH = 1280
HEIGHT = 720
win = pygame.display.set_mode((WIDTH , HEIGHT))
clock = pygame.time.Clock()
border = pygame.Rect(0,0,WIDTH , HEIGHT)

class border(pygame.Rect) :
    def __init__(self , x , y , w , h ) :
        pass


class Platform(pygame.sprite.Sprite) :
    def __init__(self , x , y , w , h , color):
        super().__init__()
        self.image = pygame.Surface((w , h))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.update(x , y , w , h )

class Entity(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill((0,55,255))

        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500

        self.position = vec(500,500)
        self.delpos = vec(0,0)
        self.velocity = vec(0,0)
        self.acceleration = vec(0,0)
        self.do_gravity = True
        # self.mass = 1
        self.max_acceleration = 4

    def get_input(self) :

        # self.velocity.x , self.velocity.y = 0 ,0
        self.acceleration.x , self.acceleration.y =  0 , 0
        # self.delpos.x , self.delpos.y  = 0 , 0 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] :
            self.acceleration.x += 2
        if keys[pygame.K_LEFT] :
            self.acceleration.x -= 2
        if keys[pygame.K_SPACE] and self.velocity.y == 0 :
            self.velocity.y -= 5

    def horizontal_movement(self) :
        self.acceleration.x += self.velocity.x * -.70
        self.velocity.x += self.acceleration.x * dt
        self.delpos.x = self.velocity.x *dt + ((self.acceleration.x *0.5) * (dt * dt))
        self.rect.x += self.delpos.x
        hitx = pygame.sprite.spritecollide(player,platform_group, False)
        if hitx :
            if self.delpos.x > 0 :    
                self.rect.right = hitx[0].rect.left
            if self.delpos.x < 0 :    
                self.rect.left = hitx[0].rect.right

    def vertical_movement(self) :
        self.acceleration.y = 0.1
        self.velocity.y += self.acceleration.y
        self.delpos.y = self.velocity.y + (0.5 * self.acceleration.y)
        self.rect.y += self.delpos.y
        hity = pygame.sprite.spritecollide(player, platform_group, False)
        if hity :
            if self.delpos.y > 0 :
                self.velocity.y = 0
                self.rect.bottom = hity[0].rect.top
            if self.delpos.y < 0 :
                self.velocity.y = 0 
                self.rect.top = hity[0].rect.bottom
    def move(self) :
        self.get_input()
        self.horizontal_movement()
        self.vertical_movement()

run = True
player = Entity()
border = border(0,0,1280,720)
platform1 = Platform(0,690,1280,30,(255,20,0))
platform2 = Platform(200, 500, 100, 50, (255,20,0))
# platform3 = Platform(400, 500, 100, 50, (255,255,0))
platform4 = Platform(180, 400, 100, 50, (0,255,0))
platform5 = Platform(700, 500, 100, 50,(0,255,255))





player_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
platform_group.add(platform1,platform2,platform4,platform5)
player_group.add(player)



while run :
    # clock.tick(120)
    dt = (clock.tick(60) /1000) * 60

    player.move()

    win.fill((255,255,255))
    platform_group.draw(win)
    player_group.draw(win)
    pygame.display.flip()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b :
            print(player.rect.topleft , player.position , player.velocity , player.acceleration , sep = "\t")
