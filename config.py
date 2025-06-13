from dataclasses import dataclass

@dataclass
class Config:
    resX:int
    resY:int
    resH:int
    resL:int

    FPS: int = 60

    colors = {
        "White":(255,255,255)
    }
    