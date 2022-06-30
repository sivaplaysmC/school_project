import json

file =  r"G:\school_project\maps\better.json"

with open(file) as f :
    data = json.load(f)

x = data["layers"][0]["data"]
c = 1 
clean = list()
for i in x :
    for j in i :
        print(j, end=",")
    else :
        print("\n------------------------------------------")
    
