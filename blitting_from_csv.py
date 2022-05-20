import pygame
from map_parser import main


pygame.init()

win = pygame.display.set_mode((160,160))

clock = pygame.time.Clock()
im1 = pygame.image.load(r"G:\school_project\split_tiles\tile029.png").convert_alpha()
im2 = pygame.image.load(r"G:\school_project\split_tiles\tile007.png")
blitter_x = 0
blitter_y = 0
run = True

x = main()
for i in x :
    blitter_x = 0
    for j in i :
        print(blitter_x , blitter_y)
        if j != -1 :
            if j < 10 :
                win.blit(pygame.image.load(r"G:\school_project\split_tiles\tile00"+str(j)+".png").convert_alpha() , (blitter_x , blitter_y))
            elif j < 100 :
                win.blit(pygame.image.load(r"G:\school_project\split_tiles\tile0"+str(j)+".png").convert_alpha() , (blitter_x , blitter_y))
        blitter_x += 16
    blitter_y += 16
while run :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False


    # win.fill((128 , 128 , 128))
    pygame.display.flip()
