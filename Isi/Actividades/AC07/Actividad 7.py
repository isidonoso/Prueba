from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, \
    QLineEdit, QGridLayout
import sys
import jugador
from PyQt5.QtCore import (QObject, pyqtSignal)
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel)

### Este codigo esta basado en la ayudantía 10 del semestre 2018-01

class Menu(QWidget):
    def __init__(self):
        """
        Preparamos la interfaz gráfica del login
        """
        super().__init__()
        self.init_gui()

    def init_gui(self):
        """
        Agregamos los componentes necesarios con algunas conecciones
        """
        self.setWindowTitle("Programadicto")
        self.setGeometry(200, 200, 300, 100)

        self.label1 = QLabel("Nombre Jugador 1", self)
        self.label2 = QLabel("Nombre Jugador 2", self)
        self.input1 = QLineEdit('', self)
        self.input2 = QLineEdit("", self)
        self.button1 = QPushButton('Empezar', self)
        self.grilla = QGridLayout()  # creamos la grilla

        self.grilla.addWidget(self.input1, 0,
                              1)  # le añadimos los componentes a la grilla
        self.grilla.addWidget(self.input2, 1, 1)
        self.grilla.addWidget(self.label1, 0, 0)
        self.grilla.addWidget(self.label2, 1, 0)
        self.grilla.addWidget(self.button1, 2, 0)

        self.setLayout(self.grilla)  # setiamos la grilla

        self.button1.clicked.connect(self.set_name)
        self.jugador1= Jugador(self.input1)
        self.jugador2 = Jugador(self.input2)

    def set_name(self):
        boton = self.sender()  # esto nos retorna el boton al que le hicieron click
        boton.disconnect()  # desconectamos el button3 para que no se pueda ingresar nombre de nuevo
        self.button1.clicked.connect(
            self.start)  # ahora si podemos conectar el button1 a la funcion start

    def start(self):
        self.screen = Screen()  # Creamos el widget screen
        self.hide()  # Escondemos el widget Menu
        self.screen.show()  # Y mostramos el widget screen

    def close(self):
        exit()

class Jugador(QObject):
    def __init__(self,nombre):
        self.nombre=nombre

class Screen(QWidget):
    trigger = pyqtSignal()

    def __init__(self, *args, **kwargs):
        """
        Preparamos la interfaz gráfica
        """
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        """
        Hacemos todos los ajustes necesarios para conectar la interfaz
        """
        menu = Menu()
        self.setGeometry(200, 100, 800, 600)
        self.setWindowTitle('Mario Bros')

        self.imagen_jugador1 = QLabel(self)
        self.pixmap1 = QPixmap("/cartas/jugador_1.png")
        self.imagen_jugador1.setGeometry(300, 50, 100, 50)
        self.imagen_jugador1.setPixmap(
            self.pixmap1)  # asi setiamos una foto a un label

        self.imagen_jugador2 = QLabel(self)
        self.imagen_jugador1.setGeometry(500, 50, 100, 50)
        self.pixmap2 = QPixmap("/cartas/jugador_1.png")
        self.imagen_jugador2.setPixmap(
            self.pixmap2)  # asi setiamos una foto a un label

        self.boton_1 = QPushButton('Empezar', self)
        self.boton_2 = QPushButton('Reiniciar', self)
        contador=0
        self.label1 = QLabel("                   Cartas: "+str(contador))
        nombre=menu.jugador1.nombre
        nombre2=menu.jugador2.nombre
        self.grilla = QGridLayout()  # creamos la grilla

        self.grilla.addWidget(self.boton_1, 0, 1)
        self.grilla.addWidget(self.boton_2, 1, 1)
        self.grilla.addWidget(self.label1, 2, 1)
        self.grilla.addWidget(self.imagen_jugador1, 4, 0)
        self.grilla.addWidget(self.imagen_jugador2, 4, 2)

        self.setLayout(self.grilla)


if __name__ == '__main__':
    app = QApplication([])
    inicio = Menu()
    inicio.show()
    app.exec_()
