import pygame
import pymunk
import math

pygame.init()

from configuracoes import largura, altura, tela, BRANCO, PRETO, VERMELHO, CINZA, fonte_padrao
from assets import background
from interface.input_box import InputBox
from interface.inputbox_equacao import InputBoxEquacao
from interface.botao import Botao
from interface.box_info import BoxInfo
from fisica.objetos import criar_chao, criar_bola
from utils.funcoes import get_img_bola_redimensionada, desenhar_canhao_img

# ==============================
# FÍSICA E CONVERSÕES
# ==============================
PIXELS_POR_METRO = 100

def metros_para_pixels(metros):
    return metros * PIXELS_POR_METRO

def pixels_para_metros(pixels):
    return pixels / PIXELS_POR_METRO

def calcular_cinematica(v0, angulo_graus, gravidade):
    angulo_rad = math.radians(angulo_graus)
    v0x = v0 * math.cos(angulo_rad)
    v0y = v0 * math.sin(angulo_rad)
    t_subida = v0y / gravidade
    h_max = (v0y ** 2) / (2 * gravidade)
    t_total = 2 * t_subida
    alcance = v0x * t_total
    return {
        "v0": v0,
        "v0x": v0x,
        "v0y": v0y,
        "t_subida": t_subida,
        "h_max": h_max,
        "t_total": t_total,
        "alcance": alcance,
        "gravidade": gravidade
    }

def calcular_velocidade_instantanea(v0y, gravidade, tempo, v0x):
    vy = v0y - gravidade * tempo
    v = math.sqrt(v0x ** 2 + vy ** 2)
    return v, vy

