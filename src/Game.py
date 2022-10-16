import pygame

from Player import Player
from GameStates import Death, Menu, Playing, Victory
from reading_tiles import get_bg , get_rects
from reading_json import MAP_HEIGHT, MAP_WIDTH, TILE_HEIGHT, TILE_WIDTH

class Game :
    def __init__(self):


        self.environment = pygame.Surface((MAP_WIDTH * TILE_WIDTH , MAP_HEIGHT * TILE_HEIGHT))
        RES = (1280 , 720 )
        self.display = pygame.display.set_mode(RES)

        self.running = True

        self.player = Player(self)
        self.GameStateStack = list()
        self.GameStateStack.append(Menu(self))
        self.rects = get_rects()
        self.victory = False

        self.gravity = 1   ## One for down , 0 for up


        self.level_bg  = get_bg()
        self.death_bg = pygame.image.load('death_bg.png')
        self.death_bg = pygame.transform.scale(self.death_bg , (MAP_WIDTH *TILE_WIDTH , MAP_HEIGHT * TILE_HEIGHT) )
        self.menu_bg = pygame.image.load('menu_bg.png')
        self.menu_bg = pygame.transform.scale(self.menu_bg , (MAP_WIDTH *TILE_WIDTH , MAP_HEIGHT * TILE_HEIGHT) )
        self.victory_bg = pygame.image.load('victory_bg.png')
        self.victory_bg =pygame.transform.scale(self.victory_bg , (MAP_WIDTH *TILE_WIDTH , MAP_HEIGHT * TILE_HEIGHT) )


    def update(self) :
        self.GameStateStack[-1].update()

    def get_keys(self) :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                self.running = False

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
                    if event.key == pygame.K_ESCAPE :
                        self.running = False
                if self.GameStateStack[-1].name == 'menu' :
                    if event.key == pygame.K_RETURN :
                        self.GameStateStack.append(Playing(self))
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
            CLOCK.tick(60)
            self.get_keys()
            self.update()
            self.draw()
            self.check_victory()
            self.check_death()

if __name__ == '__main__':
    game = Game()
    game.mainloop()
