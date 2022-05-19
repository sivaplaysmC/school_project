import pygame
pygame.init()
win = pygame.display.set_mode((800,600))
fps = 60
run = True
clock = pygame.time.Clock()
player_pos = pygame.math.Vector2(100,100)
player_acc = pygame.math.Vector2(0,0)
player_vel = pygame.math.Vector2(0,0)
pos_change = pygame.math.Vector2(0,0)

image = pygame.Surface((50,50))
image.fill((0,255,255))
while run :
    clock.tick(fps)
    dt = clock.tick(fps) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b :
            print(player_acc , player_pos , player_vel)

    keys = pygame.key.get_pressed()
    player_acc = pygame.math.Vector2(0,0)
    if keys[pygame.K_RIGHT] :
        player_acc.x += 1
    if keys[pygame.K_LEFT] :
        player_acc.x -= 1

    player_acc.x += player_vel.x * -1
    player_vel += player_acc
    player_pos += player_vel + 0.5 * (player_acc)

    # pos_change.x = player_vel.x + 0.5 * player_acc.x
    # pos_change.y = player_vel.y  + 0.5 * player_acc.y
    #
    # player_pos += pos_change
    player_acc.x , player_acc.y  = 0,0
    # player_vel.x , player_vel.y = 0,0

    win.fill((255,255,255))
    win.blit(image  , (player_pos.x , player_pos.y))
    pygame.display.flip()
