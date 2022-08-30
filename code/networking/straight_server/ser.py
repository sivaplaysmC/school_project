import socket
from pickle import loads as lo , dumps as du 
# import pickle
from por  import p


s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.bind(('localhost' , p) )
s.listen(2)

connections = []
messages = []
errors = [EOFError , BrokenPipeError  , ConnectionResetError ]


while True :
    while len(connections) <  2 :
        con , add = s.accept()
        connections.append(con)
        con.send(du("Hi waiting for other player"))
    # s.sendall("Hello".encode())
    for j  in range(len(connections)):
        connections[j]:socket.socket
        try : 
            # connections[j].send(du("Hello"))
            print(lo(connections[j].recv(2048)))
             
        except BrokenPipeError   :
            connections.pop(j)
        except ConnectionResetError : 
            pass
        except EOFError : 
            pass

        #TODO : Address EOFError caused by loads function ^_^

