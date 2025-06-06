import pygame
import pymunk
from tool import tool
from data import data
import asyncio

#Iniliza Uma data local para haver modificaçoes no atributo
data_local = data()

def Start():
    print("oi")

async def main():
    asyncio.create_task(tool.verify_modules())
    asyncio.create_task(tool.add_path_modules(data_local))
    return

if __name__ == "__main__":
    asyncio.run(main())
    Start()