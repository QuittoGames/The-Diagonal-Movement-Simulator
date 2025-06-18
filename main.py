import pygame
import pymunk
import math

pygame.init()

from configuracoes import largura, altura, tela, BRANCO, PRETO, VERMELHO, CINZA, fonte_padrao
from assets import background
from interface.input_box import InputBox
from interface.botao import Botao
from fisica.objetos import criar_chao, criar_bola
from utils.funcoes import get_img_bola_redimensionada, desenhar_canhao_img

espaco = pymunk.Space()
espaco.gravity = (0, 981)

criar_chao(espaco, altura, largura)

pos_x_canhao = 80

input_velocidade = InputBox(1100, 10, 80, 30, '500', label='Velocidade:')
input_altura = InputBox(1100, 50, 80, 30, '150', label='Altura (px):')
input_raio = InputBox(1100, 90, 80, 30, '10', label='Raio (px):')
input_gravidade = InputBox(1100, 130, 80, 30, '1000', label='Gravidade:')
input_angulo = InputBox(1100, 170, 80, 30, '20', label='Ângulo (°):')
input_massa = InputBox(1100, 210, 80, 30, '1', label='Massa (kg):')
input_inercia = InputBox(1100, 250, 80, 30, '1', label='Inércia:')
caixas = [input_velocidade, input_altura, input_raio, input_gravidade, input_angulo, input_massa, input_inercia]

botao_reset = Botao(1100, 300, 80, 30, 'reset')

trajetoria = []
bola = None
tempo_inicial = None
bola_parada = False
erro_msg = ''

rodando = True
relogio = pygame.time.Clock()

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        for caixa in caixas:
            caixa.handle_event(evento)

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if botao_reset.clicado(evento.pos):
                if bola:
                    espaco.remove(bola, *bola.shapes)
                    bola = None
                    trajetoria.clear()
                    bola_parada = False
                    tempo_inicial = None
                    erro_msg = ''

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE and not bola:
            dx = pygame.mouse.get_pos()[0] - pos_x_canhao
            dy = (altura - 50 - input_altura.get_valor()) - pygame.mouse.get_pos()[1]
            angulo = math.degrees(math.atan2(dy, dx))
            angulo = max(0, min(90, angulo))

            input_angulo.texto = f'{angulo:.2f}'
            input_angulo.txt_surface = input_angulo.fonte.render(input_angulo.texto, True, PRETO)

            velocidade = input_velocidade.get_valor()
            raio = input_raio.get_valor()
            altura_input = input_altura.get_valor()
            massa_valor = input_massa.get_valor()
            inercia_valor = input_inercia.get_valor()

            if not (10 <= velocidade <= 1000):
                erro_msg = 'Velocidade fora do limite'
                continue
            if not (1 <= raio <= 100):
                erro_msg = 'Raio inválido'
                continue
            if not (0 <= altura_input <= 485):
                erro_msg = 'Altura fora do campo'
                continue
            if massa_valor <= 0:
                erro_msg = 'Massa deve ser > 0'
                continue
            if inercia_valor <= 0:
                erro_msg = 'Inércia deve ser > 0'
                continue

            altura_canhao = altura - 50 - altura_input
            canhao_x, canhao_y = pos_x_canhao, altura_canhao
            ponta_x, ponta_y = desenhar_canhao_img(tela, canhao_x, canhao_y, angulo)

            bola = criar_bola(espaco, ponta_x, ponta_y, velocidade, math.radians(angulo), raio, massa_valor, inercia_valor, VERMELHO)
            tempo_inicial = pygame.time.get_ticks()
            trajetoria.clear()
            bola_parada = False
            erro_msg = ''

    tela.blit(background, (0, 0))

    for caixa in caixas:
        caixa.draw(tela)

    angulo = input_angulo.get_valor()
    altura_canhao = altura - 50 - input_altura.get_valor()
    ponta_x, ponta_y = desenhar_canhao_img(tela, pos_x_canhao, altura_canhao, angulo)

    img_bola = get_img_bola_redimensionada(input_raio.get_valor())
    tela.blit(img_bola, img_bola.get_rect(center=(int(ponta_x), int(ponta_y))))

    if bola:
        tempo_atual = pygame.time.get_ticks() - tempo_inicial
        x, y = bola.position
        if not bola_parada:
            trajetoria.append((int(x), int(y)))
        if len(trajetoria) > 1:
            pygame.draw.lines(tela, CINZA, False, trajetoria, 2)
        img_bola = get_img_bola_redimensionada(list(bola.shapes)[0].radius)
        tela.blit(img_bola, img_bola.get_rect(center=(int(x), int(y))))
        if not bola_parada and tempo_atual > 1000:
            vx, vy = bola.velocity
            if abs(vy) < 5 and abs(bola.position.y - (altura - 60)) < 3:
                bola.velocity = (0, 0)
                bola.angular_velocity = 0
                bola.body_type = pymunk.Body.STATIC
                bola_parada = True

    if erro_msg:
        tela.blit(fonte_padrao.render(f'Erro: {erro_msg}', True, VERMELHO), (880, 300))

    botao_reset.draw(tela)

    espaco.gravity = (0, input_gravidade.get_valor())
    espaco.step(1 / 60.0)
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()