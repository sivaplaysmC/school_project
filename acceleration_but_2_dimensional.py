import pygame , sys
import pygame.math.Vector2 as vec
pygame.init()

win = pygame.display.set_mode((1280,720))

obj = pygame.Surface(50,50)
obj.fill("blue")

run = 1

acceleration  = vec(0,0)
velocity = vec(0,0)
position = vec(100,100)




while run :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = 0
            sys.exit()
    
    if keys[pygame.K_RIGHT] :
        acceleration.x += 1
    if keys[]


    win.fill((255,255,255))
    win.blit(obj , position)
    pygame.display.update()
