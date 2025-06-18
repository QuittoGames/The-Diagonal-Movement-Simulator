import pygame
from configuracoes import BRANCO, PRETO, fonte_input

class Botao:
    def __init__(self, x, y, w, h, texto):
        self.rect = pygame.Rect(x, y, w, h)
        self.texto = texto
        self.fonte = fonte_input
        self.color_inativo = pygame.Color('#A9CCE3')
        self.color = self.color_inativo
        self.txt_surface = self.fonte.render(texto, True, PRETO)

    def draw(self, tela):
        pygame.draw.rect(tela, BRANCO, self.rect, border_radius=8)
        pygame.draw.rect(tela, self.color, self.rect, 2, border_radius=8)
        tela.blit(
            self.txt_surface,
            (self.rect.x + (self.rect.width - self.txt_surface.get_width()) // 2,
             self.rect.y + (self.rect.height - self.txt_surface.get_height()) // 2)
        )

    def clicado(self, pos):
        return self.rect.collidepoint(pos)