import pygame , random
from pygame import Vector2 as vec


pygame.init()
WIDTH = 1280
HEIGHT = 720
win = pygame.display.set_mode((WIDTH , HEIGHT))
clock = pygame.time.Clock()
border = pygame.Rect(0,0,WIDTH , HEIGHT)

class Platform(pygame.sprite.Sprite ,) :
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
    def movement(self) :
        if self.collision() :
            self.acceleration = vec(0,0)
        else :
            self.acceleration = vec(0,0.1)
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
        if x :
            # print("X true")
            # if self.position.y < x[0].rect.top :
            self.position.y = x[0].rect.top - 50
            self.velocity.y = 0
            return True
        else :
            return False
player = Player()
platform = Platform(500 , 500 , 200 , 30)
player_group = pygame.sprite.Group()
Platforms = pygame.sprite.Group()
player_group.add(player)
Platforms.add(platform)


run = True
while run :
    dt = (clock.tick(60) /1000) * 60
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
