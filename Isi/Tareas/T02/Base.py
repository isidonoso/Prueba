from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QProgressBar

import parametros as p


class EdificioBase(QThread):
    def __init__(self):
        super().__init__()
        self.hp = p.HP_BASE
        self.barra = QProgressBar()
        self.barra.setTextVisible(True)

    def actualizar(self):
        pass

    def run(self):
        while self.hp > 0:
            self.barra.actualizar()
