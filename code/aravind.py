b = ord("A")
c = 1 
print(chr(b))
print(chr(b+1),chr(b+2))
print(chr(b+3),chr(b+4),chr(b+5))
for i in range(0 , 3 ) :
    for j in range(i,i+c) :
        print(chr(j+b) , end = " ")
    c+=1
    print()

