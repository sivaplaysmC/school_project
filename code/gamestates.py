import pygame


class GameState :
    def __init__(self  , win ) :
        self.color = "blue"
        self.win = win
        pass
    def main(self):
        self.win.fill(self.color)

class Pause_menu(GameState):
    
    def __init__(self , win):
        super().__init__(win)

    def main(self) :
        self.win.fill("white")
        self.win.blit(pygame.transform.scale(pygame.image.load("pause_menu.png"), (self.win.get_width(), self.win.get_height() )), (0,0))

