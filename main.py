import pygame

pygame.init()

win = pygame.display.set_mode((800,600))

while run :
    for event in pygame.event.get :
        if event.type == pygame.QUIT :
            run = False
