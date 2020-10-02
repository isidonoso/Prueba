from PyQt5.QtCore import pyqtSignal, QThread

import parametros as p
from Eventos import Mover


class Personaje(QThread):
    mover_entidad = pyqtSignal(Mover)

    def __init__(self, x_ini, y_ini, largo, ancho, bloqueados):
        super().__init__()
        self.bloqueados = bloqueados
        self.ancho = ancho
        self.largo = largo
        self._x = x_ini
        self._y = y_ini
        self.pause = False
        self.monedas = 0

    def recolectar_monedas(self):
        pass

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        chequeo = 0
        NoPasar = False
        if (value - self.x) < 0:
            resto = value % p.PIXELES
            if resto == p.PIXELES - p.SPEED_PLAYER:
                entero = value // p.PIXELES
                columna = ((self.y) // p.PIXELES) * p.PIXELES
                fila = entero * p.PIXELES
                chequeo = 1
        else:
            resto = (value + p.ANCHO_P) % p.PIXELES
            if resto == 0:
                entero = (value + p.ANCHO_P) // p.PIXELES
                columna = ((self.y) // p.PIXELES) * p.PIXELES
                fila = entero * p.PIXELES
                chequeo = 1

        if chequeo == 1:
            for a in range(len(self.bloqueados)):
                col = self.bloqueados[a][0]
                fil = self.bloqueados[a][1]
                if (col == columna and fil == fila):
                    NoPasar = True
                    break
        if (value - self.x) < 0:
            resto = value % p.PIXELES
            if resto == p.PIXELES - p.SPEED_PLAYER:
                entero = value // p.PIXELES
                columna = (((self.y) + p.LARGO_P) // p.PIXELES) * p.PIXELES
                fila = entero * p.PIXELES
                chequeo = 1
        else:
            resto = (value + p.ANCHO_P) % p.PIXELES
            if resto == 0:
                entero = (value + p.ANCHO_P) // p.PIXELES
                columna = (((self.y) + p.LARGO_P) // p.PIXELES) * p.PIXELES
                fila = entero * p.PIXELES
                chequeo = 1

        if chequeo == 1:
            for a in range(len(self.bloqueados)):
                col = self.bloqueados[a][0]
                fil = self.bloqueados[a][1]
                if (col == columna and fil == fila):
                    NoPasar = True
                    break

        if NoPasar == False:
            if value < 0:
                self._x = 0
            elif value > p.PIXELES * self.ancho - p.ANCHO_P:
                self._x = p.PIXELES * self.ancho - p.ANCHO_P
            else:
                self._x = value
        else:
            self._x = self.x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, valor):

        chequeo = 0
        NoPasar = False
        if (valor - self.y) < 0:
            resto = valor % p.PIXELES
            if resto == p.PIXELES - p.SPEED_PLAYER:
                entero = valor // p.PIXELES
                columna = entero * p.PIXELES
                fila = ((self.x) // p.PIXELES) * p.PIXELES
                chequeo = 1
        else:
            resto = (valor + p.LARGO_P) % p.PIXELES
            if resto == 0:
                entero = (valor + p.LARGO_P) // p.PIXELES
                columna = entero * p.PIXELES
                fila = ((self.x) // p.PIXELES) * p.PIXELES
                chequeo = 1

        if chequeo == 1:
            for x in range(len(self.bloqueados)):
                col = self.bloqueados[x][0]
                fil = self.bloqueados[x][1]
                if (col == columna and fil == fila):
                    NoPasar = True
                    break
        chequeo = 0
        if (valor - self.y) < 0:
            resto = valor % p.PIXELES
            if resto == p.PIXELES - p.SPEED_PLAYER:
                entero = valor // p.PIXELES
                columna = entero * p.PIXELES
                fila = (((self.x) + p.ANCHO_P) // p.PIXELES) * p.PIXELES
                chequeo = 1
        else:
            resto = (valor + p.LARGO_P) % p.PIXELES
            if resto == 0:
                entero = (valor + p.LARGO_P) // p.PIXELES
                columna = entero * p.PIXELES
                fila = (((self.x) + p.ANCHO_P) // p.PIXELES) * p.PIXELES
                chequeo = 1

        if chequeo == 1:
            for x in range(len(self.bloqueados)):
                col = self.bloqueados[x][0]
                fil = self.bloqueados[x][1]
                if (col == columna and fil == fila):
                    NoPasar = True
                    break

        if NoPasar == False:
            if valor < 0:
                self._y = 0
            elif valor > p.PIXELES * self.largo - p.LARGO_P:
                self._y = p.PIXELES * self.largo - p.LARGO_P
            else:
                self._y = valor
        else:
            self._y = self.y

    def pausa(self):
        pass
        if self.pause == False:
            self.pause = True
        else:
            self.pause = False

    def refresh_pos(self):
        self.mover_entidad.emit(Mover(self.x, self.y))

    def move(self, event):
        if self.pause == False:
            if event.lado == "right":
                self.x += p.SPEED_PLAYER
            elif event.lado == "left":
                self.x -= p.SPEED_PLAYER
            elif event.lado == "Up":
                self.y -= p.SPEED_PLAYER
            elif event.lado == "Down":
                self.y += p.SPEED_PLAYER
            self.refresh_pos()
        else:
            pass
