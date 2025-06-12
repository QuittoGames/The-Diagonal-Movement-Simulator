import pygame
import csv
import os

class Tile:
    def __init__(self, image, x, y, spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class TileMap():
    def __init__(self, filename, spritesheet):
        self.tile_size = 16
        self.start_x, self.start_y = 0, 0
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(filename)
        
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()
    
    def draw_map(self, surface):
        surface.blit(self.map_surface, (0, 0))

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)

    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map
    
    def load_tiles(self, filename):
        tiles = []
        map = self.read_csv(filename)
        x, y = 0, 0
        for row in map:
            x = 0
            #Se necessário alterar a Matriz CSV já que pode acabar sendo necessário para alguns sprites
            for tile in row:
                if tile == '-1':
                    self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                
                #Chão
                elif tile == '9':
                    tiles.append(Tile('grama.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '10':
                    tiles.append(Tile('terra.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                
                #Graminea
                elif tile == '30':
                    tiles.append(Tile('graminea1.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '1':
                    tiles.append(Tile('graminea2.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '2':
                    tiles.append(Tile('graminea3.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '18':
                    tiles.append(Tile('graminea4.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '19':
                    tiles.append(Tile('graminea5.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                
                #Nuvens
                elif tile == '3':
                    tiles.append(Tile('nuvem1.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '12':
                    tiles.append(Tile('nuvem2.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '21':
                    tiles.append(Tile('nuvem3.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '4':
                    tiles.append(Tile('nuvem4.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '13':
                    tiles.append(Tile('nuvem5.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '22':
                    tiles.append(Tile('nuvem6.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '5':
                    tiles.append(Tile('nuvem7.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '14':
                    tiles.append(Tile('nuvem8.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '23':
                    tiles.append(Tile('nuvem9.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '6':
                    tiles.append(Tile('nuvem10.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '15':
                    tiles.append(Tile('nuvem11.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '24':
                    tiles.append(Tile('nuvem12.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '7':
                    tiles.append(Tile('nuvem13.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '16':
                    tiles.append(Tile('nuvem14.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '25':
                    tiles.append(Tile('nuvem15.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '8':
                    tiles.append(Tile('nuvem16.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '17':
                    tiles.append(Tile('nuvem17.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '26':
                    tiles.append(Tile('nuvem18.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                x += 1
            y += 1

        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles