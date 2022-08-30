from pickle import loads
import time
import socket
import pygame
from port  import p
from threading import Thread


environment = pygame.display.set_mode((500,500))

server = socket.socket(  socket.AF_INET ,socket.SOCK_STREAM)
server.bind(('localhost' ,  p))

img = pygame.Surface((50,50)) 
img.fill("blue")

def process_client_1 (c : socket.socket) :
    while True :
        playe = c.recv(102400)
        # print("hiua")
        time.sleep(0.0000000000000000000001)
        print(playe)
        playe = loads(playe)
        # print(type(playe))
        environment.blit(img , (playe.x , playe.y))
        pygame.display.flip()
        
server.listen()


while True : 
    c ,a = server.accept()
    # threading.Thread(target=send_val , args=(c,)).start()
    Thread(target=process_client_1 , args=(c,) ).start()
    # t.start()
    





        
