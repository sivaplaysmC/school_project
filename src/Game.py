import pygame

from Player import Player
from GameStates import Death, Menu, Level_1, Victory
from reading_tiles import  MAP_HEIGHT , MAP_WIDTH , TILE_HEIGHT , TILE_WIDTH
# from reading_json import MAP_HEIGHT, MAP_WIDTH, TILE_HEIGHT, TILE_WIDTH

class Game :
    def __init__(self):


        self.environment = pygame.Surface((MAP_WIDTH * TILE_WIDTH , MAP_HEIGHT * TILE_HEIGHT))
        self.RES = (900,900)
        # print(self.RES)
        self.display = pygame.display.set_mode(self.RES)
        self.GameStateStack = list()
        self.events = pygame.event.get()

        self.running = True
        self.death_bg = pygame.image.load('death_bg.png')
        self.death_bg = pygame.transform.scale(self.death_bg , (MAP_WIDTH *TILE_WIDTH , MAP_HEIGHT * TILE_HEIGHT) )
        self.victory_bg = pygame.image.load('victory_bg.png')
        self.victory_bg =pygame.transform.scale(self.victory_bg , (MAP_WIDTH *TILE_WIDTH , MAP_HEIGHT * TILE_HEIGHT) )
        self.menu_bg = pygame.image.load('menu_bg.png')
        self.menu_bg = pygame.transform.scale(self.menu_bg , (MAP_WIDTH *TILE_WIDTH , MAP_HEIGHT * TILE_HEIGHT) )
        self.GameStateStack.append(Menu(self))

        self.player = Player(self , 0 )

        self.victory = False

        self.gravity = 1   ## One for down , 0 for up



    def add_state(self , name) :
        if name == "playing" :
            self.GameStateStack.append(Level_1(self))

    def update(self) :
        self.GameStateStack[-1].update()

    def get_keys(self) :
        for event in self.events :
            if event.type == pygame.QUIT :
                self.running = False
            # mouse_pos = pygame.mouse.get_pos
            # for button in self.GameStateStack[-1].buttons :
            #     if button.rect.collidepoint(mouse_pos) :
            #         if event.type == pygame.MOUSEBUTTONDOWN :
            #             button.action()





            if event.type == pygame.KEYDOWN :
                if self.GameStateStack[-1].name == 'playing' :
                    if event.key == pygame.K_SPACE :
                        self.gravity = not self.gravity

                if self.GameStateStack[-1].name == 'won' :
                    if event.key == pygame.K_RETURN :
                        self.player.__init__(self)
                        self.victory = False
                        (self.GameStateStack.pop())
                    if event.key == pygame.K_ESCAPE :
                        self.running = False
                if self.GameStateStack[-1].name == 'died' :
                    if event.key == pygame.K_RETURN :
                        self.player.__init__(self)
                        (self.GameStateStack.pop())
                        self.GameStateStack[-1].__init__(self)
                    if event.key == pygame.K_ESCAPE :
                        self.running = False
                if self.GameStateStack[-1].name == 'menu' :
                    if event.key == pygame.K_RETURN :
                        self.GameStateStack.append(Level_1(self))
                    if event.key == pygame.K_ESCAPE :
                        self.running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] :
            self.player.direction = not self.player.direction

    def draw(self) :
        self.display.blit(pygame.transform.scale(self.environment , ( self.display.get_width() , self.display.get_height() )) , (0,0))
        pygame.display.flip()

    def check_death(self) :
        if self.GameStateStack[-1].name != 'died' :
            if self.player.alive :
                pass
            else :
                self.GameStateStack.append(Death(self))

    def check_victory(self) :
        if self.GameStateStack[-1].name != 'won' :
            if self.victory :
                self.GameStateStack.append(Victory(self))
            else :
                pass

    def check_win(self) :
        pass

    def mainloop(self) :
        CLOCK = pygame.time.Clock()
        while self.running :
            self.events = pygame.event.get()
            self.dt = CLOCK.tick(60)
            self.get_keys()
            self.update()
            self.draw()
            self.check_victory()
            self.check_death()

if __name__ == '__main__':
    game = Game()
    game.mainloop()
    # running = 1
    # while running :
    #     for event in pygame.event.get() :
    #         if event.type == pygame.QUIT :
    #             running = 0
    #     game.display.blit(game.level_bg , (0,0))
    #     pygame.display.flip()
