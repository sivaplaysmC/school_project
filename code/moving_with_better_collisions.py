import pygame
from pygame import Vector2 as vec

pygame.display.init()

win = pygame.display.set_mode((1280,720))

class Player(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()

        self.image = pygame.Surface((50,50))
        self.image.fill((0,255,255))
        self.rect = self.image.get_rect()

        self.velocity = vec(0,0)
        self.delpos = vec(0,0)
        self.acceleration = vec(0,0)
        self.position = vec(100,400)
        self.rect = self.position
    def horizontal_movement(self) :
        self.acceleration.x = 0 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] :
            self.acceleration.x += 3
        if keys[pygame.K_LEFT] :
            self.acceleration.x += -3
        self.acceleration.x += self.velocity.x * -0.9
        self.velocity.x += self.acceleration.x
        self.delpos.x = self.velocity.x + ( 0.5 * self.acceleration.x )
        self.position.x += self.velocity.x + ( 0.5 * self.acceleration.x )
        hits = pygame.sprite.spritecollide(player, platform_group, dokill)
       
        # if pygame.sprite.spritecollide(player, , dokill)
    def move(self) :
        player.horizontal_movement()
        self.rect = self.position
player = Player()
Player_group = pygame.sprite.Group()
Player_group.add(player)

run = True 
while run :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b :
            print(player.acceleration , player.velocity , player.position )
    win.fill((255,255,255))
    player.move()
    Player_group.draw(win)
    pygame.display.flip()

