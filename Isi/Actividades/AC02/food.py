from abc import ABC
import random


# Completar las clases donde corresponda #


class Pizza:
    def __init__(self, ingredientes):
        self._calidad = random.randint(50, 200)
        self.ingredientes = ingredientes
        self.tiempo = random.randint(20, 100)
        # Rellenar Aquí

    def revisar_tiempo(self):
        if self.tiempo >= 30:
            self.calidad -= 30
        # Rellenar Aquí


    def revisar_ingredientes(self):
        if "piña" in self.ingredientes:
            self.calidad -= 50
        if "pepperoni" in self.ingredientes:
            self.calidad += 50
        # Rellenar Aquí


    @property
    def calidad(self):
        return self._calidad

    @calidad.setter  # Se controla que la calidad no sea negativa
    def calidad(self, valor):
        self._calidad = max(0, valor)


class Bebestible(ABC):
    def __init__(self):
        self._calidad = random.randint(50, 150)

    @property
    def calidad(self):
        return self._calidad

    @calidad.setter  # Se controla que la calidad no sea negativa
    def calidad(self, valor):
        self._calidad = max(0, valor)


class Plato(Pizza,Bebestible):
    def __init__(self,ingredientes):
        Pizza.__init__(self,ingredientes)
        Bebestible.__init__(self)
        self.pizza = None
        self.bebestible = None

# Rellenar Aquí con las nuevas clases #

class Agua(Bebestible):
    def __init__(self):
    super().__init__(self)

    def tipo_bebestible(self):
        self.calidad += 30

class Gaseosa(Bebestible):
    def __init__(self):
        super().__init__(self)
        lista_sabores=["Coca-Cola","Pepsi","Sprite"]
        self.sabor=random.choice(lista_sabores)

    def tipo_bebestible(self):
        self.calidad -= 30



