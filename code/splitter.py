import pygame 

pygame.init()
clock = pygame.time.Clock()

win = pygame.display.set_mode((800,800))


image = pygame.image.load(r"Run (32x32).png")
ss = image.subsurface((0,0,32,32))

l = list()

for i in range(0 , 12*32 , 32 ) :
    l.append(image.subsurface(i,0,32,32))

run = True 
i = 0 
while run :
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False
    win.fill((255,255,255))
    win.blit(ss, (200,200))
    i = (i+1) % 12 
    win.blit(l[i] , (300,300))
    pygame.display.flip()
print(len(l))
