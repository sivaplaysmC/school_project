def text_parser(file) :
    # file = r"processed_spritesheets\player_run.txt"
    f = open(file , "r")
    x = f.readlines()
    # x = x.split("\n")
    for i in range(len(x)) :
        x[i] = x[i].strip("\n")
        x[i] = x[i].split(" ")
        x[i].pop(0) ; x[i].pop(0)
        for j in range(len(x[i])) :
            x[i][j] = eval(x[i][j])
        x[i] = tuple(x[i])
    x = tuple(x)
    return {"length" : len(x) , "metadata" : x }
x = text_parser("processed_spritesheets\player_run.txt")
#-----------------------------------------------------------------------------------------------
print(x["length"])
for i in range(x["length"]) :
    print(x["metadata"][i])
import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
image = (pygame.image.load(r"processed_spritesheets\player_run.png"))

def splitter(image) :
    image = image
    imgs= tuple()
    metadata = text_parser(r"processed_spritesheets\player_run.png".replace("png", "txt"))
    for i in range(metadata["length"]):
        imgs+=pygame.transform.scale(image.subsurface(metadata["metadata"][i]) , (50,50)),
    return imgs
sprites = splitter(image)
print(sprites)
clock = pygame.time.Clock()
x, y = 0 , 0 
blittable =  sprites[x%6]
rect = pygame.Rect(250, 250, 50, 50)

run = True
while run :
    clock.tick(60)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
    win.blit(image, (0,0))
    win.fill('white')
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] :
       rect.move_ip(3, 0)  
       blittable =  sprites[x%6]
    if keys[pygame.K_LEFT] :
        rect.move_ip(-3, 0)  
        blittable = pygame.transform.flip( sprites[x%6], flip_x= True , flip_y= False )
    win.blit(blittable, ( rect.x,rect.y ))
    y += 1
    if y % 4 == 0 :
        x += 1 
    pygame.display.flip()

