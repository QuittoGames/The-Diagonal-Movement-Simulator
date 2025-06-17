import pygame
import pymunk
import pymunk.pygame_util
from tool import tool
from data import data
import math
import asyncio

#Iniliza Uma data local para haver modificaçoes no atributo
data_local = data()
pygame.init()

def Start():
    pygame.display(100,100)

async def main():
    asyncio.create_task(tool.verify_modules())
    asyncio.create_task(tool.add_path_modules(data_local))
    return

if __name__ == "__main__":
    asyncio.run(main())
    Start()


# Inicialização do pygame
pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Movimento Oblíquo com Pymunk")
relogio = pygame.time.Clock()

# Inicialização do pymunk
espaco = pymunk.Space()
espaco.gravity = (0, 900)  # Gravidade puxando para baixo (y positivo)

# Desenhador do pymunk para pygame
draw_options = pymunk.pygame_util.DrawOptions(tela)

# Função para criar o projétil
def criar_projetil(posicao, velocidade, angulo_graus):
    massa = 1
    raio = 10
    inercia = pymunk.moment_for_circle(massa, 0, raio)
    corpo = pymunk.Body(massa, inercia)
    corpo.position = posicao

    angulo_radianos = math.radians(angulo_graus)
    vx = velocidade * math.cos(angulo_radianos)
    vy = -velocidade * math.sin(angulo_radianos)  # Negativo pois o y cresce para baixo no Pygame

    corpo.velocity = (vx, vy)

    forma = pymunk.Circle(corpo, raio)
    forma.elasticity = 0.6
    forma.friction = 0.5

    espaco.add(corpo, forma)
    return corpo, forma

# Função para criar o chão
def criar_chao():
    corpo_estatico = espaco.static_body
    segmento = pymunk.Segment(corpo_estatico, (0, altura - 50), (largura, altura - 50), 5)
    segmento.elasticity = 0.9
    segmento.friction = 1.0
    espaco.add(segmento)

criar_chao()
projetil = None

# Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # Cria o projétil no canto inferior esquerdo
            posicao_inicial = (50, altura - 60)
            velocidade_inicial = 400  # pixels por segundo
            angulo_inicial = 45  # graus
            projetil, forma = criar_projetil(posicao_inicial, velocidade_inicial, angulo_inicial)

    tela.fill((30, 30, 30))  # fundo escuro

    espaco.step(1/60.0)  # atualiza física
    espaco.debug_draw(draw_options)  # desenha os objetos

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
