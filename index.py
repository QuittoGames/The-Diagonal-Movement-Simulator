import pygame
import pymunk
from tool import tool
from data import data
import asyncio

#Iniliza Uma data local para haver modificaçoes no atributo
data_local = data()
pygame.init()

#Variáveis de controle
control_ball = True #As variáveis de controle no pygame são essenciais para todos os objetos que se locomovem pela tela
control_floor = True
control_loop = True #Variável de controle do loop principal

#Loop principal
while control_loop:
    for event in pygame.event.get(): #Eventos de interação do usuário
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def Start():
    print("oi")

async def main():
    asyncio.create_task(tool.verify_modules())
    asyncio.create_task(tool.add_path_modules(data_local))
    return

if __name__ == "__main__":
    asyncio.run(main())
    Start()