from food import Pizza, Gaseosa, Agua, Plato
from abc import ABC, abstractmethod
import random


# Completar las clases donde corresponda #


class Personalidad(ABC):
    def reaccionar(self, plato):
        # Rellenar aquí
        pizza=plato.pizza
        bebestible=plato.bebestible
        if (pizza.calidad + bebestible.calidad)/2 >= 50:
            self.feliz()
        else:
            self.molesto()

    @abstractmethod
    def feliz(self):
        pass

    @abstractmethod
    def molesto(self):

        pass

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

# Rellenar Aquí con las nuevas clases #

class Empatico:
    def __init__(self):
        pass

    def feliz(self):
        print("Cosa ma wena, voy a poner puros 7")

    def molesto(self):
        print("No me gustó, pondré puros 5")

class Exigente:
    def __init__(self,nombre):
        pass

    def feliz(self):
        print("Esta merienda está muy buena, los alumnos se merecen el 4")

    def molesto(self):
        print("Que bruto, póngale 0")

class Chef(Persona):
    def __init__(self,nombre):
        super().__init__(self,nombre)

    def ingredientes(self):
        lista_ing = ["pepperoni", "piña", "cebolla", "tomate", "jamón", "pollo"]
        ing_1 = random.choice(lista_ing)
        ing_2 = random.choice(lista_ing)
        ing_3 = random.choice(lista_ing)
        ingredientes = [ing_1,ing_2,ing_3]
        return ingredientes

    def Preparar_Plato(self,Plato):
        pass

class Ayudante(Persona):
    def __init__(self,nombre,personalidad):
        super().__init__(self, nombre)
        self._personalidad=personalidad