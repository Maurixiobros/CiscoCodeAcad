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
    
class Triangulo:
    def __init__(self, vertice1, vertice2, vertice3):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.vertice3 = vertice3
        self.lado1 = vertice1.distanciapunto(vertice2)
        self.lado2 = vertice2.distanciapunto(vertice3)
        self.lado3 = vertice3.distanciapunto(vertice1)
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
Triangulo = Triangulo(Punto(0, 0), Punto(1, 0), Punto(0, 1))
print(Triangulo.perimetro())  # Perímetro del triángulo