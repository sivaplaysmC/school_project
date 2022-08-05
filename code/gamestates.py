import pygame

class GameState :
    def __init__(self  , Game) :
        self.color = "blue"
        self.Game = Game
        # self.win = self.game.environment
        self.environment : "pygame.Surface" = self.Game.environment
    def main(self):
        self.environment.fill(self.color)


class Pause_menu(GameState):    
    def __init__(self , Game):
        super().__init__(Game)
        self.name = "Pause"
        self.environment : "pygame.Surface" = self.Game.environment

    def update(self) :
        self.Game.environment.fill("white")
        self.Game.environment.blit(pygame.transform.scale(pygame.image.load("pause_menu.png"), (self.Game.environment.get_width(), self.Game.environment.get_height() )), (0,0))


class Main_menu(GameState) :
    def __init__(self, Game):
        super().__init__(Game)
        self.name = "Main"
        self.environment : "pygame.Surface" = self.Game.environment
    def update(self) :
        self.Game.environment.fill((100,100,100))


class basic(GameState):
    vec = pygame.Vector2
    def __init__(self , Game) :
        super().__init__(Game)
        self.name = "basic"
        self.environment : "pygame.Surface" = self.Game.environment
        
    def update(self) :
        self.environment.fill("white")
        self.Game.player.move(self.Game.dt)
        for i in self.Game.platforms :
            self.environment.blit(i.image , (i.rect.x , i.rect.y))
        self.environment.blit(self.Game.player.image , (self.Game.player.rect.x , self.Game.player.rect.y))


            
