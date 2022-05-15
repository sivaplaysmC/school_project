import pygame , time , sys

pygame.init()
win = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
framerate = 60

acceleration = 0
velocity = 0
position = 10

is_jumping = False

rect = pygame.Rect(position,360,50,50)
while True:
    rect.move_ip(0,10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(framerate)
    acceleration = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        acceleration += 1
    if keys[pygame.K_LEFT] :
        acceleration -= 1
    if not is_jumping :
        if keys[pygame.K_SPACE] :
            rect.move_ip(0,1)
            is_jumping = True
        else :
            is_jumping = False
    # if abs(acceleration) > 10 :
    acceleration += velocity * -0.025
    velocity += acceleration
    position += velocity + 0.5 * acceleration
    rect.update(position , 360 , 50 , 50 )
    
    rect.midbottom = rect.topleft
    print(rect.y)
    win.fill('white')
    pygame.draw.rect(win,'red',rect)
    pygame.display.flip()
