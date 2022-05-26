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


class Player(pygame.sprite.Sprite) :
    global Platforms
    def __init__(self) :
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill((0,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((640,360))

        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.coeff = 0
        self.acceleration = vec(0,0)
        self.velocity = vec(0,0)
        self.position = vec(640,360)
        self.mass = 1
    def gravity(self) :
        self.acceleration = vec(0,0.1)
    def movement(self) :
        self.collision()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] :
            self.acceleration.x += 1
        if keys[pygame.K_LEFT] :
            self.acceleration.x += -1

        self.acceleration.x += self.velocity.x * -0.1
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt + (self.acceleration) * (0.5 * dt * dt)

        bruh = self.position.y + 50
        if bruh > HEIGHT :
            # print("Ha")
            self.velocity.y = 0
            self.position.y = HEIGHT - 50
        self.rect.topleft = self.position
    def collision(self) :

        x = pygame.sprite.spritecollide(self , Platforms , dokill = False)
        for y in x :
            if abs(self.rect.bottom  - y.rect.top)<=10:
                self.position.y = y.rect.top - 49
                self.velocity.y = 0

        else :
            self.gravity()
    def check_and_move(self , dx , dy) :
        move_in_x , move_in_y = True , True
        x_i , y_i = 1,1
        while move_in_x :
            if x_i <= dx :
                y = self.rect.move(0,0)
                for i in Platforms.getsprites : pass

        ##  YOU HAVE TO ADD THE CHECK AND MOVE FUNCTIONALITY
        ##  ie , YOU HAVE TO MOVE ONE PIXEL IN X CHECK COLLISIONS ,
        ##  MOVE 1 PIXEL IN Y , CHECK COLLISIONS
        ##  TILL X AND Y MOVEMENT IS EQUAL TO PROVIDED PARAMS
        ##  IF ANY COLLISIONS , ABORT MOVEMENT IN THAT SPECIFIC DIRECTION

player = Player()
platform = Platform(500 , 500 , 200 , 30)
_platform = Platform(710 , 550 , 200 , 30)
player_group = pygame.sprite.Group()
Platforms = pygame.sprite.Group()
player_group.add(player)
Platforms.add(platform , _platform)
y = copy(player)
print(player.rect)
y.rect.move_ip(10,10)
print(player.rect)
print(id(player.rect) , id(y.rect) )
run = True
while run :
    dt = (clock.tick(30) /1000) * 60
    for event in pygame.event.get() :
        # print(event)
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b :
            print("=" * 14)
            print(player.acceleration)
            print(player.velocity)
            print(player.position)

            print("=" * 14)
    # print(player.position.y , WIDTH)
    player.movement()
    print(player.collision())
    win.fill((255,255,255))
    player_group.draw(win)
    Platforms.draw(win)
    pygame.display.flip()
