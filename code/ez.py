import pygame

pygame.init()

win = pygame.display.set_mode((1280,720))

run = True

rect = pygame.Rect(100, 200, 50, 50)
while run == True :
    for event in pygame.event.get() :
        # print(event)
        if event.type == pygame.QUIT :
            run = False
    win.fill((0,0,153))
    pygame.draw.rect(win, (250,250,250), rect)
    pygame.display.update()


