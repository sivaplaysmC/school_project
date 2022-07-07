import subprocess

p = subprocess.Popen("ls ~/patching/nerd_fonts" , stdout=subprocess.PIPE, shell=True)



x = p.communicate()
x = str((x[0]))
for i in x.split(r"\n") :
    print(i)
    i = r"~/patching/nerd_fonts/" + i
    r = subprocess.Popen(r"/home/sivaplays/patching/./font-patcher " + i.replace(" " , r"\ ") + r" --custom codicon.ttf" , stdout=subprocess.PIPE, shell=True)
    print(r.communicate())


