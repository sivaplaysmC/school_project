import pygame
from map_parser import main


pygame.init()

win = pygame.display.set_mode((900,600))

clock = pygame.time.Clock()
bg = pygame.image.load(r"g:\school_project\assets\Background\single_background.png").convert_alpha()
bg = pygame.transform.scale(bg , (900,600))
# im1 = pygame.image.load(r"split_tiles\tile029.png").convert_alpha()
# im2 = pygame.image.load(r"split_tiles\tile007.png")
blitter_x = 0
blitter_y = 0
run = True
win.blit(bg , (0,0))
x = main()
for i in x :
    blitter_x = 0
    for j in i :
        # print(blitter_x , blitter_y)
        if j != -1 :
            if j < 10 :
                win.blit(pygame.transform.scale(pygame.image.load(r"split_tiles\tile00"+str(j)+".png").convert_alpha() , (30,30)) , (blitter_x , blitter_y))
            elif j < 100 :
                win.blit(pygame.transform.scale(pygame.image.load(r"split_tiles\tile0"+str(j)+".png").convert_alpha() , (30,30)) , (blitter_x , blitter_y))
        blitter_x += 30
    blitter_y += 30
while run :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False


    # win.fill((128 , 128 , 128))
    pygame.display.flip()
