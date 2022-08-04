from friction import Friction
from typing import Tuple
import pygame

# class Entity(pygame.sprite.Sprite) :
#     def __init__(self , color , spawn : Tuple) -> None:
#         self.color = color
#         self.image = pygame.Surface((50,50))
#         self.rect  = self.image.get_rect()
#         self.rect.x = spawn[0]
#         self.rect.y = spawn[1]
#         self.acceleration = pygame.math.Vector2()
#         self.velocity = pygame.math.Vector2()
#         self.delpos = 1

class Platform(pygame.sprite.Sprite) :
    def __init__(self , x , y , w , h , color):
        super().__init__()
        self.image = pygame.Surface((w , h))
        self.image.fill(color)
        self.name = "Platform"

        self.rect = self.image.get_rect()
        self.rect.update(x , y , w , h )
class Simple (pygame.sprite.Sprite) :
    
    def __init__(self , color , spawn : Tuple ) -> None:
        super().__init__()
        self.name = str(self)
        self.spawn = spawn
        self.color = color
        self.image =pygame.image.load(r"console.png").convert_alpha() 
        self.image = pygame.transform.scale(self.image , (50 , 50 ))
        self.rect  = self.image.get_rect()
        self.rect.x = spawn[0]
        self.rect.y = spawn[1]
        self.acceleration = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.delpos =pygame.math.Vector2() 
        self.velocity.x , self.velocity.y = 0 , 0 
        self.actions = {"right" : False , "left" : False , "up" : False}
        # self.collidelist = self.Game.

        self.jump_key = pygame.K_UP
        self.other_player_name = str()
        self.move_right_key = pygame.K_RIGHT
        self.move_left_key  =pygame.K_LEFT

    def in_contact(self) :
        for i in self.collidelist :
            # print(i)
            if self.rect.colliderect(i.rect) :
                print("collided")
                return True
        return False
    def horizontal(self, dt ) :
        self.mul = 60/(1/dt) 
        self.velocity.x += self.acceleration.x - Friction(self.acceleration.x)
        self.velocity.x += self.acceleration.x * self.mul
        self.delpos.x = ( self.acceleration.x  * 0.5 * self.mul * self.mul)  + self.velocity.x * self.mul   
        self.rect.x  += self.delpos.x
        for i in self.collidelist : 
            i : pygame.sprite.Sprite = i 
            if i.rect.colliderect(self.rect) :
                if self.delpos.x >= 0 :
                    self.rect.right = i.rect.left
                if self.delpos.x < 0 :
                    self.rect.left = i.rect.right
    def vertical(self, dt) :
        self.mul = 60/(1/dt) 
        self.acceleration.y = 4.0
        self.velocity.y += self.acceleration.y - Friction(self.acceleration.y)
        self.velocity.y += self.acceleration.y * self.mul
        self.delpos.y = ( self.acceleration.y  * 0.5 * self.mul * self.mul)  + self.velocity.y * self.mul   
        self.rect.y  += self.delpos.y
        for i in self.collidelist : 
            i : pygame.sprite.Sprite = i 
            if i.rect.colliderect(self.rect) :
                if self.delpos.y >= 0 :
                    self.rect.bottom = i.rect.top
                if self.delpos.y < 0 :
                    self.rect.top = i.rect.bottom
    def move(self,dt , collidelist) :
        self.acceleration = pygame.math.Vector2(0,0)
        self.collidelist = collidelist
        if self.actions["right"] : self.acceleration.x += 2
        if self.actions["left"] : self.acceleration.x -= 2
        # print(self.velocity.y) 
        # if self.in_contact() :
        if self.actions["up"] :
            print("One Up")
            # print("In Contact")
            # self.velocity.y -= 20 
            print(self.velocity.y)
            if  (self.velocity.y) == 0.0 : 
                self.velocity.y -= 20
        self.horizontal(dt)
        self.vertical(dt)
        self.velocity.x  ,self.velocity.y = 0 , 0 



class Entity(pygame.sprite.Sprite) :
    def __init__(self , color):
        super().__init__()
        vec = pygame.Vector2
        self.color = color
        self.image = pygame.Surface((30,30))
        self.image.fill(self.color)
        self.px , self.py = 0 , 0 
        self.name = str() 
        self.other_player_name = str()
        self.actions = {"right" : False , "left" : False , "up" : False}

        self.collidelist = pygame.sprite.Group()

        self.move_right_key = pygame.K_RIGHT
        self.move_left_key  = pygame.K_LEFT
        self.jump_key = pygame.K_SPACE

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
        if self.actions["right"] :
            self.acceleration.x += 0.8
        if self.actions["left"] :
            self.acceleration.x -= 0.8
        if self.actions["up"] and self.velocity.y == 0 :
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
