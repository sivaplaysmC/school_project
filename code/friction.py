import math



def Friction(acc) : 
    if acc >= 0 :
        return -(math.fabs(acc) * 0.2)
    if acc < 0 :
        return (math.fabs(acc) * 0.2 )
    return 1.0
