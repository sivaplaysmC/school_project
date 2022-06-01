import pygame

def clamp(obj , range_) :
    if obj < range_[0]  : 
        return range_[0]
    if obj > range_[1] :
        return range_[1]
    return obj
    


FPS = 120
screen = pygame.display.set_mode((640 , 640))
bg = pygame.image.load(r'g:\school_project\sewer.png').convert_alpha()
bg = pygame.transform.scale(bg, ( 3840,640 ))

screen_size = screen.get_size()
bg_size = bg.get_size()
bg_x = 0     #(bg_size[0]-screen_size[0]) // 2
bg_y = 0    #(bg_size[1]-screen_size[1]) // 2

clock = pygame.time.Clock()
delta_time_clock = pygame.time.Clock()
while True:
    delta_time = delta_time_clock.tick(FPS) * 0.001 * 60 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b :
            print("-"*14)
            print(bg_size[0]-screen_size[0])
            print(bg_x)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bg_x += 10 * delta_time
    if keys[pygame.K_RIGHT]:
        bg_x -= 10 * delta_time
    bg_y = 0
    bg_x = clamp(bg_x, ( 0,bg_size[0] - screen_size[0]))

    screen.blit(bg, (bg_x, bg_y))
    pygame.display.flip()
