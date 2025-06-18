import pygame
from configuracoes import PRETO, BRANCO, fonte_input

class InputBox:
    def __init__(self, x, y, w, h, texto='', label=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inativo = pygame.Color('#A9CCE3')
        self.color_ativo = pygame.Color('#2471A3')
        self.color = self.color_inativo
        self.texto = texto
        self.fonte = fonte_input
        self.txt_surface = self.fonte.render(texto, True, PRETO)
        self.ativo = False
        self.label = label

    def handle_event(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            self.ativo = self.rect.collidepoint(evento.pos)
            self.color = self.color_ativo if self.ativo else self.color_inativo
        if evento.type == pygame.KEYDOWN and self.ativo:
            if evento.key == pygame.K_RETURN:
                self.ativo = False
                self.color = self.color_inativo
            elif evento.key == pygame.K_BACKSPACE:
                self.texto = self.texto[:-1]
            else:
                self.texto += evento.unicode
            self.txt_surface = self.fonte.render(self.texto, True, PRETO)

    def draw(self, tela):
        label_surface = self.fonte.render(self.label, True, PRETO)
        tela.blit(label_surface, (self.rect.x - 120, self.rect.y + 5))
        pygame.draw.rect(tela, BRANCO, self.rect, border_radius=8)
        pygame.draw.rect(tela, self.color, self.rect, 2, border_radius=8)
        tela.blit(self.txt_surface, (self.rect.x + 8, self.rect.y + (self.rect.height - self.txt_surface.get_height()) // 2))

    def get_valor(self):
        try:
            return float(self.texto)
        except ValueError:
            return 0