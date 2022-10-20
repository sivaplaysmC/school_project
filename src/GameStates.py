

from os import times_result
from typing import ClassVar
import pygame
from reading_tiles import get_bg , get_coins , get_rects
from button import Button
from Player import Player
import csv


class GameState() :
    def __init__(self , Game ):
        self.Game = Game
        self.env : pygame.Surface = Game.environment
        self.name = str()
        self.font = pygame.font.Font("igoe.ttf" , 24 )
        self.other_font = pygame.font.Font("doom.ttf" , 48)
        self.title_font = pygame.font.Font("doom.ttf" , 128)
        self.buttons = []
        self.speed = 0
        self.diff = None
        self.time_elapsed_s = None

    def update(self) :
        ## This Function Is meant to be over-ridden @Naren dont freak out
        pass

class Level_1(GameState) :
    def __init__(self, Game , diff) :
        super().__init__(Game)
        self.name = "playing"
        self.font = pygame.font.Font("igoe.ttf" , 24 )
        self.level_bg  = get_bg()
        self.rects = get_rects()
        self.coins = get_coins()
        self.time_elapsed = 0
        self.time_elapsed_s = self.time_elapsed // 1000
        self.diff = diff
        if self.diff == "easy" :
            self.speed = 0.3
        if self.diff == "med" :
            self.speed = 0.5
        if self.diff == "hard" :
            self.speed = 0.9
        self.Game.player.__init__(self.Game , self.speed)

        # self.Game.player.del_acc  = speed
        # print(self.Game.player.del_acc)



    def update(self ):
        self.time_elapsed += self.Game.dt
        self.time_elapsed_s = self.time_elapsed // 1000
        # print(self.time_elapsed_s)
        self.Game.player.update()
        self.Game.environment.blit(self.level_bg , ( 0, 0))
        self.Game.environment.blit(self.Game.player.image , (self.Game.player.rect.x , self.Game.player.rect.y))
        points = self.font.render("Points : " + str(self.Game.player.points) , True , "white")
        time = self.font.render("time : " + str(self.time_elapsed_s) , True , "white")
        for i in self.coins :
            self.Game.environment.blit(i.image , (i.x , i.y) )
        pygame.draw.rect(self.Game.environment , "#ff4d4d" , (90,0,200,32))
        pygame.draw.rect(self.Game.environment , "#ff4d4d" , (690,0,200,32))
        self.Game.environment.blit(points , (100,2))
        self.Game.environment.blit(time, (720,2))



class Death(GameState) :
    def __init__(self , Game ):
        super().__init__(Game)
        self.name = "died"
        self.bg = self.Game.menu_bg

        self.data_saved = 0
    def update(self ):
        self.Game.environment.fill('white')
        self.Game.environment.blit(self.bg , ( 0, 0 ))

        Greeter = self.title_font.render("Game Over" , True , "green"  )
        self.Game.player.__init__(self.Game , 0.6)
        self.retry_button = Button(500 , 250, 500 ,"retry" , 64  , self.env ,(self.Game.GameStateStack.append , DifficultyMenu(self.Game) ) , self.Game)
        self.exit_button = Button(500 , 350, 500 ,"Quit" , 64  , self.env ,(self.Game.GameStateStack.append , Menu(self.Game) ) , self.Game)
        self.exit_button.update()
        self.retry_button.update()
        if not self.data_saved :
            print('Not Saved')
            self.save_data()

        # print(self.Game.GameStateStack[-2])
    def save_data(self) :
        if not self.data_saved :
            self.data_saved = 1
            with open('scores.csv' , "a+") as fh :
                reader = csv.reader(fh)
                writer = csv.writer(fh)
                contents = [i for i in reader]
                ### File Schema :: Mode , difficulty
                headers = ["diff" , "speed"]
                data = contents[1:]
                print(data)
                data.append([self.Game.GameStateStack[-2].diff , self.Game.GameStateStack[-2].time_elapsed_s ])
                print(data)
                for i in data :
                    # if i[0] and i[1] :
                    if len(i) :
                        writer.writerow(i)
                # writer.writerows(data)
                print('Saved')



class Menu(GameState) :
    def __init__(self , Game ):
        super().__init__(Game)
        self.name = "menu"
        self.bg = self.Game.menu_bg
    def update(self ):
        # self.Game.environment.fill('white')
        self.env.blit(self.bg , (0,0))
        Greeter = self.title_font.render("Gravity Runner" , True , "green"  )


        ###  x , y , w ,  txt  , size , surface , action , game

        play_button = Button(500 , 500 , 500 ,  "Start" , 64 , self.env , ( self.Game.GameStateStack.append , DifficultyMenu(self.Game) ) , self.Game)
        exit_button = Button(500 , 600 , 500 ,  "Exit" , 64 , self.env , ( quit , ) , self.Game )
        high_button = Button(500 , 700 , 500 ,  "High Scores" , 64 , self.env , ( self.Game.GameStateStack.append , HighScores(self.Game) ) , self.Game )
        play_button.update()
        exit_button.update()
        high_button.update()
        self.env.blit(Greeter , (200,200))


class Victory(GameState) :
    def __init__(self , Game ):
        super().__init__(Game)
        self.name = "won"
    def update(self ):
        self.Game.environment.fill('white')
        self.Game.environment.blit(self.Game.victory_bg , ( 0, 0 ))


class DifficultyMenu(GameState) :
    def __init__(self, Game):
        super().__init__(Game)
        self.bg = self.Game.menu_bg

    def update(self):
        super().update()
        # self.env.fill('teal')
        self.env.blit(self.bg , (0,0))
        Greeter = self.title_font.render("Choose Difficulty " , True , "red"  )
        self.easy_button = Button(500 , 350, 500 ,"Easy" , 64  , self.env ,( self.Game.GameStateStack.append , Level_1(self.Game , "easy") ) , self.Game)
        self.medium_button = Button(500 , 450, 500 ,"Medium" , 64  , self.env ,( self.Game.GameStateStack.append , Level_1(self.Game , "med") ) , self.Game)
        self.hard_button = Button(500 , 550, 500 ,"Hard" , 64  , self.env ,( self.Game.GameStateStack.append , Level_1(self.Game , "hard") ) , self.Game)
        self.easy_button.update()
        self.medium_button.update()
        self.hard_button.update()
        self.env.blit(Greeter , (200,200))


class HighScores(GameState) :
    def __init__(self, Game):
        super().__init__(Game)
        self.bg = self.Game.menu_bg
        with open('scores.csv' , "r") as fh :
            reader = csv.reader(fh)
            contents = [i for i in reader]
            ### File Schema :: Mode , difficulty
            headers = ["diff" , "speed"]
            data = contents[1:]
            hard = [i for i in data if i[0] == "hard"]
            med  = [i for i in data if i[0] == "med"]
            easy  = [i for i in data if i[0] == "easy"]
            hard = [i[::-1] for i in hard]
            med  = [i[::-1] for i in med ]
            easy = [i[::-1] for i in easy]
            self.hard_val = min(hard)[::-1]
            self.med_val  = min(med)[::-1]
            self.easy_val = min(easy)[::-1]

    def update(self):
        super().update()
        self.env.blit(self.bg , (0,0))
        hard_render = self.font.render(str(self.hard_val) , True , "red")
        med_render = self.font.render(str(self.med_val) , True , "red")
        easy_render = self.font.render(str(self.easy_val) , True , "red")
        self.env.blit(easy_render , (400,500))
        self.env.blit(med_render ,  (400,600))
        self.env.blit(hard_render , (400,700))
        print(self.hard_val, self.med_val , self.easy_val)
            # writer.writerows(data)
