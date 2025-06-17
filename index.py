import pygame
import pymunk
import pymunk.pygame_util

from tool import Tool
from data import data
from config import Config

import asyncio
from dataclasses import dataclass

from models.tilesheet import Tilesheet
from models.tile import TileMap
from models.InputBox import Inputbox

data_local = data()

def Start():
    pygame.init()

    screen = pygame.display.set_mode((Config.resX, Config.resY))
    canvas = pygame.Surface((Config.resX, Config.resY))
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0, 200)

    draw_options = pymunk.pygame_util.DrawOptions(screen)

    tilesheet = Tilesheet('data/tilesheet.png')
    map = TileMap('data/tilemap.csv', tilesheet)

    font = pygame.font.Font(Config.font, 32)

    #InputBox
    input_width, input_height = 200, 40
    margin = 20
    input_x = Config.resX - input_width - margin
    input_y = Config.resY - input_height - margin
    input_box = Inputbox(input_x, input_y, input_width, input_height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

                if input_box.active:
                    if event.key == pygame.K_RETURN:
                        print(f"Input: {input_box.text}")
                        input_box.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        input_box.text = input_box.text[:-1]
                    else:
                        # Limite de 20 caracteres
                        if len(input_box.text) < 5:
                            input_box.text += event.unicode

                if input_box.text == '' and not input_box.active:
                    placeholder = font.render("Digite aqui...", True, pygame.Color('gray'))
                    screen.blit(placeholder, (input_box.x + 5, input_box.y + 8))
                else:
                    txt_surface = font.render(input_box.text, True, pygame.Color('white'))
                    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 8))

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(input_box.x, input_box.y, input_box.width, input_box.height).collidepoint(event.pos):
                    input_box.active = True
                else:
                    input_box.active = False

        screen.fill(Tool.rgb(Config.color['background']))
        space.step(1 / 60)
        space.debug_draw(draw_options)

        canvas.fill(Tool.rgb(Config.color['background']))
        map.draw_map(canvas)
        screen.blit(canvas, (0, 0))

        # Desenha InputBox
        color = pygame.Color('lightskyblue3') if input_box.active else pygame.Color('gray')
        pygame.draw.rect(screen, color, (input_box.x, input_box.y, input_box.width, input_box.height), 2, border_radius=10)
        txt_surface = font.render(input_box.text, True, pygame.Color('white'))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 8))
        

        pygame.display.flip()
        clock.tick(Config.FPS)

if __name__ == "__main__":
    Start()
