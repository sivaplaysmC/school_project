import socket
# import _thread as t 
import threading


def haha():
    conn = socket.socket(socket.AF_INET , socket.SOCK_STREAM) 
    ip = "localhost" ; port = 6968
    conn.bind((ip , port))
    print(f"server to {ip , port}")
    conn.listen(2)
    conne , addr = conn.accept()
    with conn :
        # print(conn  , addr)
        print(f"connected by {addr}")
        while True :
            data = conne.recv(1024)
            print("Hoho")
            print("Hoho")
            stri = data.decode()
            stri = stri.strip("\n")
            print(f"Receieved {stri}")
            if not data :
                break
            inp = ("You Said " + data.decode("UTF-8")).encode()
            conne.sendall(inp)



t = threading.Thread(target=haha)
# conn.close()
t.start()
