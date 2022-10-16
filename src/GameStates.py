

class GameState() :
    def __init__(self , Game ):
        self.Game = Game
        self.env = Game.environment
        self.name = str()

    def update(self) :
        ## This Function Is meant to be over-ridden @Naren dont freak out
        pass

class Playing(GameState) :
    def __init__(self, Game) :
        super().__init__(Game)
        self.name = "playing"

    def update(self ):
        self.Game.player.update()
        self.Game.environment.blit(self.Game.level_bg , ( 0, 0 ))
        self.Game.environment.blit(self.Game.player.image , (self.Game.player.rect.x , self.Game.player.rect.y))



class Death(GameState) :
    def __init__(self , Game ):
        super().__init__(Game)
        self.name = "died"
    def update(self ):
        self.Game.environment.fill('white')
        self.Game.environment.blit(self.Game.death_bg , ( 0, 0 ))


class Menu(GameState) :
    def __init__(self , Game ):
        super().__init__(Game)
        self.name = "menu"
    def update(self ):
        self.Game.environment.fill('white')
        self.Game.environment.blit(self.Game.menu_bg , ( 0, 0 ))

class Victory(GameState) :
    def __init__(self , Game ):
        super().__init__(Game)
        self.name = "won"
    def update(self ):
        self.Game.environment.fill('white')
        self.Game.environment.blit(self.Game.victory_bg , ( 0, 0 ))
