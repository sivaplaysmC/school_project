from itertools import cycle

lst1 = list(range(10,20))
lst2 = list(range(20,10,-1))
while True :
    while True :
        print(*lst1 , sep = "\n")
        break
    while True : 
        print(*lst2 , sep = "\n")
        break
