import pygame
import pymunk
import pymunk.pygame_util
from tool import tool
from data import data
import asyncio

#Declaração de variáveis
color = {
        'white': "#BDBDBD",
        'black': "#000000",
        'gray': "#3D3D3D",
        'blue': "#6C6AE2",
        'yellow': "#D8DF82",
        'red': "#FF6969",
        'orange': "#FFB972",
        'green': "#82F77C",
    }

#Iniliza Uma data local para haver modificaçoes no atributo
data_local = data()
pygame.init()

#Atribuições para inicialização (pygame e pymunk)
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
fonte = pygame.font.Font(None, 32)

space = pymunk.Space()
space.gravity = (0, 200)

draw_options = pymunk.pygame_util.DrawOptions(screen)

#Variáveis de controle
control_ball = True #As variáveis de controle no pygame são essenciais para todos os objetos que se locomovem pela tela
running = True #Variável de controle do loop principal

#Variáveis dos inputs

#Loop principal
while running:
    #Eventos de interação do usuário
    for event in pygame.event.get(): 
        #Interrupção da execução do jogo
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #Interações com o teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    screen.fill(tool.rgb(color['white']))
    
    #Atualização dos quadros de física (pymunk)
    space.step(1 / 60)
    space.debug_draw(draw_options)
    
    #Display e Taxa de quadros (pygame)
    pygame.display.flip()
    clock.tick(60)

def Start():
    print("oi")

async def main():
    asyncio.create_task(tool.verify_modules())
    asyncio.create_task(tool.add_path_modules(data_local))
    return

if __name__ == "__main__":
    asyncio.run(main())
    Start()