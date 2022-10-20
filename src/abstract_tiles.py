
import pygame
import json
from Obstacle import Barrier, Coin, Obstacle, Platform, Reverser, WinBlock



class Map :
    def __init__(self , file ,
                 platform_tiles = [ 97 ] ,
                 barrier_tiles  = [] ,
                 background_tiles = [ 154 ] ,
                 reverser_tiles = [  214 , 43 ] ,
                 coin_tiles = [ 2 ],
                 win_tiles = [100]
                 ) -> None:
        self.file = file
        with open(fr"{file}.json") as h :
            x = json.load(h)

        self.TILE_HEIGHT = x['tileheight']
        self.TILE_WIDTH = x['tilewidth']

        self.MAP_WIDTH = x['layers'][0]['width']
        self.MAP_HEIGHT = x['layers'][0]['height']

        self.MAP_ = x['layers'][0]['data']
        self.MAP_ = [i-1 if i != 0 else i  for i in self.MAP_]


        self.MAP = []

        for i in range(self.MAP_HEIGHT) :
            self.MAP.append(self.MAP_[i*self.MAP_WIDTH : (i+1) * self.MAP_WIDTH ])
            print(self.MAP_[i*30 : (i+1) * 30 ])

        self.image = pygame.image.load('tiles.png')

        self.surface = pygame.Surface((self.MAP_WIDTH * self.TILE_WIDTH , self.MAP_HEIGHT * self.TILE_HEIGHT ))

        self.USED_IMAGES = set(self.MAP_)  ## Get Unique Image Indices
        self.USED_IMAGES = {i : pygame.image.load(f'tilez//tile{str(i).zfill(3)}.png') for i in self.USED_IMAGES}   # Make a hashh map used image indices as keys




        self.rects = []
        self.coins = []


        self.platform_tiles   = platform_tiles
        self.barrier_tiles    = barrier_tiles
        self.background_tiles = background_tiles
        self.reverser_tiles   = reverser_tiles
        self.coin_tiles       = coin_tiles
        self.win_tiles        = win_tiles

        self.surface.fill('white')
        for row_no , row in enumerate(self.MAP) :
            for element_no , element in enumerate(row) :
                if element in self.win_tiles  :
                    self.rects.append(WinBlock(element_no * self.TILE_WIDTH , row_no * self.TILE_WIDTH  , self.TILE_WIDTH , self.TILE_HEIGHT ))

                    pass
                elif element in self.reverser_tiles :
                    self.rects.append(Reverser(element_no * self.TILE_WIDTH , row_no * self.TILE_WIDTH  , self.TILE_WIDTH , self.TILE_HEIGHT ))
                elif element in self.barrier_tiles :
                    self.rects.append(Barrier(element_no * self.TILE_WIDTH , row_no * self.TILE_WIDTH  , self.TILE_WIDTH , self.TILE_HEIGHT ))
                elif element in self.platform_tiles :
                    self.rects.append(Platform(element_no * self.TILE_WIDTH , row_no * self.TILE_WIDTH  , self.TILE_WIDTH , self.TILE_HEIGHT ))

                if element not in self.background_tiles :
                    self.surface.blit(self.USED_IMAGES[self.background_tiles[0]] , (element_no * self.TILE_WIDTH , row_no * self.TILE_WIDTH  ))
                    if element in self.coin_tiles :
                        self.coins.append(Coin(element_no * self.TILE_WIDTH , row_no * self.TILE_WIDTH  , self.TILE_WIDTH , self.TILE_HEIGHT , self.USED_IMAGES[element] ))
                        continue

                self.surface.blit(self.USED_IMAGES[element] , (element_no * self.TILE_WIDTH , row_no * self.TILE_WIDTH  ))

        def get_rects(self) :
            return self.rects

        def get_bg(self) :
            return self.surface

        def get_coins(self) :
            return self.coins


if __name__ == '__main__':
    m = Map("lvl2")
    for i in m.rects :
        pygame.draw.rect(m.surface , 'red' , i.rect , 1)

    for i in m.coins :
        pygame.draw.rect(m.surface , 'green' , i.rect , 1)




    win = pygame.display.set_mode((m.MAP_WIDTH * m.TILE_WIDTH , m.MAP_HEIGHT * m.TILE_HEIGHT ))
    win.fill('white')
    win.blit(m.surface , (0,0))
    pygame.display.flip()
    while 1 :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT  :
                quit()
        pygame.display.flip()
