import pymunk

class projectile:
    #Método construtor
    def __init__(self, space, position, mass, radius, inertia, elasticity):
        self.mass = mass
        self.radius = radius
        self.inertia = inertia
        self.elasticity = elasticity
        self.position = position

        self.body = pymunk.Body(mass, inertia)
        self.body.position = position
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = elasticity
        space.add(self.body, self.shape)

    #toString
    def __str__(self):
        return (f'Ball:\npos x:{self.body.position[0]} y:{self.body.position[0]}\tmass={self.mass}\tradius={self.radius}\tinertia={self.inertia}\telasticity={self.elasticity}')

