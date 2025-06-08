import pymunk

class ball:
    #Valores de atribuição padrão para a bola
    position = [300, 100] #x, y
    mass = 1
    radius = 25
    inertia = 100
    elasticity = 0.9

    #Método construtor da bola
    def ball(space, position, mass, radius, inertia, elasticity):
        body = pymunk.Body(mass, inertia)
        body.position = position
        shape = pymunk.Circle(body, radius)
        shape.elasticity = elasticity
        space.add(body, shape)
        return body, shape