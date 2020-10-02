from random import randint as rand
import Personas
from collections import namedtuple


class Edificio():
    def __init__(self, turnos, trabajadores, e_oro, e_madera, e_piedra, hp_e,
                 p_oro, p_madera, p_piedra):
        self.max_hp = int(hp_e)
        self.hp_edificio = int(hp_e)
        self.disponibilidad = ["O", int(turnos)]
        self.trabajadores = int(trabajadores)
        self.madera = int(e_madera)
        self.oro = int(e_oro)
        self.piedra = int(e_piedra)
        self.p_oro = int(p_oro)
        self.p_madera = int(p_madera)
        self.p_piedra = int(p_piedra)


class DCCowork(Edificio):
    def __init__(self, turnos, trabajadores, e_oro, e_madera, e_piedra, hp_e,
                 p_oro, p_madera, p_piedra):
        super().__init__(turnos, trabajadores, e_oro, e_madera, e_piedra, hp_e,
                         p_oro,
                         p_madera, p_piedra)

    def crear_ayudantes(self, civilizacion, cantidad):
        oro = self.p_oro * cantidad
        piedra = self.p_piedra * cantidad
        madera = self.p_madera * cantidad
        c_madera = civilizacion.cantidad_madera
        c_oro = civilizacion.cantidad_oro
        c_piedra = civilizacion.cantidad_piedra
        if c_madera >= madera and c_oro >= oro and c_piedra >= piedra:
            posible = True
        else:
            posible = False
        return posible


class CentroUrbano(Edificio):
    def __init__(self, turnos, trabajadores, e_oro, e_madera, e_piedra, hp_e,
                 p_oro, p_madera, p_piedra):
        super().__init__(turnos, trabajadores, e_oro, e_madera, e_piedra, hp_e,
                         p_oro, p_madera, p_piedra)

    def crear_trabajador(self, civilizacion, cantidad):
        oro = self.p_oro * cantidad
        piedra = self.p_piedra * cantidad
        madera = self.p_madera * cantidad
        c_madera = civilizacion.cantidad_madera
        c_oro = civilizacion.cantidad_oro
        c_piedra = civilizacion.cantidad_piedra
        if c_madera >= madera and c_oro >= oro and c_piedra >= piedra:
            posible = True
        else:
            posible = False
        return posible


class Muralla(Edificio):
    def __init__(self, turnos, trbajadores, e_oro, e_madera, e_piedra, hp_e,
                 p_oro, p_madera, p_piedra):
        super().__init__(turnos, trbajadores, e_oro, e_madera, e_piedra, hp_e,
                         p_oro, p_madera, p_piedra)


class Cuartel(Edificio):
    def __init__(self, turnos, trbajadores, e_oro, e_madera, e_piedra, hp_e,
                 p_oro, p_madera, p_piedra):
        super().__init__(turnos, trbajadores, e_oro, e_madera, e_piedra, hp_e,
                         p_oro, p_madera, p_piedra)

    def crear_soldado(self, civilizacion, cantidad):
        oro = self.p_oro * cantidad
        piedra = self.p_piedra * cantidad
        madera = self.p_madera * cantidad
        c_madera = civilizacion.cantidad_madera
        c_oro = civilizacion.cantidad_oro
        c_piedra = civilizacion.cantidad_piedra
        if c_madera >= madera and c_oro >= oro and c_piedra >= piedra:
            posible = True
        else:
            posible = False
        return posible
