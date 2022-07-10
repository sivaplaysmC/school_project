import pygame

def menu(win) :
    win.fill("white")
    pygame.display.flip()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            exit()
