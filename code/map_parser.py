<<<<<<< HEAD:map_parser.py
import csv

def main():
    x = []
    returnable = tuple()
    with open (r"csv\sample.csv" , "r" ) as f :
        for i in f :
            x.append(i)

    for j in x :
        returnable+=(eval(j.strip("\n")),)
    return returnable
=======
import csv

def main():
    x = []
    returnable = tuple()
    with open (r"G:\school_project\csv\sample.csv" , "r" ) as f :
        for i in f :
            x.append(i)

    for j in x :
        returnable+=(eval(j.strip("\n")),)
    return returnable
>>>>>>> fd21dd7a4035172c0f18dede42566ed89b2bb72c:code/map_parser.py
