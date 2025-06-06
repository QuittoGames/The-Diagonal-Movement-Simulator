import pygame
from tool import tool
from data import data
import asyncio

#Iniliza Uma data local para haver modificaçoes no atributo
data_local = data()

def Start():
    pass

def main():
    asyncio.create_task(tool.add_path_modules())
    asyncio.create_task(tool.verify_modules())
    return

if __name__ == "__main__":
    main()
    Start()