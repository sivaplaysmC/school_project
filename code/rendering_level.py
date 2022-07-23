from reading_json import rect_list
import pygame

pygame.init()

win = pygame.Surface((1408,736))

win.fill("white")
print(rect_list)
for haha in rect_list :
    print(haha)
    win.blit(pygame.Surface((haha.w,haha.h)),(haha.x,haha.y))
while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            raise SystemExit()
    pygame.display.flip()
