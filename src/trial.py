import pygame

image = pygame.Surface((100,100))
image.fill('grey')


temp = pygame.Surface((20,20))
temp.fill('black')

image.blit(temp , (20,20))

surface = pygame.Surface((1280 , 720))
surface.fill('white')
surface.blit(image , (640 , 360))


win = pygame.display.set_mode((1280 , 720))
win.fill('white')
win.blit(surface , (0,0))
pygame.display.flip()
while 1 :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT  :
            quit()
    pygame.display.flip()
