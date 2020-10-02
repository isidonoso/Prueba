from time import sleep

from PyQt5.QtCore import QThread

import parametros as p


class Racimo(QThread):
    def __init__(self):
        super().__init__()
        self.imagen = "sprites/mapa/towerDefense_tile250.png"
        self.velocidad = p.SPD_RACIMO
        self.ataque = p.ATK_RACIMO
        self.radio = p.RADIO_ATAQUE
        self.mejora_a = False
        self.mejora_r = False

    def atacar(self, enemigo):
        self.lock.acquire()
        ###AQUI HAY QUE ENCONTRAR LA FORMA DE REVISAR SI ESQUE EL ENEMIGO SIGUE
        enemigo.hp -= self.ataque
        sleep(p.self.velocidad)
        self.lock.release()

    def mejora_ataque(self):
        if self.mejora_a == False:
            self.ataque = self.ataque * 3
            self.mejora_a = True

    def mejora_alcance(self):
        if self.mejora_r == False:
            self.radio = self.radio * 3
            self.mejora_r = True

    def run(self):
        pass


class Francotirador(QThread):
    def __init__(self):
        super().__init__()
        self.velocidad = p.SPD_FRANCOTIRADORA
        self.ataque = p.ATK_FRANCOTIRADORA
        self.radio = p.RADIO_ATAQUE
        self.mejora_a = False
        self.mejora_r = False

    def atacar(self, enemigo):
        self.lock.acquire()
        ###AQUI HAY QUE ENCONTRAR LA FORMA DE REVISAR SI ESQUE EL ENEMIGO SIGUE
        enemigo.hp -= p.ATK_FRANCOTIRADORA
        sleep(p.SPD_FRANCOTIRADORA)
        self.lock.release()

    def mejora_ataque(self):
        if self.mejora_a == False:
            self.ataque = self.ataque * 3
            self.mejora_a = True

    def mejora_alcance(self):
        if self.mejora_r == False:
            self.radio = self.radio * 3
            self.mejora_r = True

    def run(self):
        pass
        # INSERTAR MOVIMIENTO MARIO, una vez listo el movimiento


franco = Francotirador()
franco.start()
