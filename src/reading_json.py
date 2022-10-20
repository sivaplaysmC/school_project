import json
import pygame
with open(r"test.json") as h :
    x = json.load(h)
rect_list = list()

TILE_HEIGHT = x['tileheight']
TILE_WIDTH = x['tilewidth']

MAP_WIDTH = x['layers'][0]['width']
MAP_HEIGHT = x['layers'][0]['height']

MAP_ = x['layers'][0]['data']



MAP = []

for i in range(MAP_HEIGHT) :
    MAP.append(MAP_[i*30 : (i+1) * 30 ])

del MAP_

if __name__ == '__main__':
    
    print(MAP , end=('\n' + '-' *14*33 + '\n'))
    print(MAP_WIDTH , MAP_HEIGHT , TILE_WIDTH  , TILE_HEIGHT , sep= '\t')