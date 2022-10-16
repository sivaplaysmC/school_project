import pygame
from reading_json import *
from Obstacle import Barrier, Obstacle, Platform, Reverser, WinBlock


image = pygame.image.load('tiles.png')

surface = pygame.Surface((MAP_WIDTH * TILE_WIDTH , MAP_HEIGHT * TILE_HEIGHT ))

__USED_IMAGES = set(MAP_)  ## Get Unique Image Indices
__USED_IMAGES = {i : pygame.image.load(f'tile_images//tile{str(i).zfill(3)}.png') for i in __USED_IMAGES}   # Make a hashh map used image indices as keys




rects = []

### Tile 000 :: Background Tile
### Tile 040 :: Rosewater tile
### Tile 154 :: Brick Wall
### Tile 059 and 021  :: sliding platforms
### Tile 24 , 43 , 63 : vertical border tiles
### Tile 100 : winblock

platform_tiles = [ 24 , 43 , 62 , 59 , 21 ]
barrier_tiles  = [ 154  ]
background_tiles = [0 , 40 ]
reverser_tiles = [2]

surface.fill('white')
for row_no , row in enumerate(MAP) :
    for element_no , element in enumerate(row) :
        if element == 100 :
            rects.append(WinBlock(element_no * 32 , row_no * 32  , TILE_WIDTH , TILE_HEIGHT ))
        if element  in background_tiles :
            pass
        elif element in reverser_tiles :
            rects.append(Reverser(element_no * 32 , row_no * 32  , TILE_WIDTH , TILE_HEIGHT ))
        elif element in barrier_tiles :
            rects.append(Barrier(element_no * 32 , row_no * 32  , TILE_WIDTH , TILE_HEIGHT ))
        elif element in platform_tiles :
            rects.append(Platform(element_no * 32 , row_no * 32  , TILE_WIDTH , TILE_HEIGHT ))
        surface.blit(__USED_IMAGES[element] , (element_no * 32 , row_no * 32  ))

def get_rects() :
    return rects

def get_bg() :
    return surface


if __name__ == '__main__':
    for i in rects :
        pygame.draw.rect(surface , 'red' , i.rect , 1)


    print(__USED_IMAGES)

    win = pygame.display.set_mode((MAP_WIDTH * TILE_WIDTH , MAP_HEIGHT * TILE_HEIGHT ))
    win.fill('white')
    win.blit(surface , (0,0))
    pygame.display.flip()
    # print(*rects , sep='\t\t')
    while 1 :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT  :
                quit()
        pygame.display.flip()
