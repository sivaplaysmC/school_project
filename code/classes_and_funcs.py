from time import time as t 
import pygame
from pygame import Vector2 as vec

class border(pygame.Rect) :
    def __init__(self , x , y , w , h ) :
        pass
def command_console(win , Player1 , Player2 ) :
    command_console_screen =  pygame.image.load(r"console.png").convert_alpha()
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
        win.blit(pygame.transform.scale(command_console_screen, (win.get_width(), win.get_height() )), (0,0))
        win.blit(font.render(string, True, 'black'), ( 600 ,win.get_height() / 2  ))
        pygame.display.flip()


def pause(win) :
    pause_screen = pygame.image.load(r"pause_menu.png").convert_alpha()
    n = t()
    print(n)
    paused = True
            
    win.blit(pygame.transform.scale(pause_screen, (win.get_width(), win.get_height() )), (0,0))
    while paused :
        pygame.display.flip()
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused = False
            if event.type == pygame.QUIT :
                paused = False
                pygame.quit()
                raise SystemExit(0)
    o = t()
    print(o)
    print(o - n)
    return  o - n  
class Platform(pygame.sprite.Sprite) :
    def __init__(self , x , y , w , h , color):
        super().__init__()
        self.image = pygame.Surface((w , h))
        self.image.fill(color)
        self.name = "Platform"

        self.rect = self.image.get_rect()
        self.rect.update(x , y , w , h )
        
class Entity(pygame.sprite.Sprite) :
    def __init__(self , color):
        super().__init__()
        self.color = color
        self.image = pygame.Surface((30,30))
        self.image.fill(self.color)
        self.px , self.py = 0 , 0 
        self.name = str() 
        self.other_player_name = str()

        self.collidelist = pygame.sprite.Group()

        self.move_right_key = pygame.K_RIGHT
        self.move_left_key  = pygame.K_LEFT
        self.jump_key = pygame.K_SPACE
        self.actions = {"left" : False , "right" : False, "jumping" : False , "idle" : False}
        self.rect = self.image.get_rect()
        self.rect.x = 226
        self.rect.y = 470
        self.hitx , self.hity = list() , list()

        self.position = vec(500,500)
        self.delpos = vec(0,0)
        self.velocity = vec(0,0)
        self.acceleration = vec(0,0)
        self.do_gravity = True
        # self.mass = 1
        self.max_acceleration = 4

    def get_input(self) :

        # self.velocity.y = 0 
        self.acceleration.x , self.acceleration.y =  0 , 0
        # self.delpos.x , self.delpos.y  = 0 , 0 
        keys = pygame.key.get_pressed()
        if keys[self.move_right_key] :
            self.acceleration.x += 0.5
        if keys[self.move_left_key] :
            self.acceleration.x -= 0.5
        if keys[self.jump_key] and self.velocity.y == 0 :
            # print("colliderect")
            self.velocity.y -= 10
        # for event in pygame.event.get() :
        #     if event.type == pygame.KEYDOWN and event.key == self.jump_key and self.velocity == 0 :
        #         print(self.name , "jumped")
        #         self.velocity.y -= 9

    def horizontal_movement(self,dt) :
        if self.velocity.x > 1.6 :
            self.velocity.x = 1.6
        self.acceleration.x += self.velocity.x * -.50
        self.velocity.x += self.acceleration.x * dt
        self.delpos.x = self.velocity.x *dt + ((self.acceleration.x *0.5) * (dt * dt))
        self.px = self.rect.x + self.delpos.x
        self.rect.x = round(self.px)
        hitx = pygame.sprite.spritecollide(self,self.collidelist, False)
        if hitx :

            ## Warning : The player-player collision part has been removed and no longer will be implemented
            ## Nah No error can stop siva from implementing siva's ideas in his own game 
            ## where else will he add them ??
            if hitx[0].name == self.other_player_name : 
                # print("hoho")
                hitx[0].rect.move_ip(self.delpos.x , 0)
                self.rect.x = hitx[0].rect.left
            if self.delpos.x > 0 :    
                self.rect.right = hitx[0].rect.left
            if self.delpos.x < 0 :    
                self.rect.left = hitx[0].rect.right

    def vertical_movement(self,dt) :
        self.acceleration.y = 0.4
        self.velocity.y += self.acceleration.y
        self.delpos.y = self.velocity.y + (0.5 * self.acceleration.y)
        self.rect.y += self.delpos.y
        hity = pygame.sprite.spritecollide(self, self.collidelist, False)
        if hity :
            ## Lol i added the player-player collsion somehow 
            ## Warning : The player-player collision part has been removed and no longer will be implemented
            # if hity[0].name in player_group.sprites() :
            #      hity[0].velocity.y += self.velocity.y
            if self.delpos.y > 0 :
                self.velocity.y = 0
                self.rect.bottom = hity[0].rect.top
            if self.delpos.y < 0 :
                self.velocity.y *= -0.1
                self.rect.top = hity[0].rect.bottom
    def move(self,dt) :
        """ Do Some Movement ^_^  """
        self.get_input()
        self.horizontal_movement(dt)
        self.vertical_movement(dt)
    def debug(self) :
        print(self.rect.topleft , self.position , self.velocity , self.acceleration , sep = "\t")
