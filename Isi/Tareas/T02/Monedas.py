from time import sleep

from PyQt5.QtCore import QThread

from parametros import TIEMPO_MONEDA, DURACION_MONEDA


class Moneda(QThread):
    def __init__(self, x, y):
        super().__init__()
        self.duracion = DURACION_MONEDA
        self.x = x
        self.y = y
        self.pause = False

    def pausa(self):
        if self.pause == False:
            self.pause = True
        else:
            self.pause = False

    def run(self):
        sleep(TIEMPO_MONEDA)
        while self.duracion > 0:
            sleep(1)
            self.duracion -= 1
