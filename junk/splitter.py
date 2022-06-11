import pygame

pygame.init()

win = pygame.display.set_mode((800,400))


image = pygame.image.load(r"g:\school_project\code\Run (32x32).png").convert_alpha()

def splitr(image):
    returnable = list()
    for i in range(0,12*32 , 32) :
        list.append(returnable, image.subsurface(i,0,32,32))
    return returnable

img_list = splitr(image)
i = 0

run = True
while run :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
            i+=1 
    if i >= 36 :
        i = 0
    win.fill((255,255,255))
    win.blit(img_list[i // 3 ], (100,100))
        
    pygame.display.flip()
    i += 1
    
