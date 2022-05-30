import pygame 

pygame.init()


win = pygame.display.set_mode((800,800))

image = pygame.image.load(r"Run (32x32).png")

img_list = image.subsurface()

run = True 
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False
    win.blit(image , (100,100))
    pygame.display.flip()
