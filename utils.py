class Vector() :
    def __init__(self , x = 0 , y = 0 ) :
        self.x = x
        self.y = y

    def get_vector(self) :
        return (self.x , self.y)
    def reset(self) :
        self.x , self.y  = 0,0

class Stack(list) :
    def __init__(self) :
        super().__init__()
    def add(self , data) :
        self.append(data)
    def peek(self ) :
        return self[-1]
    def max_index(self) :
        return len(self) - 1
