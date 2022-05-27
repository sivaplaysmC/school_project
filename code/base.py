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

        # if self.position.y - (self.rect.h + 10) > 720 :
        #     self.position.y = 720 - (self.rect.h + 10)
        #     self.do_gravity = False

        if self.do_gravity :
            self.acceleration.y = 0.9
        else :
            self.acceleration.y = 0
        self.acceleration.x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] :
            self.acceleration.x +=3
        if keys[pygame.K_LEFT] :
            self.acceleration.x -= 3
        if self.velocity.y == 0 :
            if keys[pygame.K_SPACE] :
                self.velocity.y += -15
        if self.position.y - (self.rect.h + 10) > 720 :
            self.position.y = 720 - (self.rect.h + 11)
            self.acceleration.y = 0
        if self.acceleration.y < -self.max_acceleration :
            self.acceleration.y = -self.max_acceleration
        self.acceleration.x += self.velocity.x * -0.2
        self.velocity += self.acceleration * dt
        self.delpos = self.velocity *dt + ((self.acceleration *0.5) * (dt * dt))
        self.position += self.delpos
        hits = pygame.sprite.spritecollide(player,platform_group, False)
        if hits :
            if self.position.y <= hits[0].rect.top :
                self.position.y = hits[0].rect.top - 50  
                self.velocity.y = 0 
        self.rect.topleft = self.position

    def collision(self , delpos) :
        collision_list = pygame.sprite.spritecollide(self , platform_group , dokill=False )
        if collision_list :
            x = collision_list[0]
            print(x.rect)
            if self.delpos.x > 0 :
                self.position.x = x.rect.left 
            elif self.delpos.x < 0 :
                self.position.x = x.rect.right 
            if self.delpos.y > 0 :
                self.position.y = x.rect.top
            elif self.delpos.y < 0 :
                self.position.y = x.rect.bottom

run = True
player = Entity()
border = border(0,0,1280,720)
platform1 = Platform(0,690,1280,30,(255,20,0))
platform2 = Platform(200, 600, 100, 50, (255,20,0))
platform3 = Platform(400, 500, 100, 50, (255,255,0))
platform4 = Platform(180, 400, 100, 50, (0,255,0))
platform5 = Platform(500, 300, 100, 50,(0,255,255))





player_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
platform_group.add(platform1,platform2,platform3,platform4,platform5)
player_group.add(player)



while run :
    # clock.tick(120)
    dt = (clock.tick(120) /1000) * 60

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
