import pygame

win = pygame.display.set_mode((800,800))
# din = pygame.display.set_mode((400,400))
win.fill((255,255,255))
# din.fill(( 0,255,0 ))

x = 0 
y = 400 
background = pygame.Surface((1600,400))
background.fill((255,255,255))
image = pygame.Surface((100,100))
image.fill('blue')
background.blit(image, (1200,400))
win.blit(background, ( 0,0 ))
run = True
while run :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
           run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] :
        x+=5
    win.blit(background, (x,y))
    pygame.display.flip()






















































