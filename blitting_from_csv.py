import pygame

pygame.init()

win = pygame.display.set_mode((1280 , 720))

clock = pygame.time.Clock()

run = True

while run :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False

    win.fill((128 , 128 , 128))
    pygame.display.flip()    
