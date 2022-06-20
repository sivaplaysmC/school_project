# iLport blitting_text
import pygame , random 
# from reading_json import rect_list
from pygame import Vector2 as vec
from copy import copy
from classes import Entity , Platform
pygame.init()
WIDTH = 1408
HEIGHT = 736
win = pygame.display.set_mode((WIDTH , HEIGHT))
clock = pygame.time.Clock()
border = pygame.Rect(0,0,WIDTH , HEIGHT)

# def get_image(image , metadata) :


pause_screen = pygame.image.load(r"pause_menu.png").convert_alpha()
command_console_screen =  pygame.image.load(r"console.png").convert_alpha()


class border(pygame.Rect) :
    def __init__(self , x , y , w , h ) :
        pass
def command_console() :
    comm = True
    string = str()
            
    font = pygame.font.Font(None, 50)
    
    while comm :
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN : 
                if event.key == pygame.K_BACKQUOTE:
                    comm = False
                if event.unicode != "" :
                    if event.key == pygame.K_RETURN :
                        if string[:3] == "set" :
                            string = string.lstrip()
                            try : exec(string[4:])
                            except : print("Bad command")
                        string = str()
                    if event.unicode != '\r' and event.unicode != '`' :
                        string += event.unicode 
                        
            if event.type == pygame.QUIT :
                comm = False
                pygame.quit()
                raise SystemExit(0)
                run = False
        win.blit(command_console_screen, (0,0))
        win.blit(font.render(string, True, 'blue'), ( 400,400 ))
        pygame.display.flip()


def pause() :
    paused = True
            
    win.blit(pause_screen, (0,0))
    while paused :
        pygame.display.flip()
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused = False
            if event.type == pygame.QUIT :
                paused = False
                pygame.quit()
                raise SystemExit(0)
                run = False
      


run = True
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
# platform1 = Platform(-1280,690,1280*5,30,(255,20,0))
# platform2 = Platform(200, 600, 100, 50, (255,20,0))
# # platform3 = Platform(400, 500, 100, 50, (255,255,0))
# platform4 = Platform(180, 500, 100, 50, (0,255,0))
# platform5 = Platform(700, 600, 100, 50,(0,255,255))
# platform6 = Platform(800, 600, 100, 50, 'cyan')
player_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
# platform_group.add(platform1,platform2,platform4,platform5 , platform6)
player_group.add(Player1 , Player2)
# for i in rect_list :
#     platform_group.add(Platform(i.x, i.y, i.w, i.h, "black"))
Player1.collidelist.add(Player2 , *platform_group.sprites())
Player2.collidelist.add(Player1 , *platform_group.sprites())
print(len(platform_group.sprites()))

while run :
    dt = (clock.tick(60) /1000) * 60
    # Player1.debug()

    # pause()
    Player1.move() ; Player2.move()
    # platform6.move(700, 1100, 1)

    win.fill((255,255,255))
    platform_group.draw(win)
    player_group.draw(win)
    pygame.display.flip()
    for event in pygame.event.get() :
        
        if event.type == pygame.QUIT :
            pygame.quit()
            raise SystemExit(0)
            run = False
            pygame.quit()
        
        if event.type == pygame.KEYDOWN  :
            if event.key == pygame.K_BACKQUOTE :
                command_console()
            if event.key == pygame.K_ESCAPE :
                pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b :
            print("Player1")
            print(Player2.rect.topleft , Player2.position , Player2.velocity , Player2.acceleration , sep = "\t")
            print("Player1")
            print(Player1.rect.topleft , Player1.position , Player1.velocity , Player1.acceleration , sep = "\t")
        if event.type == pygame.MOUSEBUTTONDOWN :
            print(pygame.mouse.get_pos())

