import pygame

pygame.font.init()

class Button :
    def __init__(self , x , y , w ,  txt  , size , surface , action , game  ) -> None:
        self.x , self.y , self.w = x , y , w
        self.txt = txt
        self.size = size
        self.game = game
        self.image= pygame.Surface((self.w,100))
        self.image.fill('black')
        self.image.set_colorkey('black')
        self.surface  = surface

        self.action = action[0]
        self.args =  action[1:]

        self.rect = self.image.get_rect()

        self.name = "cool"


        self.rect.center = (self.x , self.y )


        self.font = pygame.font.Font('ousp.ttf', size)
        # self.render  = pygame.Surface((10,10))
        self.render  = self.font.render(txt , True , 'blue' )
        self.render_rect = self.render.get_rect()
        self.render_rect.center = (self.x , self.y )

        self.image.blit(self.render , (self.render_rect.topleft))

    def hover(self) :
        self.image.fill('red')
        self.image.set_colorkey('red')
        self.rect = self.image.get_rect()
        self.rect.center = (self.x , self.y )


        self.font = pygame.font.Font('ousp.ttf', self.size + 10)
        self.render  = self.font.render(self.txt , True , 'blue' )
        self.render_rect = self.render.get_rect()
        self.render_rect.center = (self.x , self.y )
        self.image.blit(self.render , (self.render_rect.topleft))


    def draw(self , surface ) :
        surface.blit(self.image , (self.rect.topleft))
        surface.blit(self.render , (self.render_rect.topleft))

    def action(self  , *args ) :
        return self.action(*args)

    def update(self) :
        if self.rect.collidepoint(pygame.mouse.get_pos()) :
            self.hover()
            for event in self.game.events :
                if event.type == 1026 :
                    (self.action(*self.args))
        self.draw(self.surface)


if __name__ == '__main__':

    a = Button(400,306 , "Hi There " * 2, 32 ,"t" , )
    buttons = list[Button]()
    buttons.append(a)
    surface = pygame.Surface((1280 , 720))
    surface.fill('white')
    a.draw(surface)
    win = pygame.display.set_mode((1280 , 720))
    win.fill('white')
    win.blit(surface , (0,0))
    pygame.display.flip()
    while 1 :
        for event in pygame.event.get() :
            # print(event)
            if event.type == pygame.QUIT  :
                quit()
            if  event.type == pygame.MOUSEBUTTONDOWN :
                for i in buttons :
                    if  i.rect.collidepoint(  *pygame.mouse.get_pos() ) :
                        i.hover()
        #         i.hover()
        #         a.draw(surface)
        # for i in buttons :
        #     if  i.rect.collidepoint(  *pygame.mouse.get_pos() ) :
        #         print("Hoho ")
        #         i.hover()
        #         a.draw(surface)
        print(a.name)
        a.draw(surface)
        pygame.display.flip()
