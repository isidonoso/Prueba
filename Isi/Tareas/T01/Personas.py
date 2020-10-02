from random import randint as rand
from data.constantes import MIN_HP_PERSONA as min_hp, MAX_HP_PERSONA as max_hp, \
    MIN_ATAQUE_SOLDADO as min_ataque, MAX_ATAQUE_SOLDADO as max_ataque, \
    MIN_IQ_AYUDANTE as min_iq, MAX_IQ_AYUDANTE as max_iq, \
    MIN_CANTIDAD_RECURSO as min_recurso, MAX_CANTIDAD_RECURSO as max_recurso


class Persona():
    def __init__(self):
        self.max_hp = rand(min_hp, max_hp)
        self.hp_persona = self.max_hp
        self.disponibilidad = ["D", 0]


class Trabajador(Persona):
    def __init__(self):
        super().__init__()

    def recolectar_recursos(self, trabajador):
        recolectado = rand(min_recurso, max_recurso)
        trabajador.disponibilidad = ["O", 1]
        return recolectado

    def construir_edificio(self, turnos):
        self.disponibilidad = ["O", turnos]


class Soldado(Persona):
    def __init__(self):
        super().__init__()
        self.poder_de_fuerza = rand(min_ataque, max_ataque)

    def ocupado(self, turnos):
        self.disponibilidad = ["O", turnos]


class Ayudante(Persona):
    def __init__(self):
        super().__init__()
        iq = rand(min_iq, max_iq)
        self.iq_ayudante = iq
