import pygame
from configuracoes import largura, altura

background = pygame.image.load(r'background.png')
background = pygame.transform.scale(background, (largura, altura))

img_canhao_original = pygame.image.load(r'canhao.png').convert_alpha()
img_canhao = pygame.transform.scale(img_canhao_original, (100, 100))

img_bola_original = pygame.image.load(r'projetil.png').convert_alpha()