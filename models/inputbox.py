import pygame
from dataclasses import dataclass

@dataclass
class Inputbox:
    x: int
    y: int
    width: int
    height: int
    active: bool = False
    text: str = ''

    def __str__(self):
        return (f'left={self.left}\ttop={self.top}\twidth={self.width}\theight={self.height}\tcolor={self.color}\tborder={self.border}')