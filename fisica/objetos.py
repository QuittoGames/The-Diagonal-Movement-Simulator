import pymunk
import math

def criar_chao(espaco, altura, largura):
    chao = pymunk.Segment(espaco.static_body, (0, altura - 115), (largura, altura - 115), 5)
    chao.elasticity = 0.1
    espaco.add(chao)
    return chao

def criar_bola(espaco, x, y, velocidade, angulo_rad, raio, massa, inercia, cor):
    momento = pymunk.moment_for_circle(massa, 0, raio) * inercia
    corpo = pymunk.Body(massa, momento)
    corpo.position = x, y
    corpo.velocity = velocidade * math.cos(angulo_rad), -velocidade * math.sin(angulo_rad)
    forma = pymunk.Circle(corpo, raio)
    forma.elasticity = 0.1
    espaco.add(corpo, forma)
    corpo.cor = cor
    return corpo