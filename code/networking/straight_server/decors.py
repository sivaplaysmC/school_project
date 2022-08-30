def check(func) :
    def inner(*args) :
        try : 
            print("In Decorator")
            func(*args)
        except : print("Error")
    return inner

@check
def haha() :
    print("hahaha")
    
haha()