def menu_inicial():
    fonte_titulo = pygame.font.SysFont(None, 60)
    titulo = fonte_titulo.render("Simulador de Lançamento Oblíquo", True, PRETO)
    titulo_rect = titulo.get_rect(center=(largura // 2, altura // 2.2))

    botao_iniciar = Botao(largura // 2 - 100, altura // 2 + 20, 200, 50, 'Iniciar Simulação')

    esperando_inicio = True
    while esperando_inicio:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_iniciar.clicado(evento.pos):
                    esperando_inicio = False

        tela.blit(background, (0, 0))
        tela.blit(titulo, titulo_rect)
        botao_iniciar.draw(tela)
        pygame.display.flip()

# ==============================
# CONFIGURAÇÕES INICIAIS
# ==============================
espaco = pymunk.Space()
espaco.gravity = (0, 981)

criar_chao(espaco, altura, largura)

pos_x_canhao = 345

input_velocidade = InputBox(1100, 10, 80, 30, '5', label='Velocidade:')
input_altura = InputBox(1100, 50, 80, 30, '1.5', label='Altura (m):')
input_raio = InputBox(1100, 90, 80, 30, '0.1', label='Raio (m):')
input_gravidade = InputBox(1100, 130, 80, 30, '9.8', label='Gravidade:')
input_angulo = InputBox(1100, 170, 80, 30, '20', label='Ângulo (°):')
input_massa = InputBox(1100, 210, 80, 30, '1', label='Massa (kg):')
input_inercia = InputBox(1100, 250, 80, 30, '1', label='Inércia:')

caixas = [input_velocidade, input_altura, input_raio, input_gravidade, input_angulo, input_massa, input_inercia]

botao_reset = Botao(1100, 300, 80, 30, 'Reset')
botao_mostrar_calculos = Botao(10, 10, 280, 30, 'Apresentar Cálculos')

y_inicial_info = 50
caixas_info = [
    BoxInfo(10, y_inicial_info + i * 35, 280, 30, label)
    for i, label in enumerate([
        "Velocidade inicial",
        "v0x",
        "v0y",
        "Tempo de subida",
        "Altura máxima",
        "Tempo total de voo",
        "Alcance horizontal",
    ])
]

def atualizar_caixas_info(caixas, dados, tempo_voo):
    valores = [
        dados["v0"],
        dados["v0x"],
        dados["v0y"],
        dados["t_subida"],
        dados["h_max"],
        dados["t_total"],
        dados["alcance"],
    ]

    for caixa, valor in zip(caixas, valores):
        caixa.atualizar_valor(valor)

mostrar_calculos = False
trajetoria = []
bola = None
tempo_inicial = None
bola_parada = False
erro_msg = ''
dados_fisicos = None

menu_inicial()

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
                    dados_fisicos = None
                    mostrar_calculos = False

            if botao_mostrar_calculos.clicado(evento.pos):
                mostrar_calculos = not mostrar_calculos

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE and not bola:
            angulo = input_angulo.get_valor()

            velocidade_metros = input_velocidade.get_valor()
            velocidade = metros_para_pixels(velocidade_metros)

            altura_metros = input_altura.get_valor()
            altura_input = metros_para_pixels(altura_metros)

            raio_metros = input_raio.get_valor()
            raio = metros_para_pixels(raio_metros)

            gravidade_metros = input_gravidade.get_valor()
            gravidade = metros_para_pixels(gravidade_metros)

            massa_valor = input_massa.get_valor()
            inercia_valor = input_inercia.get_valor()

            if not (1 <= velocidade <= 5000):
                erro_msg = 'Velocidade fora do limite'
                continue
            if not (1 <= raio <= 100):
                erro_msg = 'Raio inválido'
                continue
            if not (metros_para_pixels(0.1) <= altura_input <= metros_para_pixels(4.85)):
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
            dados_fisicos = calcular_cinematica(velocidade_metros, angulo, gravidade_metros)
            atualizar_caixas_info(caixas_info, dados_fisicos, 0)

    tela.blit(background, (0, 0))

    for caixa in caixas:
        caixa.draw(tela)

    botao_mostrar_calculos.draw(tela)
    botao_reset.draw(tela)

    angulo = input_angulo.get_valor()
    altura_canhao = altura - 50 - metros_para_pixels(input_altura.get_valor())
    ponta_x, ponta_y = desenhar_canhao_img(tela, pos_x_canhao, altura_canhao, angulo)

    if bola:
        tempo_atual = pygame.time.get_ticks() - tempo_inicial
        x, y = bola.position
        raio_bola = list(bola.shapes)[0].radius
        y_chao = altura - 10

        if not bola_parada:
            trajetoria.append((int(x), int(y)))

            vx, vy = bola.velocity

            if (y + raio_bola) >= y_chao and vy > 0:
                espaco.remove(bola, *bola.shapes)

                corpo_estatico = pymunk.Body(body_type=pymunk.Body.STATIC)
                corpo_estatico.position = (x, y_chao - raio_bola)
                forma = pymunk.Circle(corpo_estatico, raio_bola)
                forma.color = VERMELHO
                espaco.add(corpo_estatico, forma)

                bola = corpo_estatico
                bola_parada = True

        if len(trajetoria) > 1:
            pygame.draw.lines(tela, CINZA, False, trajetoria, 2)

        img_bola = get_img_bola_redimensionada(raio_bola)
        tela.blit(img_bola, img_bola.get_rect(center=(int(x), int(y))))

        if dados_fisicos and mostrar_calculos:
            atualizar_caixas_info(caixas_info, dados_fisicos, tempo_atual / 1000)
            for caixa in caixas_info:
                caixa.draw(tela)

    if erro_msg:
        texto_erro = f'Erro: {erro_msg}'
        superficie_erro = fonte_padrao.render(texto_erro, True, VERMELHO)
        ret_erro = superficie_erro.get_rect(center=(largura // 2, 40))
        tela.blit(superficie_erro, ret_erro)

    espaco.gravity = (0, metros_para_pixels(input_gravidade.get_valor()))
    espaco.step(1 / 60.0)
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()