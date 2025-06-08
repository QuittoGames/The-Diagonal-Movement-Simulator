import os
import platform
from dataclasses import dataclass
import subprocess
from data import data
import sys

@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    async def verify_modules():
        try:
            # #Uso Do modules por txt
            req_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "requirements", "requirements.txt"))
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", req_path], check=True)
        
        except Exception as E:
            print(f"Erro na verificação De módulos; Erro: {E}")
            return
        
    async def add_path_modules(data_local:data):
        if data.modules_local == None:return
        try:
            for i in data.modules_local:
                sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), i)))
                if data_local.Debug:print(f"Module_local: {i}")
            return
        except Exception as E:
            print(f"Erro ao adicionar os caminhos brutos; Erro: {E}")
            return
    
    def rgb(hexadecimal): #Exemplo de uso: rgb(color['white'])
        hexadecimal = hexadecimal.lstrip('#')
        return tuple(int(hexadecimal[i:i+2], 16) for i in (0, 2, 4))

    

    
