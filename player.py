import pygame 
from utils import Vector 

class Player() :
    def __init__(self , color = 'red'  , spawn_pos = Vector(500  ,  500 ) , backend = False , id = 0 ) :
        self.backend = backend 
        self.id = id
        self.size = Vector(50,50)
        self.spawn_pos = spawn_pos
        if not self.backend :
            self.color =  color 
            self.image = pygame.Surface((self.size.get_vector()))
            self.image.fill(self.color)
        self.Rect = pygame.Rect( (self.spawn_pos.get_vector()) , (self.size.get_vector()) )
        self.pos  = Vector( *self.spawn_pos.get_vector())
        self.displacement = Vector(0,0)
        self.velocity = Vector(0,0)
        self.acceleration = Vector(0,0)
        self.friction = 0.5
        self.actions = {'right' : False , 'left' : False , 'up' : False , 'down' : False }

    def update(self , dt ) :
        self.process_actions()
        self.movement(dt)
##        self.horizontal_movement()
##        self.vertical_movement()
        


    def process_actions(self) :
        if self.actions['right'] :
            self.acceleration.x = 4.0
        if self.actions['left'] :
            self.acceleration.x = -4.0
        if self.actions['up'] :
            self.acceleration.y = -4.0
        if self.actions['down'] :
            self.acceleration.y = -4.0

    def movement(self , dt ) :
        self.horizontal_movement(dt)
        self.vertical_movement(dt)
        
    def horizontal_movement(self , dt ) :
        self.displacement.reset()
        self.velocity.x += self.acceleration.x * self.friction
        self.acceleration.x += self.velocity.x
        self.displacement.x = self.velocity.x + (0.5 * self.acceleration.x)

    def vertical_movement(self ,  dt ) :
        self.displacement.reset()
        self.velocity.y += self.acceleration.y * self.friction
        self.acceleration.y += self.velocity.y
        self.displacement.y = self.velocity.y + (0.5 * self.acceleration.y)

a = Player(color = 'red')
a.update(69)
