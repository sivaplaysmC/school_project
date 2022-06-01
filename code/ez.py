import pygame

pygame.init()


player = pygame.Rect(360, 360, 50, 50)
win = pygame.display.set_mode((1280,720))

run = True

rect = pygame.Rect(100, 200, 50, 50)
while run == True :
    for event in pygame.event.get() :
        # print(event)
        if event.type == pygame.QUIT :
            run = False
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] :
        player.x -= 10
    if keys[pygame.K_RIGHT] :
        player.x += 10




    win.fill((0,0,153))
    pygame.draw.rect(win, (250,250,250), player)
    pygame.display.update()


