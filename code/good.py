import pygame , random
from pygame import Vector2 as vec
from copy import copy

pygame.init()
WIDTH = 1280
HEIGHT = 720
win = pygame.display.set_mode((WIDTH , HEIGHT))
clock = pygame.time.Clock()
border = pygame.Rect(0,0,WIDTH , HEIGHT)


# def get_image(image , metadata) :



class border(pygame.Rect) :
    def __init__(self , x , y , w , h ) :
        pass
paused = False
def pause() :
    # global paused , run
    # for event in pygame.event.get():
    #     if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
    paused = True
            
    while paused :
        win.fill((0,0,0))
        pygame.display.flip()
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused = False
            if event.type == pygame.QUIT :
                paused = False
                # pygame.quit()
                run = False
        

class Platform(pygame.sprite.Sprite) :
    def __init__(self , x , y , w , h , color):
        super().__init__()
        self.image = pygame.Surface((w , h))
        self.image.fill(color)
        self.name = "Platform"

        self.rect = self.image.get_rect()
        self.rect.update(x , y , w , h )
    def move(self ,  x_min , x_max , velocity) :
        self.x_max = x_max
        self.x_min = x_min
        self.velocity = velocity
        # print(self.rect.left <= self.x_min , self.rect.right >= self.x_min)
        if self.rect.left <= self.x_min or self.rect.right >= self.x_min  :
            self.velocity *= -1
        self.rect.move_ip(self.velocity, 0)
class Entity(pygame.sprite.Sprite) :
    def __init__(self , color):
        super().__init__()
        self.color = color
        self.image = pygame.Surface((30,30))
        self.image.fill(self.color)
        self.px , self.py = 0 , 0 

        self.collidelist = pygame.sprite.Group()
        self.name = str() 
        

        self.move_right_key = pygame.K_RIGHT
        self.move_left_key  = pygame.K_LEFT
        self.jump_key = pygame.K_SPACE

        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        self.hitx , self.hity = list() , list()

        self.position = vec(500,500)
        self.delpos = vec(0,0)
        self.velocity = vec(0,0)
        self.acceleration = vec(0,0)
        self.do_gravity = True
        # self.mass = 1
        self.max_acceleration = 4

    def get_input(self) :

        # self.velocity.y = 0 
        self.acceleration.x , self.acceleration.y =  0 , 0
        # self.delpos.x , self.delpos.y  = 0 , 0 
        keys = pygame.key.get_pressed()
        if keys[self.move_right_key] :
            self.acceleration.x += 1
        if keys[self.move_left_key] :
            self.acceleration.x -= 1
        if keys[self.jump_key] and self.velocity.y == 0 :
            # print("colliderect")
            self.velocity.y -= 9

    def horizontal_movement(self) :
        self.acceleration.x += self.velocity.x * -.10
        self.velocity.x += self.acceleration.x * dt
        self.delpos.x = self.velocity.x *dt + ((self.acceleration.x *0.5) * (dt * dt))
        self.px = self.rect.x + self.delpos.x
        self.rect.x = round(self.px)
        hitx = pygame.sprite.spritecollide(self,self.collidelist, False)
        if hitx :

            ## Warning : The player-player collision part has been removed and no longer will be implemented
            # if hitx[0].name in player_group.sprites() :
            #     print("hoho")
                # hitx[0].velocity.x =  self.velocity.x
            if hitx[0].name == "platform6" :
                self.rect.move_ip(hitx[0].velocity, 0)
            if self.delpos.x > 0 :    
                self.rect.right = hitx[0].rect.left
            if self.delpos.x < 0 :    
                self.rect.left = hitx[0].rect.right

    def vertical_movement(self) :
        global player_group
        self.acceleration.y = 0.4
        self.velocity.y += self.acceleration.y
        self.delpos.y = self.velocity.y + (0.5 * self.acceleration.y)
        self.rect.y += self.delpos.y
        hity = pygame.sprite.spritecollide(self, self.collidelist, False)
        if hity :
            ## Warning : The player-player collision part has been removed and no longer will be implemented
            # if hity[0].name in player_group.sprites() :
            #      hity[0].velocity.y += self.velocity.y
            if self.delpos.y > 0 :
                self.velocity.y = 0
                self.rect.bottom = hity[0].rect.top
            if self.delpos.y < 0 :
                # self.velocity.y *= -1 
                self.rect.top = hity[0].rect.bottom
    def move(self) :
        self.get_input()
        self.horizontal_movement()
        self.vertical_movement()
    def debug(self) :
        print(self.rect.topleft , self.position , self.velocity , self.acceleration , sep = "\t")

run = True
player = Entity("blue")
player.name = "Player1"
player.jump_key = pygame.K_UP
pl = Entity("red")
pl.name = "Player2"
pl.move_right_key = pygame.K_d
pl.move_left_key = pygame.K_a
pl.jump_key = pygame.K_w
border = border(-1280,0,1280*2,720)
platform1 = Platform(-1280,690,1280*5,30,(255,20,0))
platform2 = Platform(200, 600, 100, 50, (255,20,0))
# platform3 = Platform(400, 500, 100, 50, (255,255,0))
platform4 = Platform(180, 500, 100, 50, (0,255,0))
platform5 = Platform(700, 600, 100, 50,(0,255,255))
platform6 = Platform(800, 600, 100, 50, 'cyan')




player_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
platform_group.add(platform1,platform2,platform4,platform5 , platform6)
player_group.add(player , pl)
player.collidelist.add(pl , *platform_group.sprites())
pl.collidelist.add(player , *platform_group.sprites())


while run :
    # clock.tick(120)
    dt = (clock.tick(60) /1000) * 60
    # player.debug()

    # pause()
    player.move() ; pl.move()
    platform6.move(700, 1100, 1)

    win.fill((255,255,255))
    platform_group.draw(win)
    player_group.draw(win)
    pygame.display.flip()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
            pygame.quit()
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
            pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b :
            print("Player1")
            print(pl.rect.topleft , pl.position , pl.velocity , pl.acceleration , sep = "\t")
            print("Player2")
            print(player.rect.topleft , player.position , player.velocity , player.acceleration , sep = "\t")
        if event.type == pygame.MOUSEBUTTONDOWN :
            print(pygame.mouse.get_pos())

