import pygame

class Inputbox:
    def __init__(left, top, width, height,color ,border,self):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.color = color
        self.border = border

    def __str__(self):
        return (f'left={self.left}\ttop={self.top}\twidth={self.width}\theight={self.height}\tcolor={self.color}\tborder={self.border}')