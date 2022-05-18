import pygame , random
from pygame import Vector2 as vec


pygame.init()
WIDTH = 1280
HEIGHT = 720
win = pygame.display.set_mode((WIDTH , HEIGHT))
clock = pygame.time.Clock()
border = pygame.Rect(0,0,WIDTH , HEIGHT)
class Player(pygame.sprite.Sprite) :
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

        self.acceleration = vec(0,0.5)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] :
            self.acceleration.x += 1
        if keys[pygame.K_LEFT] :
            self.acceleration.x += -1

        self.acceleration.x += self.velocity.x * -0.1
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt + (self.acceleration) * (0.5 * dt * dt)

        self.rect.center = self.position

    def in_air(self) :
        if player.rect.bottom >= border.bottom :
            return False
        else :
            return True
    def gravity(self) :
        if self.in_air() :
            self.position.y += 10
            self.rect.topleft = self.position
        else :
            player.rect.bottom = HEIGHT
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

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
    # keys = pygame.key.get_pressed()
    # # print(keys)
    # if keys[pygame.K_LEFT] :
    #     player.movement("left")
    # if keys[pygame.K_RIGHT] :
    #     player.movement("right")


    # print(player.in_air())
    player.movement()
    win.fill((255,255,255))
    player_group.draw(win)
    pygame.display.flip()
