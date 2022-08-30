import socket
import time
import pickle
from port import p
import threading
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM )


def send_val(c : socket.socket) :
    while True : 
        data = c.recv(2048)
        data = [i*2 for i in pickle.loads(data) ]
        print(data)
        print(pickle.loads(pickle.dumps(data)))
        time.sleep(0.0000000000000000000001)
        c.send(pickle.dumps(data))
server.bind(('localhost' , p))
server.listen( )
while True : 
    c ,a = server.accept()
    threading.Thread(target=send_val , args=(c,)).start()
