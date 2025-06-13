import pygame
import pymunk
import pymunk.pygame_util

from tool import *
from data import data
from config import Config
import asyncio

from models.tilesheet import Tilesheet
from models.tile import *
from models.InputBox import Inputbox

data_local = data()

def Start():
    pygame.init()

    #Atribuições para inicialização (pygame e pymunk)
    screen = pygame.display.set_mode((Config.resX, Config.resY))
    canvas = pygame.Surface((Config.resX, Config.resY))
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0, 200)

    draw_options = pymunk.pygame_util.DrawOptions(screen)

    #Carregando o tilemap
    tilesheet = Tilesheet('data/tilesheet.png')
    map = TileMap('data/tilemap.csv', tilesheet )

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


        input_box = pygame.Rect(100, 80, 140, 40)

        screen.fill(Tool.rgb(Config.color['background']))
        space.step(1 / 60)
        space.debug_draw(draw_options)

        canvas.fill(Tool.rgb(Config.color['background']))
        map.draw_map(canvas)
        screen.blit(canvas, (0, 0))

        pygame.display.flip()
        clock.tick(Config.FPS)


if __name__ == "__main__":
    Start()