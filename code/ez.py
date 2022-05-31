import pygame

pygame.init()

win = pygame.display.set_mode((1280,720))

run = True

while run == True :
    for event in pygame.event.get() :
        # print(event)
        if event.type == pygame.QUIT :
            run = False
    win.fill((0,0,153))
    pygame.display.update()
