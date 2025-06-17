from dataclasses import dataclass
import pygame

@dataclass
class Config:
    resX:int = 1296
    resY:int = 360
    FPS: int = 60
    font = r"fonts\Segoe UI.ttf"

    #Variáveis de personalização
    # fonte = pygame.font.Font(None, 32)
    color = {
            'white': "#BDBDBD",
            'black': "#000000",
            'gray': "#3D3D3D",
            'background': "#b4d2df",
        }
        