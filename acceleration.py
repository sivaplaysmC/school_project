import pygame , time , sys

pygame.init()
win = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
framerate = 60

x_acceleration = 0
x_velocity = 0
x_position = 10

y_acceleration = 9.8
y_velocity = 0
y_position = 360

is_jumping = False

rect = pygame.Rect(x_position,360,50,50)
while True:
    y_position += 1

    # rect.update(0,y_position , 50 , 50 )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(framerate)
    x_acceleration = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x_acceleration += 1
    if keys[pygame.K_LEFT] :
        x_acceleration -= 1
    # if not is_jumping :
    if keys[pygame.K_SPACE] :
        rect.move_ip(0,1000)
        is_jumping = True
    else :
        is_jumping = False
    # if abs(x_acceleration) > 10 :
    x_acceleration += x_velocity * -0.025
    x_velocity += x_acceleration
    x_position += x_velocity + 0.5 * x_acceleration
    rect.update(x_position , y_position , 50 , 50 )
    if y_position > 710 :
        y_position = 710
        # rect.update(rect.x , 710, rect.w , rect.h)
    else :
        y_acceleration += y_velocity * -0.025
        y_velocity += y_acceleration
        y_position += y_velocity + 0.5 * y_acceleration
        rect.update(x_position , y_position , 50 , 50 )


    rect.midbottom = rect.topleft
    print(rect.y , y_position)
    win.fill('white')
    pygame.draw.rect(win,'red',rect)
    pygame.display.flip()
