# import blitting_text
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
# border = border(-1280,0,1280*2,720)
#platform1 = Platform(-1280,690,1280*5,30,(255,20,0))
#platform2 = Platform(200, 600, 100, 50, (255,20,0))
#platform3 = Platform(400, 500, 100, 50, (255,255,0))
#platform4 = Platform(180, 500, 100, 50, (0,255,0))
#platform5 = Platform(700, 600, 100, 50,(0,255,255))
#platform6 = Platform(800, 600, 100, 50, 'cyan')
player_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
#platform_group.add(platform1,platform2,platform4,platform5 , platform6)
player_group.add(Player1 , Player2)
for i in rect_list :
    platform_group.add(Platform(i.x, i.y, i.w, i.h, "black"))
Player1.collidelist.add(Player2 , *platform_group.sprites())
Player2.collidelist.add(Player1 , *platform_group.sprites())
print(len(platform_group.sprites()))
pause_clock= pygame.time.Clock()
reduction = 0 

run = True
while run :
    dt = (clock.tick(60) /1000) * 60
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
                command_console(hoho)
            if event.key == pygame.K_ESCAPE :
                pause(hoho)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b :
            print("Player1",Player1.color)
            print(Player1.rect.topleft , Player1.position , Player1.velocity , Player1.acceleration , sep = "\t")
            print("Player2",Player2.color)
            print(Player2.rect.topleft , Player2.position , Player2.velocity , Player2.acceleration , sep = "\t")
        if event.type == pygame.MOUSEBUTTONDOWN :
            print(pygame.mouse.get_pos())


