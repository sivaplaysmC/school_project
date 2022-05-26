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
