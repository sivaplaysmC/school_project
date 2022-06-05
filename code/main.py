import pygame

pygame.init()
width , height = 800,600
win = pygame.display.set_mode((width , height))

run = True

fps = 60

fps_clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite) :

    global dt , width , height

    def __init__(self , x , y , w , h ) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w , h))
        self.image.fill((0,255,255))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.acc = pygame.math.Vector2(1,0)

        self.w  = w
        self.h = h
        self.position = pygame.math.Vector2(x,y)
        self.velocity = pygame.math.Vector2(0,0)
        self.acceleration = pygame.math.Vector2(0,0)
    def move(self) :
        self.acceleration = pygame.math.Vector2(0,0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] :
            print("pressed")
            self.acceleration += self.acc
        if keys[pygame.K_LEFT]  :
            print("pressed")
            self.acceleration -= self.acc
        if self.acceleration.x > 0 :
            self.velocity += self.acceleration * dt
            self.position = self.velocity * dt + self.acceleration * (dt**2)
            self.acceleration.x -= 1
        if self.position.x > width :
            self.postion.x = 0
        if self.position.x < 0 :
            self.postion.x = width
        self.rect.update(self.position , (self.w , self.h ))
player = Player(100,100,50,50)
player_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player.add(player_group )

while run :
    fps_clock.tick(60)
    dt = (fps_clock.tick(fps))/1000
    win.fill((255,255,255))
    win.blit(player.image  , player.rect)
    player.move()
    pygame.display.flip()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b :
            print(player.acceleration , player.velocity , player.position )
