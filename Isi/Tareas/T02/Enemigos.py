from os import path
from random import randint
from time import sleep

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QProgressBar

import parametros as p
from Eventos import Mover
from Mapas import mapa_para_traducir


class EnemigoNormal(QThread):
    mover = pyqtSignal(Mover)

    def __init__(self, enemigo, inicio, imagen, bloqueados):
        super().__init__()
        self.enemigo = enemigo
        self._x = inicio[0]
        self._y = inicio[1]
        self.imagen = imagen
        self.hp = p.HP_ENEMIGO
        self.bloqueados = bloqueados
        self.barra = QProgressBar()
        self.mapa = mapa_para_traducir[0]
        self.pause = False
        self.start()

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value == 0:
            col = 0
        else:
            col = (value // p.PIXELES)
        fil = self.y // p.PIXELES
        if self.mapa[fil][col] == 'C':
            self._x = value
        else:
            self._x = self.x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, valor):
        if self.x == 0:
            col = 0
        else:
            col = (self.x // p.PIXELES)
        fil = valor // p.PIXELES
        if self.mapa[fil][col] == 'C':
            self._y = valor
        else:
            self._y = self.y
            self._y = self.y

    def nueva_pos(self):
        self.mover.emit(Mover(self.x, self.y))

    def atacar_base(self, base):
        pass

    def run(self):
        while self.hp > 0:
            if self.pause == False:
                sleep(p.SPD_NORMAL)
                numero = randint(1, 4)
                if self.enemigo == "gato":
                    if numero == 1:
                        anterior = self.x
                        self.x += p.PIXELES
                        self.imagen.move(self.x, self.y)
                        if anterior != self.x:
                            self.imagen.setPixmap(QPixmap(
                                path.join("sprites", self.enemigo, "normal",
                                          "normal_15")))
                    elif numero == 2:
                        anterior = self.y
                        self.y += p.PIXELES
                        self.imagen.move(self.x, self.y)
                        if anterior != self.y:
                            self.imagen.setPixmap(QPixmap(
                                path.join("sprites", self.enemigo, "normal",
                                          "normal_13")).transformed(
                                QTransform().scale(-1, 1)))
                    elif numero == 3:
                        anterior = self.x
                        if self.x >= p.PIXELES:
                            self.x -= p.PIXELES
                        self.imagen.move(self.x, self.y)
                        if anterior != self.x:
                            self.imagen.setPixmap(QPixmap(
                                path.join("sprites", self.enemigo, "normal",
                                          "normal_03")))
                    else:
                        anterior = self.y
                        if self.y >= p.PIXELES:
                            self.y -= p.PIXELES
                        self.imagen.move(self.x, self.y)
                        if anterior != self.y:
                            self.imagen.setPixmap(QPixmap(
                                path.join("sprites", self.enemigo, "normal",
                                          "normal_13")))
                else:
                    if numero == 1:
                        anterior = self.x
                        self.x += p.PIXELES
                        self.imagen.move(self.x, self.y)
                        if anterior != self.x:
                            self.imagen.setPixmap(QPixmap(
                                path.join("sprites", self.enemigo, "normal",
                                          "normal_39")))
                    elif numero == 2:
                        anterior = self.y
                        self.y += p.PIXELES
                        self.imagen.move(self.x, self.y)
                        if anterior != self.y:
                            self.imagen.setPixmap(QPixmap(
                                path.join("sprites", self.enemigo, "normal",
                                          "normal_18")).transformed(
                                QTransform().scale(-1, 1)))
                    elif numero == 3:
                        anterior = self.x
                        if self.x >= p.PIXELES:
                            self.x -= p.PIXELES
                        self.imagen.move(self.x, self.y)
                        if anterior != self.x:
                            self.imagen.setPixmap(QPixmap(
                                path.join("sprites", self.enemigo, "normal",
                                          "normal_05")))
                    else:
                        anterior = self.y
                        if self.y >= p.PIXELES:
                            self.y -= p.PIXELES
                        self.imagen.move(self.x, self.y)
                        if anterior != self.y:
                            self.imagen.setPixmap(QPixmap(
                                path.join("sprites", self.enemigo, "normal",
                                          "normal_18")))
                self.refresh_pos()

    def refresh_pos(self):
        self.mover.emit(Mover(self.x, self.y))

    def pausa(self):
        if self.pause == False:
            self.pause = True
        else:
            self.pause = False


class EnemigoKamikaze(QThread):
    mover = pyqtSignal(Mover)

    def __init__(self, enemigo, inicio, imagen, bloqueados):
        super().__init__()
        self.enemigo = enemigo
        self._x = inicio[0]
        self._y = inicio[1]
        self.bloqueados = bloqueados
        self.largo = p.PIXELES
        self.ancho = p.PIXELES
        self.imagen = imagen
        self.imagen.show()
        self.hp = p.HP_ENEMIGO
        self.barra = QProgressBar()
        self.mapa = mapa_para_traducir[0]
        self.pause = False
        self.start()

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value == 0:
            col = 0
        else:
            col = (value // p.PIXELES)
        fil = self.y // p.PIXELES
        if self.mapa[fil][col] == 'C':
            self._x = value
        else:
            self._x = self.x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, valor):
        if self.x == 0:
            col = 0
        else:
            col = (self.x // p.PIXELES)
        fil = valor // p.PIXELES
        if self.mapa[fil][col] == 'C':
            self._y = valor
        else:
            self._y = self.y

    def nueva_pos(self):
        self.movimiento.emit(Mover(self.x, self.y))

    def colision(self, base):
        pass

    def run(self):
        while self.hp > 0:
            if self.pause == False:
                sleep(p.SPD_KAMIKAZE)
                numero = randint(1, 4)
                if self.enemigo == "gato":
                    if numero == 1:
                        anterior = self.x
                        self.x += p.PIXELES
                        self.imagen.move(self.x, self.y)
                        if anterior != self.x:
                            self.imagen.setPixmap(QPixmap(
                                path.join("sprites", self.enemigo, "kamikaze",
                                          "kamikaze_15")))
                    elif numero == 2:
                        anterior = self.y
                        self.y += p.PIXELES
                        self.imagen.move(self.x, self.y)
                        if anterior != self.y:
                            self.imagen.setPixmap(QPixmap(
                                path.join("sprites", self.enemigo, "kamikaze",
                                          "kamikaze_18")).transformed(
                                QTransform().scale(-1, 1)))
                    elif numero == 3:
                        anterior = self.x
                        if self.x >= p.PIXELES:
                            self.x -= p.PIXELES
                        self.imagen.move(self.x, self.y)
                        if anterior != self.x:
                            self.imagen.setPixmap(QPixmap(
                                path.join("sprites", self.enemigo, "kamikaze",
                                          "kamikaze_30")))
                    else:
                        anterior = self.x
                        if self.y >= p.PIXELES:
                            self.y -= p.PIXELES
                        self.imagen.move(self.x, self.y)
                        if anterior != self.y:
                            self.imagen.setPixmap(QPixmap(
                                path.join("sprites", self.enemigo, "kamikaze",
                                          "kamikaze_18")))
                else:
                    if numero == 1:
                        anterior = self.x
                        self.x += p.PIXELES
                        self.imagen.move(self.x, self.y)
                        if anterior != self.x:
                            self.imagen.setPixmap(QPixmap(
                                path.join("sprites", self.enemigo, "kamikaze",
                                          "kamikaze_32")))
                    elif numero == 2:
                        anterior = self.y
                        self.y += p.PIXELES
                        self.imagen.move(self.x, self.y)
                        if anterior != self.y:
                            self.imagen.setPixmap(QPixmap(
                                path.join("sprites", self.enemigo, "kamikaze",
                                          "kamikaze_17")).transformed(
                                QTransform().scale(-1, 1)))
                    elif numero == 3:
                        anterior = self.x
                        if self.x >= p.PIXELES:
                            self.x -= p.PIXELES
                        self.imagen.move(self.x, self.y)
                        if anterior != self.x:
                            self.imagen.setPixmap(QPixmap(
                                path.join("sprites", self.enemigo, "kamikaze",
                                          "kamikaze_01")))
                    else:
                        anterior = self.y
                        if self.y >= p.PIXELES:
                            self.y -= p.PIXELES
                        self.imagen.move(self.x, self.y)
                        if anterior != self.y:
                            self.imagen.setPixmap(QPixmap(
                                path.join("sprites", self.enemigo, "kamikaze",
                                          "kamikaze_17")))
                self.refresh_pos()

    def refresh_pos(self):
        self.mover.emit(Mover(self.x, self.y))

    def pausa(self):
        if self.pause == False:
            self.pause = True
        else:
            self.pause = False
