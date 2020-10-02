from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.Qt import QTest


class Jugador(QObject):
    def __init__(self,nombre):
        self.nombre=nombre