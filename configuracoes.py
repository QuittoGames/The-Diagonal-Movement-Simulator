import pygame

largura, altura = 1200, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Movimento Parabólico - Pygame + Pymunk')

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
CINZA = (120, 120, 120)

fonte_padrao = pygame.font.SysFont('Arial', 18)
fonte_input = pygame.font.SysFont('Arial', 22)

