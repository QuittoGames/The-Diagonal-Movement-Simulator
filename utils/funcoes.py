import pygame
import math
from assets import img_bola_original, img_canhao

def get_img_bola_redimensionada(raio):
    return pygame.transform.scale(img_bola_original, (int(raio * 2), int(raio * 2)))

def desenhar_canhao_img(tela, x, y, angulo_graus):
    img_rotacionada = pygame.transform.rotate(img_canhao, angulo_graus)
    rect = img_rotacionada.get_rect(center=(x, y))
    tela.blit(img_rotacionada, rect)
    comprimento = 50
    angulo_rad = math.radians(-angulo_graus)
    ponta_x = x + comprimento * math.cos(angulo_rad)
    ponta_y = y + comprimento * math.sin(angulo_rad)
    return ponta_x, ponta_y