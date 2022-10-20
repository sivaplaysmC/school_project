
from pygame import Rect
from Player import Player
# from Game import Game

class Obstacle :
    def __init__(self , x , y , w ,h ):
        self.x , self.y , self.w , self.h = x ,y , w  , h
        self.rect = Rect(x , y , w , h)

    def apply_effects(self ,game) :
        pass

class Platform(Obstacle) :

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def apply_effects(self ,game ) :
        super().apply_effects(game)

class Reverser(Obstacle) :

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def apply_effects(self ,game ) :
        super().apply_effects(game)
        game.player.direction = not game.player.direction


class Barrier(Obstacle) :

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        pass

    def apply_effects(self,game):
        super().apply_effects(game)
        game.player.alive = False

class WinBlock(Obstacle) :

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        pass

    def apply_effects(self,game):
        super().apply_effects(game)
        game.victory = True

class Coin(Obstacle) :
    def __init__(self, x, y, w, h, image ):
        super().__init__(x, y, w, h,)
        self.image = image
