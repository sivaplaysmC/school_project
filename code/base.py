import pygame , random
from pygame import Vector2 as vec
from copy import copy

pygame.init()

def clamp(obg , renge) :
    if obj > range :
        return range 
    if obj < renge :
        return obj
    return obg 
pygame.init()
WIDTH = 1280
HEIGHT =640 
win = pygame.display.set_mode((WIDTH , HEIGHT))
clock = pygame.time.Clock()
### BACKGROUND 
background = pygame.image.load("g:\school_project\sewer.png").convert_alpha()
background = pygame.transform.scale(background, ( 3840 , 640 ) )
bg_x = 0
bg_y = 0

background_surface = pygame.Surface((3840,640))
background_surface.blit(background , (0,0))



class Platform(pygame.sprite.Sprite) :
    def __init__(self , x , y , w , h , color):
        super().__init__()
        self.image = pygame.Surface((w , h))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.update(x , y , w , h )
    def move(self ,x ,y , beginning , end) :
        self.direction = 1 # 1 means right to left
        if self.direction == 1 :
            self.rect.move_ip(2, y)
            if self.rect.x >= end :
                self.direction = 0
        if self.direction == 0 :
            self.rect.move_ip(-2, y)
            if self.rect.x <= beginning :
                self.direction = 1 

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
        self.max_acceleration = 4

    def move(self) :

        self.delpos.x = 0
        self.acceleration.x = 0 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] :
            self.acceleration.x +=3
        if keys[pygame.K_LEFT] :
            self.acceleration.x -= 3
        self.acceleration.x += self.velocity.x * -0.2
        self.velocity.x += self.acceleration.x * dt
        self.delpos.x = self.velocity.x *dt + ((self.acceleration.x *0.5) * (dt * dt))
        self.rect.x += self.delpos.x
        hitx = pygame.sprite.spritecollide(player, platform_group, False)
        if hitx :
            if self.delpos.x > 0 :
                self.rect.right = hitx[0].rect.left
            if self.delpos.x < 0 :
                self.rect.left = self.rect.right
        self.delpos.y = 0
        self.acceleration.y = 1.5
        keys = pygame.key.get_pressed()
        if abs( self.velocity.y ) <= 0.5 :
            if keys[pygame.K_SPACE] :
                self.velocity.y += -15
        hity = pygame.sprite.spritecollide(player,platform_group, False)
        if hity :
            print(hity[0].rect)
            if self.position.y <= hity[0].rect.top :
                self.position.y = hity[0].rect.top - 50  
                self.velocity.y = 0 
        self.velocity.y += self.acceleration.y * dt
        self.delpos.y = self.velocity.y *dt + ((self.acceleration.y *0.5) * (dt * dt))
        self.rect.y += self.delpos.y

        self.rect.topleft = self.position

def screen_movement():
    global bg_x
    if player.position.x > 900:
       player.position.x =900 
       if -bg_x < 2560 :
            bg_x -= player.velocity.x
            if abs(player.velocity.x) > 1 :
                for i in platform_group.sprites() :
                    if id(i) != id(platform1) :
                        i.rect.x-=player.velocity.x
    if player.position.x < 300 :
        player.position.x =300 
        if -bg_x > 0 :
            bg_x -= player.velocity.x
            if abs(player.velocity.x) > 1 :
                for i in platform_group.sprites() :
                    if id(i) != id(platform1) :
                        i.rect.x -= player.velocity.x
run = True
player = Entity()
platform1 = Platform(-1280,610,5000,30,(255,20,0))
platform2 = Platform(200, 600, 100, 50, (255,20,0))
platform3 = Platform(400, 500, 100, 50, (255,255,0))
platform4 = Platform(180, 400, 100, 50, (0,255,0))
platform5 = Platform(400 , 400 , 100,50 , (0,0,0))
platform6 = Platform(2000, 500, 100, 50, (255,255,255))




player_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
baseplatform = pygame.sprite.Group()
# baseplatform.add(platform1)
platform_group.add(platform1,platform2,platform3,platform4,platform5,platform6)
player_group.add(player)



while run :
    platform5.move(2,0,400 , 500)
    # clock.tick(120)
    dt = (clock.tick(120) /1000) * 60

    player.move()
    screen_movement()
    win.fill((255,255,255))
    win.blit(background_surface , ( bg_x,0 ))
    background_surface.blit(background , (0,0))
    for i in platform_group.sprites():
        background_surface.blit(i.image, i.rect.topleft)
    player_group.draw(win)
    pygame.display.flip()
    for event in pygame. event.get() :
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b :
            
            print(player.rect.topleft , player.position , player.velocity , player.acceleration , sep = "\t")
            print(bg_x)
