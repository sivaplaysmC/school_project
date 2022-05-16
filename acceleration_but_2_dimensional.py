import pygame , sys
pygame.init()

win = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
obj = pygame.Surface((50,50))
obj.fill("blue")

run =1

acceleration  = [0,0]
velocity = [0,0]
position = [100,100]




while run :
    dt = clock.tick(60) / 1000
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = 0
            sys.exit()
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_RIGHT] :
        accelertion.x += 1
    if keys[pygame.K_LEFT] :
        acceleration.x -= 1 

    acceleration = [0,0.5]
    accelereation = acceleration - velocity
    velocity = velocity + acceleration *dt
    position = position + velocity * dt + ( acceleration * 0.5 ) * dt * dt

    win.fill((255,255,255))
    win.blit(obj , position)
    pygame.display.update()
