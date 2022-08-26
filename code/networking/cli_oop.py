
from utils import Stack
from gamestates  import Main_menu  , Pause_menu , GameState, client_basic
from reading_json  import rect_list
from entity  import Platform
import pygame
import socket
from por  import p
from pickle import loads as lo , dumps as du

c = socket.socket()

# c.connect(('localhost' ,  p))
#
# while 1:
#     print(lo(c.recv(2048)))
#     c.send(du("Hi from client1"))

class Client ():
    """docstring for Client ."""

    global rect_list

    def __init__(self):
        super(Client , self).__init__()
        # self.color = color
        self.display = pygame.display.set_mode((1280,720))
        self.environment = pygame.Surface((1280 , 720 ))
        self.drawables = list[client_entity]()
        self.player = client_entity(color="red")
        self.drawables.append(self.player)
        self.game_state_stack = Stack()
        self.game_state_stack.add(Main_menu(self))
        self.drawables.append(self.player)
        for i in rect_list :
            self.drawables.append(client_platform(i.x , i.y , i.w , i.h , ))
        self.running = True


        self.soc = socket.socket()
        self.soc.connect(('localhost' , p))


    def send_data(self) :
        self.soc.send(du(self.player.actions))
        # print(du(self.player.actions))


    def get_input(self) :
        for self.event in pygame.event.get() :
            if self.event.type == pygame.QUIT :
                self.running = False
            if self.event.type == pygame.KEYDOWN :
                if self.event.key == pygame.K_RETURN and self.game_state_stack.peek().name != "Clie" :
                    print("Hi")
                    print(self.game_state_stack.peek())
                    self.game_state_stack.add(client_basic(self))
                if self.event.key == pygame.K_UP :
                    self.player.actions["up"] = True
                if self.event.key == pygame.K_RIGHT :
                    self.player.actions["right"] = True
                if self.event.key == pygame.K_LEFT :
                    self.player.actions["left"] = True

            if self.event.type == pygame.KEYUP :
                if self.event.key == pygame.K_UP :
                    self.player.actions["up"] = False
                if self.event.key == pygame.K_RIGHT :
                    self.player.actions["right"] = False
                if self.event.key == pygame.K_LEFT :
                    self.player.actions["left"] = False

    def draw(self) :
        self.display.blit(pygame.transform.scale(self.environment , ( self.display.get_width() , self.display.get_height()  )) , (0,0))
        self.game_state_stack.peek().update()
        pygame.display.flip()
    def mainloop(self) :
        while self.running :
            self.get_input()
            self.draw()
            # print(self.player.rect.topleft)
            self.send_data()



class client_entity():
    """docstring for client_entity."""
    def __init__(self , color='black'):
        super(client_entity, self).__init__()
        self.color = color
        self.pos = pygame.Vector2()
        self.pos.x , self.pos.y = 700,300
        self.image = pygame.Surface((50,50))
        self.rect = pygame.Rect(self.pos.x , self.pos.y , 50 , 50 )
        # self.rect.update(self.pos.x , self.pos.y , 50 , 50 )
        self.image.fill(color)
        print(type(self.image))
        self.actions = {"right" : False , "left" : False , "up" : False}
    # def draw(self) :

# class client_platform(client_entity):
#     """docstring for client_platform."""
#     def __init__(self , x,y , w , h ):
#         super(client_platform, self).__init__()
#         self.x =x
#         self.y =y
#         self.w =w
#         self.h =h
#         self.image = pygame.Surface(self.w , self.h)
#         self.rect = pygame.Rect(self.)

c = Client()
c.mainloop()
c.send_data()
