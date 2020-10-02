print("Hello Isidora")
import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def obtener_area(self):
        area = math.pi * self.radio * self.radio
        return area

    def obtener_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro

    def __str__(self):
        imprimir = ("El circulo de radio " + str(radio) + " cm es de área " + str(
            circulo.obtener_area()) + " cm2 y de perimetro " + str(circulo.obtener_perimetro()) + " cm")
        return imprimir


class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def obtener_area(self):
        area = self.largo * self.ancho
        return area

    def obtener_perimetro(self):
        perimetro = self.largo * 2 + self.ancho * 2
        return perimetro

    def es_cuadrado(self):
        if self.largo == self.ancho:
            hola = True
        else:
            hola = False
        return hola

    def __str__(self):
        imprimir = ("El rectangulo de largo " + str(self.largo) + " cm y de ancho " + str(
            self.ancho) + " cm es de área " + str(rectangulo.obtener_area()) + " cm2 y de perimetro " + str(
            rectangulo.obtener_perimetro()) + " cm y es cuadrado "+str(rectangulo.es_cuadrado()))
        return imprimir


radio = int(input("Ingrese radio en cm: "))
circulo = Circulo(radio)
print(circulo)

largo = int(input("Ingrese el largo en cm: "))
ancho = int(input("Ingrese el ancho en cm: "))
rectangulo = Rectangulo(largo, ancho)
print(rectangulo)