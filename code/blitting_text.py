import pygame
pygame.init()

win = pygame.display.set_mode((800,800))

font = pygame.font.Font(None, 50)

run = True
get_input = False
string  = str()
while run :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_BACKQUOTE :
                get_input = not(get_input) 
            if get_input :
                
                if event.key == pygame.K_RETURN :
                    if string[:3] == "set" :
                        string = string.lstrip()
                        exec(string[4:])
                    string = str()
                if event.unicode != "" and event.unicode != "`" and event.unicode != '\r':
                    string += event.unicode

    win.fill((255,255,255))
    win.blit(font.render(string, True, (0,0,0)), (100,100))
    pygame.display.flip()

