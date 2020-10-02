from os import path
from random import randint

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QProgressBar

import parametros as p
from Base import EdificioBase
from DragDrop import DropBox, DraggableLabel
from Enemigos import EnemigoNormal, EnemigoKamikaze
from Eventos import MoverEntidad
from Jugador import Personaje
from Mapas import mapa_para_traducir
from Monedas import Moneda
from Resultados import Resultado
from Torres import Racimo, Francotirador
from parametros import PIXELES as PIX


class Juego(QWidget):
    trigger = pyqtSignal()
    trigger_mover_entidad = pyqtSignal(MoverEntidad)

    def __init__(self, principal, enemigos, equipo, usuario):
        super().__init__()
        self.mapa = mapa_para_traducir
        self.usuario = usuario
        self.equipo = equipo
        self.principal = principal
        self.enemigo = enemigos
        self.threads = []
        self.torres = []
        self.monedas = p.MONEDAS_I
        self.init_GUI()

    def init_GUI(self):
        mapa = self.mapa[0]
        siguientes = []
        for i in range(len(self.mapa)):
            if i > 0:
                siguientes.append(self.mapa[i])
        self.mapa = siguientes
        self.largo = len(mapa)
        self.ancho = (len(mapa[0]))
        self.setWindowTitle("DCCivil War")
        self.setGeometry(0, 0, PIX * self.ancho + 250, PIX * self.largo)
        self.inicios = []
        self.bloqueados = []
        self.bloqueados_e = []
        base = 0
        for linea in range(len(mapa)):
            cuadrado = list(mapa[linea])
            contar = 0
            for i in range(len(cuadrado)):
                if cuadrado[i] == "X":
                    self.obstaculo = QLabel("", self)
                    pixmap = QPixmap(path.join("sprites", "mapa",
                                               "towerDefense_tile123.png"))
                    self.obstaculo.setGeometry(PIX * contar, PIX * linea,
                                               PIX, PIX)
                    pixmap = pixmap.scaled(PIX, PIX)
                    self.obstaculo.setPixmap(pixmap)
                    self.bloqueados.append([PIX * linea, PIX * (contar)])
                    contar += 1
                elif cuadrado[i] == "C":
                    self.camino = QLabel("", self)
                    pixmap1 = QPixmap(path.join("sprites", "mapa",
                                                "towerDefense_tile236.png"))
                    self.camino.setGeometry(PIX * contar, PIX * linea, PIX, PIX)
                    pixmap1 = pixmap1.scaled(PIX, PIX)
                    self.camino.setPixmap(pixmap1)
                    contar += 1
                elif cuadrado[i] == "B":
                    if base == 0:
                        self.base = QLabel("", self)
                        pix = QPixmap(path.join("sprites", "mapa",
                                                "towerDefense_tile236.png"))
                        self.base.setGeometry(PIX * contar, PIX * linea,
                                              PIX * 2, 2 * PIX)
                        pix = pix.scaled(PIX * 2, 2 * PIX)
                        self.base.setPixmap(pix)
                        self.base = QLabel("", self)
                        pix = QPixmap(path.join("sprites", self.enemigo,
                                                "base_cuadrada.png"))
                        self.base.setGeometry(PIX * contar, PIX * linea,
                                              PIX * 2, 2 * PIX)
                        pix = pix.scaled(PIX * 2, 2 * PIX)
                        self.base.setPixmap(pix)
                        base += 1
                        self.edificio_base = EdificioBase()
                        self.barra = QProgressBar(self)
                        self.barra.setGeometry(PIX * contar, PIX * linea,
                                              PIX * 4, round(PIX / 2))
                        self.barra.show()
                    self.bloqueados.append([PIX * linea, PIX * (contar)])
                    contar += 1
                elif cuadrado[i] == "O":
                    self.libre = QLabel("", self)
                    pixmap4 = QPixmap(path.join("sprites", "mapa",
                                                "towerDefense_tile231.png"))
                    self.libre.setGeometry(PIX * contar, PIX * linea, PIX, PIX)
                    pixmap4 = pixmap4.scaled(PIX, PIX)
                    self.libre.setPixmap(pixmap4)

                    if mapa[linea - 1][i] == 'C' or mapa[linea + 1][i] == 'C' or \
                            mapa[linea][i - 1] == 'C' or mapa[linea][
                        i + 1] == 'C':
                        self.dropbox1 = DropBox(self)
                        self.dropbox1.setGeometry(PIX * contar, PIX * linea,
                                                  PIX, PIX)

                    self.bloqueados_e.append([PIX * linea, PIX * (contar)])
                    contar += 1
                elif cuadrado[i] == "S":
                    self.inicio = QLabel("", self)
                    pixmap2 = QPixmap(path.join("sprites", "mapa",
                                                "towerDefense_tile172.png"))
                    self.inicio.setGeometry(PIX * contar, PIX * linea, PIX, PIX)
                    pixmap2 = pixmap2.scaled(PIX, PIX)
                    self.inicio.setPixmap(pixmap2)
                    contar += 1
                    self.inicios.append([PIX * (contar - 1), PIX * linea])
        self.icono = QLabel('', self)
        pixmap5 = QPixmap(
            path.join("sprites", self.equipo, "normal", "normal_logo.png"))
        self.icono.setGeometry(PIX * (contar + 1), 0, PIX * 2, 2 * PIX)
        pixmap5 = pixmap5.scaled(PIX * 2, 2 * PIX)
        self.icono.move(PIX * (contar + 1), 0)
        self.icono.setPixmap(pixmap5)
        self.nombre_usuario = QLabel("Usuario: " + self.usuario, self)
        self.n_ronda = 1
        self.nombre_usuario.move(PIX * (contar + 3) + PIX / 2, 10)
        self.ronda = QLabel("Ronda: " + str(self.n_ronda), self)
        self.ronda.move(PIX * (contar + 3) + PIX / 2, 40)
        self.cant = ((self.n_ronda - 1) * p.GENERACION_1) + p.GENERACION_2
        self.enemigos = QLabel("Cantidad de Enemigos: " + str(self.cant), self)
        self.enemigos.move(PIX * (contar + 1), 70)
        self.l_monedas = QLabel("Monedas Totales: " + str(self.monedas), self)
        self.l_monedas.move(PIX * (contar + 1), 100)
        self.monedas_r = 0
        self.monedas_ronda = QLabel("Monedas Ronda: " + str(self.monedas_r),
                                    self)
        self.monedas_ronda.move(PIX * (contar + 1), 130)
        self.progreso = QLabel("Progreso:", self)
        self.progreso1 = QProgressBar(self)
        self.progreso1.setGeometry(PIX * (contar + 1) + 50, 160, 170, 15)
        self.progreso.move(PIX * (contar + 1), 160)
        self.compras_disponibles = QLabel("Tus compras disponibles son: ", self)
        self.compras_disponibles.move(PIX * (contar + 1), 190)
        self.mejora_a = QPushButton("Mejora Ataque $" + str(p.C_ATAQUE), self)
        self.mejora_a.move(PIX * (contar + 1), 210)
        self.mejora_r = QPushButton("Mejora Rango $" + str(p.C_ALCANCE), self)
        self.mejora_r.move(PIX * (contar + 1), 240)
        self.comprar_r = QPushButton("Torre Racimo $" + str(p.C_TORRES), self)
        self.comprar_r.move(PIX * (contar + 1), 270)
        self.comprar_f = QPushButton("Torre Francotirador $" + str(p.C_TORRES),
                                     self)
        self.comprar_f.move(PIX * (contar + 1), 300)
        self.otra_ronda = QPushButton("Comenzar Ronda", self)
        self.otra_ronda.move(PIX * (contar + 1), 330)
        self.cerrar_sesion = QPushButton("Cerrar Sesión", self)
        self.cerrar_sesion.move(PIX * (contar + 1), 360)
        self.label_pausa = QLabel('                               ', self)
        self.label_pausa.move(PIX * (contar + 1), 390)
        self.pausado = False
        self.otra_ronda.clicked.connect(self.comenzar)
        self.cerrar_sesion.clicked.connect(self.cerrar)
        self.comprar_f.clicked.connect(self.franco)
        self.comprar_r.clicked.connect(self.racimo)
        self.mejora_r.clicked.connect(self.mejora_rango)
        self.mejora_a.clicked.connect(self.mejora_ataque)
        self.empezar = False
        self.dropbox1 = DropBox(self)
        self.dropbox1.setGeometry(PIX * (len(self.mapa[0][0])) + 3, 300,
                                  PIX, PIX)
        self.dropbox2 = DropBox(self)
        self.dropbox2.setGeometry(PIX * (len(self.mapa[0][0])) + 3, 270, PIX,
                                  PIX)

    def comenzar(self):
        self.empezar = True
        self.niña = Personaje(self.inicios[0][0], self.inicios[0][1],
                              self.largo, self.ancho, self.bloqueados)
        self.threads.append(self.niña)
        self.trigger_mover_entidad.connect(self.niña.move)
        self.imagen_niña = QLabel('', self)
        self.imagen_niña.setGeometry(self.niña.x, self.niña.y, p.ANCHO_P,
                                     p.LARGO_P)
        self.imagen_niña.setPixmap(
            QPixmap(path.join("sprites", "personaje", "f", "f_01.png")))
        self.current_pix = 0
        self.imagen_niña.show()
        self.mejora_a.setEnabled(False)
        self.mejora_r.setEnabled(False)
        self.comprar_r.setEnabled(False)
        self.comprar_f.setEnabled(False)
        self.otra_ronda.setEnabled(False)
        self.crear_enemigos()
        # self.crear_monedas()

    def crear_enemigos(self):
        contador = 1
        for i in range(self.cant):
            imagen_enemigo = QLabel('', self)
            bloqueados = self.bloqueados_e
            if i == 0 or i % 4 == 0:
                imagen_enemigo.setPixmap(
                    QPixmap(path.join("sprites", self.enemigo, "kamikaze",
                                      "kamikaze_01.png")))
                self.nuevo = EnemigoKamikaze(self.enemigo, self.inicios[
                    contador % (len(self.inicios))], imagen_enemigo, bloqueados)
            else:
                imagen_enemigo.setPixmap(
                    QPixmap(path.join("sprites", self.enemigo, "normal",
                                      "normal_01.png")))
                self.nuevo = EnemigoNormal(self.enemigo, self.inicios[
                    contador % (len(self.inicios))], imagen_enemigo, bloqueados)
            imagen_enemigo.setGeometry(self.nuevo.x, self.nuevo.y, p.ANCHO_P,
                                       p.LARGO_P)
            imagen_enemigo.show()
            self.threads.append(self.nuevo)
            contador += 1

    def crear_monedas(self):
        self.imagen = QLabel('', self)
        self.imagen.setPixmap(QPixmap(path.join("sprites", "mapas",
                                                "towerDefense_tile272")))
        while True:
            mapa = self.mapa[0]
            a = True
            while a == True:
                linea = randint(1, len(mapa) - 2)
                i = randint(1, len(mapa[0]) - 2)
                if mapa[linea - 1][i] == 'C' or mapa[linea + 1][i] == 'C' or \
                        mapa[linea][i - 1] == 'C' or mapa[linea][i + 1] == 'C':
                    self.coin = Moneda(linea, i)
                    self.imagen.setGeometry(self.coin.x, self.coin.y, p.ANCHO_P,
                                            p.LARGO_P)
                    self.imagen.show()
                    self.threads.append(self.coin)

    def mejora_ataque(self):
        if self.monedas >= p.C_ATAQUE and len(self.torres) > 0:
            a = self.torres[0].ataque
            for i in range(len(self.torres)):
                torre = self.torres[i]
                torre.mejora_ataque()
            if a != self.torres[0].ataque:
                self.monedas -= p.C_ATAQUE
                self.l_monedas.setText("Monedas Totales: " + str(self.monedas))

    def mejora_rango(self):
        if self.monedas >= p.C_ALCANCE and len(self.torres) > 0:
            a = self.torres[0].radio
            for i in range(len(self.torres)):
                torre = self.torres[i]
                torre.mejora_alcance()
            if a != self.torres[0].radio:
                self.monedas -= p.C_ALCANCE
                self.l_monedas.setText("Monedas Totales: " + str(self.monedas))

    def franco(self):
        if self.monedas >= p.C_TORRES:
            self.imagen1 = DraggableLabel(self.dropbox1)
            self.imagen1.setGeometry(0, 0, PIX, PIX)
            pix = QPixmap(
                path.join("sprites", "mapa", "towerDefense_tile250.png"))
            pix = pix.scaled(PIX, PIX)
            self.imagen1.setPixmap(pix)
            self.imagen1.show()
            self.torre = Francotirador()
            self.monedas -= p.C_TORRES
            self.l_monedas.setText("Monedas Totales: " + str(self.monedas))
            self.torres.append(self.torre)

    def racimo(self):
        if self.monedas >= p.C_TORRES:
            self.imagen2 = DraggableLabel(self.dropbox2)
            self.imagen2.setGeometry(0, 0, PIX, PIX)
            pix = QPixmap(
                path.join("sprites", "mapa", "towerDefense_tile249.png"))
            pix = pix.scaled(PIX, PIX)
            self.imagen2.setPixmap(pix)
            self.imagen2.show()
            self.torre = Racimo()
            self.monedas -= p.C_TORRES
            self.l_monedas.setText("Monedas Totales: " + str(self.monedas))
            self.torres.append(self.torre)

    def cheat_end(self):
        pass

    def cheat_mon(self):
        pass

    def QKeySequence(self):
        if (Qt.Key_E + Qt.Key_N + Qt.Key_D):
            self.cheat_end()

    def keyPressEvent(self, e):
        if self.empezar == True:
            path1 = path.join("sprites", "personaje", "f", "f_0{}.png")
            if e.key() == Qt.Key_D:
                self.current_pix += 1
                if self.current_pix > 9:
                    self.current_pix = 7
                self.imagen_niña.setPixmap(
                    QPixmap(path1.format(self.current_pix)).transformed(
                        QTransform().scale(-1, 1)))
                self.trigger_mover_entidad.emit(MoverEntidad("right"))
            elif e.key() == Qt.Key_A:
                self.current_pix += 1
                if self.current_pix > 9:
                    self.current_pix = 7
                self.imagen_niña.setPixmap(
                    QPixmap(path1.format(self.current_pix)))
                self.trigger_mover_entidad.emit(MoverEntidad("left"))
            elif e.key() == Qt.Key_S:
                self.current_pix += 1
                if self.current_pix > 3:
                    self.current_pix = 1
                self.imagen_niña.setPixmap(
                    QPixmap(path1.format(self.current_pix)))
                self.trigger_mover_entidad.emit(MoverEntidad("Down"))
            elif e.key() == Qt.Key_W:
                self.current_pix += 1
                if self.current_pix > 6:
                    self.current_pix = 4
                self.imagen_niña.setPixmap(
                    QPixmap(path1.format(self.current_pix)))
                self.trigger_mover_entidad.emit(MoverEntidad("Up"))
            elif e.key() == Qt.Key_P:
                if self.pausado == False:
                    for i in range(len(self.threads)):
                        self.threads[i].pausa()
                    self.label_pausa.setText('Juego Pausado')
                    self.pausado = True
                elif self.pausado == True:
                    for i in range(len(self.threads)):
                        self.threads[i].pausa()
                    self.label_pausa.setText('')
                    self.pausado = False
            elif e.key() == Qt.Key_E:
                self.cheat_end()
            elif e.key() == Qt.Key_N:
                self.cheat_end()
                self.cheat_mon()
            elif e.key() == Qt.Key_D:
                self.cheat_end()
            elif e.key() == Qt.Key_M:
                self.cheat_mon()
            elif e.key() == Qt.Key_O:
                self.cheat_mon()

    def keyReleaseEvent(self, e):
        if self.empezar == True:
            path1 = path.join("sprites", "personaje", "f", "f_01.png")
            if e.key() == Qt.Key_D:
                self.imagen_niña.setPixmap(QPixmap(path1))
                self.imagen_niña.move(self.niña.x, self.niña.y)
            elif e.key() == Qt.Key_A:
                self.imagen_niña.setPixmap(QPixmap(path1))
                self.imagen_niña.move(self.niña.x, self.niña.y)
            elif e.key() == Qt.Key_S:
                self.imagen_niña.setPixmap(QPixmap(path1))
                self.imagen_niña.move(self.niña.x, self.niña.y)
            elif e.key() == Qt.Key_W:
                self.imagen_niña.setPixmap(QPixmap(path1))
                self.imagen_niña.move(self.niña.x, self.niña.y)

    def mover_entidad(self, event):
        self.imagen_niña.move(event.x, event.y)

    def cerrar(self):
        self.fin = Resultado(self.principal, self, self.n_ronda, self.monedas)
        self.fin.show()
        self.close()
