import pickle
import socket
import pygame
from pygame.math import Vector2
from porto import pair



class simple : 
    def __init__(self , color , x=100 , y = 100 ) -> None:
        self.color = color
        self.image = None
        self.x = x
        self.y = y
        self.name=str()
        self.rect = pygame.Rect(self.x , self.y , 50,50)
        self.actions = {"left" : False , "right" : False , "up" : False}
        self.velocity = Vector2()
    def move(self):
        if self.actions["right"] :
            self.rect.x += 10
        if self.actions["left"] :
            self.rect.x -= 10
        # print(self.rect.x , self.rect.y  )


s = socket.socket()
s.connect(('3.6.115.182' , 19944))
p1 = pickle.loads(s.recv(512))
p1.image = pygame.Surface((50,50))
p1.image.fill(p1.color)


display = pygame.display.set_mode((500,500))


def handshake() -> simple: 
    
    ## De Surfacing the player 

    temp1 = p1
    temp1.image = None



    s.send(pickle.dumps(temp1))
    temp2 =  pickle.loads(s.recv(1024))

    
    ## Re Surfacing the player 

    
    temp2.image = pygame.Surface((50,50))
    temp2.image.fill(temp2.color)
    return temp2

def redraw() : 
    display.fill('white')
    p1.image = pygame.Surface((50,50))
    p1.image.fill(p1.color)
    display.blit(p1.image , (p1.rect.x , p1.rect.y))
    display.blit(p2.image , (p2.rect.x , p2.rect.y))
    pygame.display.flip()
    
def get_input() : 
    global running , p1
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        if event.type == pygame.KEYDOWN : 
            print("HIT")
            if event.key == pygame.K_UP :
                p1.actions["up"] = True
            if event.key == pygame.K_RIGHT :
                p1.actions["right"] = True
            if event.key == pygame.K_LEFT :
                p1.actions["left"] = True
            if event.key == pygame.K_SPACE :
                p1.actions["punch" ]= True

        if event.type == pygame.KEYUP : 
            if event.key == pygame.K_UP :
                p1.actions["up"] = False
            if event.key == pygame.K_LEFT :
                p1.actions["left"] = False
            if event.key == pygame.K_RIGHT :
                p1.actions["right"] = False
            if event.key == pygame.K_SPACE :
                p1.actions["punch" ]= False
    print(p1.actions)


running = True

while running :
    pass
    # DONE p1 = recieve from server 
    # p2 = returned from sending p1 to the server , defined in a function that send first and returns socket.recv 
    p2 = handshake()
    get_input()
    p1.move()
    p1.name="1"
    p2.move()
    p2.name="2"
    # print(p1.name , p1.rect.topleft , sep = '\t')
    # print(p2.name , p2.rect.topleft , sep = '\t')
    redraw()
    
