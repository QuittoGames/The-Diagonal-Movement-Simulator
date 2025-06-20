import pygame
from configuracoes import BRANCO, PRETO, fonte_input

class BoxInfo:
    def __init__(self, x, y, w, h, label='', valor=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.label = label
        self.valor = valor
        self.color_inativo = pygame.Color('#A9CCE3')
        self.color_ativo = pygame.Color('#2471A3')
        self.color = self.color_inativo
        self.fonte = fonte_input
        self.texto = f"{label}: {valor}"
        self.txt_surface = self.fonte.render(self.texto, True, PRETO)

    def atualizar_valor(self, valor):
        self.valor = valor
        self.texto = f"{self.label}: {self.valor:.2f}"
        self.txt_surface = self.fonte.render(self.texto, True, PRETO)

    def draw(self, tela):
        pygame.draw.rect(tela, BRANCO, self.rect, border_radius=8)
        pygame.draw.rect(tela, self.color, self.rect, 2, border_radius=8)
        texto_y = self.rect.y + (self.rect.height - self.txt_surface.get_height()) // 2
        tela.blit(self.txt_surface, (self.rect.x + 8, texto_y))
