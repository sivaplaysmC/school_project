import pygame
import json
from Obstacle import Barrier, Coin, Obstacle, Platform, Reverser, WinBlock

with open(r"lvl1.json") as h :
    x = json.load(h)
rect_list = list()

TILE_HEIGHT = x['tileheight']
TILE_WIDTH = x['tilewidth']

MAP_WIDTH = x['layers'][0]['width']
MAP_HEIGHT = x['layers'][0]['height']

MAP_ = x['layers'][0]['data']
MAP_ = [i-1 if i != 0 else i  for i in MAP_]


MAP = []

for i in range(MAP_HEIGHT) :
    MAP.append(MAP_[i*30 : (i+1) * 30 ])

image = pygame.image.load('tiles.png')

surface = pygame.Surface((MAP_WIDTH * TILE_WIDTH , MAP_HEIGHT * TILE_HEIGHT ))

USED_IMAGES = set(MAP_)  ## Get Unique Image Indices
USED_IMAGES = {i : pygame.image.load(f'tilez//tile{str(i).zfill(3)}.png') for i in USED_IMAGES}   # Make a hashh map used image indices as keys




rects = []
coins = []


platform_tiles = [ 97 ]
barrier_tiles  = [214]
background_tiles = [ 154 ]
reverser_tiles = [ 43 ]
coin_tiles = [ 2 ]
win_tiles = [100]

surface.fill('white')
for row_no , row in enumerate(MAP) :
    for element_no , element in enumerate(row) :
        if element in win_tiles  :
            rects.append(WinBlock(element_no * TILE_WIDTH , row_no * TILE_WIDTH  , TILE_WIDTH , TILE_HEIGHT ))
        if element  in background_tiles :
            pass
        elif element in reverser_tiles :
            rects.append(Reverser(element_no * TILE_WIDTH , row_no * TILE_WIDTH  , TILE_WIDTH , TILE_HEIGHT ))
        elif element in barrier_tiles :
            rects.append(Barrier(element_no * TILE_WIDTH , row_no * TILE_WIDTH  , TILE_WIDTH , TILE_HEIGHT ))
        elif element in platform_tiles :
            rects.append(Platform(element_no * TILE_WIDTH , row_no * TILE_WIDTH  , TILE_WIDTH , TILE_HEIGHT ))

        if element not in background_tiles :
            surface.blit(USED_IMAGES[background_tiles[0]] , (element_no * TILE_WIDTH , row_no * TILE_WIDTH  ))
            if element in coin_tiles :
                coins.append(Coin(element_no * TILE_WIDTH , row_no * TILE_WIDTH  , TILE_WIDTH , TILE_HEIGHT , USED_IMAGES[element] ))
                continue

        surface.blit(USED_IMAGES[element] , (element_no * TILE_WIDTH , row_no * TILE_WIDTH  ))

def get_rects() :
    return rects

def get_bg() :
    return surface

def get_coins() :
    return coins


if __name__ == '__main__':
    for i in rects :
        pygame.draw.rect(surface , 'red' , i.rect , 1)

    for i in coins :
        pygame.draw.rect(surface , 'green' , i.rect , 1)



    print(USED_IMAGES)

    win = pygame.display.set_mode((MAP_WIDTH * TILE_WIDTH , MAP_HEIGHT * TILE_HEIGHT ))
    print( win.get_width() , win.get_height())
    win.fill('white')
    win.blit(surface , (0,0))
    pygame.display.flip()
    # print(*rects , sep='\t\t')
    while 1 :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT  :
                quit()
        pygame.display.flip()
