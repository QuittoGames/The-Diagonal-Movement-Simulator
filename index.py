import pygame
import pymunk
import pymunk.pygame_util

from tool import *
from data import data
import asyncio

from tilesheet import Tilesheet
from tile import *

data_local = data()
pygame.init()

#Atribuições para inicialização (pygame e pymunk)
screen_w, screen_h = 1296, 360
screen = pygame.display.set_mode((screen_w, screen_h))
canvas = pygame.Surface((screen_w, screen_h))
clock = pygame.time.Clock()

#Variáveis de personalização
fonte = pygame.font.Font(None, 32)
color = {
        'white': "#BDBDBD",
        'black': "#000000",
        'gray': "#3D3D3D",
        'background': "#b4d2df",
    }

space = pymunk.Space()
space.gravity = (0, 200)

draw_options = pymunk.pygame_util.DrawOptions(screen)

#Carregando o tilemap
tilesheet = Tilesheet('tilesheet.png')
map = TileMap('tilemap.csv', tilesheet )

#Variáveis de controle
control_ball = True 
running = True

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    screen.fill(Tool.rgb(color['background']))
    space.step(1 / 60)
    space.debug_draw(draw_options)

    canvas.fill(Tool.rgb(color['background']))
    map.draw_map(canvas)
    screen.blit(canvas, (0, 0))

    pygame.display.flip()
    clock.tick(60)