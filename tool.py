import os
import platform
from dataclasses import dataclass

@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    #Project created successfully!