from reading_json import rect_list
import pygame

pygame.init()

win = pygame.display.set_mode((1408,736))
win.fill("white")
for haha in rect_list :
    win.blit(pygame.Surface((haha.w,haha.h)),(haha.x,haha.y))
while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            raise SystemExit()
        
    pygame.display.flip()
