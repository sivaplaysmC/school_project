import pygame 

pygame.init()

win = pygame.display.set_mode((1280,720))

run = True

while run == True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False

