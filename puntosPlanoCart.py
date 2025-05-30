import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def distanciaxy(self, x, y):
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
    
    def distanciapunto(self, otro_punto):
        return math.sqrt((self.x - otro_punto.get_x()) ** 2 + (self.y - otro_punto.get_y()) ** 2)
    
punto1 = Punto(0, 0)
punto2 = Punto(1, 1)
print(punto1.distanciapunto(punto2))  # Distancia entre dos puntos
print(punto2.distanciaxy(2, 0))  # Distancia entre un punto y coordenadas (x, y)