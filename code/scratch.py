import pygame
from pygame import Vector2 as vec 
pygame.init()

win = pygame.display.set_mode((1000,800))
clock = pygame.time.Clock()

class Platform(pygame.sprite.Sprite) :
    def __init__(self , x , y, w , h ,color) :
        super().__init__()
        self.color = color
        if not self.color :
            self.color = 'red'
        self.image = pygame.Surface((w,h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x , self.rect.y = x,y 

class Player(pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill((200,100,150))
        self.rect = self.image.get_rect()
        self.rect.x ,self.rect.y = 500 ,400
        self.acc = 1 
        self.is_moving_in_x = False
        self.is_moving_in_x = False
        self.dummy_velocity = 0 

        
        self.acceleration = vec(0,0)
        self.velocity = vec(0,0)
        self.delpos = vec(0,0)

        self.friction = -0.5
    def horizontal_movement(self):
        self.delpos.x = 0
        self.acceleration.x = 0 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] :
            self.acceleration.x -= self.acc
        if keys[pygame.K_RIGHT] :
            self.acceleration.x += self.acc
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x
        self.delpos.x = self.velocity.x + (0.5 * ( self.acceleration.x * self.acceleration.x ))
        self.rect.x += self.delpos.x
        if self.delpos.x != 0 :
            hits = pygame.sprite.spritecollide(player, platforms, False)
            if hits :
                if self.delpos.x > 0 :
                    self.velocity.x = 0 
                    self.rect.x = hits[0].rect.x - 50
                if self.delpos.x < 0 :
                    self.velocity.x = 0 
                    self.rect.x = hits[0].rect.right

    def vertical_movement(self):
        self.delpos.y += 0.1
        global base_platfom
        # for event in pygame.event.get() :
        #     if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
        #         self.delpos.y -= 10 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] :
            if player.rect.colliderect(base_platfom):
                print("colliderect")
                self.delpos.y -= 100 
        if self.delpos.y < -5 :
            self.rect.y = -5
        self.rect.y += self.delpos.y

        hity = pygame.sprite.spritecollide(player, platforms, False)
        if hity :
            if player.delpos.y > 0 :
                self.delpos.y = 0 
                player.rect.bottom = hity[0].rect.top
            elif player.delpos.y < 0 :
                player.delpos.y = 0 
                player.rect.top = hity[0].rect.bottom 


player = Player()
top = Platform(0, 0, 3000, 100,'blue')
right = Platform(750, 0, 50, 1000,'red')
base_platfom = Platform(0, 750 ,3000,100 , 'green')
platform = Platform(100,400,100,100,'yellow')
plat = Platform(700,400,100,100,'black')
platforms = pygame.sprite.Group()
platforms.add(platform,plat,base_platfom,top,right)
player_group = pygame.sprite.Group()
player_group.add(player)
run = True
while run :
    clock.tick(60)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b :
            print(player.rect.x , player.rect.y , player.acceleration , player.velocity , player.delpos , player.dummy_velocity ,  sep = "  ")
    win.fill((255,255,255))
    player.vertical_movement()
    player.horizontal_movement()
    platforms.draw(win)
    player_group.draw(win)
    pygame.display.flip()

