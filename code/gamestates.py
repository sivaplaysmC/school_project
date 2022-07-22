import pygame
# from pygame.display import update

class GameState :
    def __init__(self  , Game:"Game") :
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


class mini(GameState) :
    def __init__(self , Game):
        super().__init__(Game)
        self.name = "mini"
        self.environment : "pygame.Surface" = self.Game.environment
    def update(self) :
        pass
class Game_world(GameState) :
    def __init__(self, Game: "Game"):
        super().__init__(Game)
        self.name = "World"
    def update(self) :
        if self.Game.Player2.actions["right"] : self.Game.Player2.acceleration.x += 1
        if self.Game.Player2.actions["right"] : self.Game.Player2.acceleration.x += 1
        if self.Game.Player1.actions["left"] : self.Game.Player1.acceleration.x -= 1
        if self.Game.Player1.actions["left"] : self.Game.Player1.acceleration.x -= 1
        self.Game.environment.fill((255,255,255))
        self.Game.Player1.move(self.Game.dt)
        self.Game.Player2.move(self.Game.dt)
        self.Game.players.draw(self.Game.environment)
        self.Game.platforms.draw(self.Game.environment)
