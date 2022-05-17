import pygame , random

pygame.init()
WIDTH = 1280
HEIGHT = 720
win = win = pygame.display.set_mode((WIDTH , HEIGHT))

border = pygame.Rect(0,0,WIDTH , HEIGHT)
class Player(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill((0,255,255))

        self.rect = self.image.get_rect()
        self.rect.center = ((640,360))

        self.moving_right = False
        self.moving_left = True
        self.jumping = False

    def in_air(self) :
        if player.rect.bottom >= border.bottom :
            return False
        else :
            return True
    def gravity(self) :
        if self.in_air() :
            self.rect.move_ip(0,1)
        else :
            player.rect.bottom = HEIGHT
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

run = True
while run :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.KEYDOWN :
            # player.rect.move_ip(0,120)
            pass

    print(player.in_air())
    player.gravity()
    win.fill((255,255,255))
    player_group.draw(win)
    pygame.display.flip()
