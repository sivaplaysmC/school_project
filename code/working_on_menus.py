import pygame
from pygame.constants import RESIZABLE 
from reading_json import rect_list
pygame.init()
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
WIDTH = 1408
HEIGHT = 736
hoho = pygame.display.set_mode((1280,700) , RESIZABLE)
win = pygame.Surface((WIDTH , HEIGHT))
clock = pygame.time.Clock()
from classes_and_funcs import Entity , Platform , command_console , pause



Player1 = Entity("blue")
Player1.name = "Player1"
Player1.jump_key = pygame.K_UP
Player1.other_player_name = "Player2"
Player2 = Entity("red")
Player2.name = "Player2"
Player2.move_right_key = pygame.K_d
Player2.move_left_key = pygame.K_a
Player2.jump_key = pygame.K_w
Player2.other_player_name = "Player1"
player_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
player_group.add(Player1 , Player2)
for i in rect_list :
    platform_group.add(Platform(i.x, i.y, i.w, i.h, "black"))
Player1.collidelist.add(Player2 , *platform_group.sprites())
Player2.collidelist.add(Player1 , *platform_group.sprites())
print(len(platform_group.sprites()))
pause_clock= pygame.time.Clock()
reduction = 0 
pause_time = 0 
run = True
while run :
    dt = (clock.tick(60) /1000) * 60
    dt = dt - pause_time
    pause_time = 0 
    # Player1.debug()

    # pause()
    Player1.move(dt) ; Player2.move(dt)
    # platform6.move(700, 1100, 1)

    win.fill((255,255,255))
    platform_group.draw(win)
    player_group.draw(win)
    pygame.transform.scale(win , (1200,700))
    hoho.blit( pygame.transform.scale(win , (hoho.get_width() , hoho.get_height())), (0,0))
    pygame.display.flip()
    for event in pygame.event.get() :
        
        if event.type == pygame.QUIT :
            pygame.quit()
            raise SystemExit(0)
       
        
        if event.type == pygame.KEYDOWN  :
            if event.key == pygame.K_BACKQUOTE :
                command_console(hoho,Player1,Player2)
            if event.key == pygame.K_ESCAPE :
                pause_time = pause(hoho)
                print("pause_time = ",pause_time)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b :

#the holy line 
            print("Player1",Player1.color)
            print(Player1.rect.topleft , Player1.position , Player1.velocity , Player1.acceleration , sep = "\t")
            print("Player2",Player2.color)
            print(Player2.rect.topleft , Player2.position , Player2.velocity , Player2.acceleration , sep = "\t")
        if event.type == pygame.MOUSEBUTTONDOWN :
            print(pygame.mouse.get_pos())


