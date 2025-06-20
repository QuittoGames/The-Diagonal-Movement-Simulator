import math

# Fator de conversão: 100 pixels = 1 metro
PIXELS_POR_METRO = 100

def metros_para_pixels(metros):
    return metros * PIXELS_POR_METRO

def pixels_para_metros(pixels):
    return pixels / PIXELS_POR_METRO

def calcular_cinematica(v0, angulo_graus, gravidade):
    angulo_rad = math.radians(angulo_graus)

    # Componentes da velocidade
    v0x = v0 * math.cos(angulo_rad)
    v0y = v0 * math.sin(angulo_rad)

    # Tempo de subida
    t_subida = v0y / gravidade

    # Altura máxima
    h_max = (v0y ** 2) / (2 * gravidade)

    # Tempo total
    t_total = 2 * t_subida

    # Alcance horizontal
    alcance = v0x * t_total

    return {
        "v0": v0,
        "v0x": v0x,
        "v0y": v0y,
        "t_subida": t_subida,
        "h_max": h_max,
        "t_total": t_total,
        "alcance": alcance
    }

def calcular_velocidade_instantanea(v0y, gravidade, tempo, v0x):
    vy = v0y - gravidade * tempo
    v = math.sqrt(v0x**2 + vy**2)
    return v, vy
