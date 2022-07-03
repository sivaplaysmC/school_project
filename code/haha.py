import subprocess

p = subprocess.Popen("ls ~/Downloads/JetBrainsMono" , stdout=subprocess.PIPE, shell=True)


#print(type(p.communicate()))
#for i in p.communicate() :
#    print(i)
#    break

x = p.communicate()
x = str((x[0]))
#print(x.split(r"\n"))
for i in x.split(r"\n") :
    #i = i[1:]
    i = r"~/Downloads/JetBrainsMono/" + i
    r = subprocess.Popen(r"/home/sivaplays/patching/./font-patcher " + i.replace(" " , r"\ ") + r" --custom codicon.ttf" , stdout=subprocess.PIPE, shell=True)
    print(r.communicate())


#    print(i)
#    print("0000000000000" * 14 )
#    print(i.replace(" " , r"\ "))
#    subprocess.run(r"/home/sivaplays/patching/./font-patcher" , i , "--custom" , r"codicon.ttf")

#    print(i)
#    print(r"/home/sivaplays/patching/./font-patcher " + i.rstrip("b' ").replace(" " , r"\ ") + r" --custom codicon.ttf")
#    print(i)
#    print("_________________" * 14 )
