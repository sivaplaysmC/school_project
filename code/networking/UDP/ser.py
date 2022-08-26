import socket
from por import p


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(('localhost'  , p) )


while 1 : 
    print(s.recvfrom(2048)[0].decode())
    print("Hi")

    
    
