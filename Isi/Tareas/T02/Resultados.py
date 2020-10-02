from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QGridLayout


class Resultado(QWidget):
    def __init__(self, principal, juego, rondas, monedas):
        super().__init__()
        self.juego = juego
        self.principal = principal
        self.rondas = rondas
        self.monedas = monedas
        self.init_GUI()

    def init_GUI(self):
        self.setWindowTitle("DCCivil War Resultados")
        self.setGeometry(200, 200, 300, 200)
        self.info_monedas = QLabel("Monedas Obtenidas: " + str(self.monedas),
                                   self)
        self.rondas_alcanzadas = QLabel(
            "Rondas Alcanzadas: " + str(self.rondas), self)
        self.volver_menu = QPushButton("Volver al Menú", self)
        self.b_salir = QPushButton("Salir", self)
        self.resultados = QLabel("Resultados", self)
        self.espacio = QLabel(" ", self)
        self.grilla = QGridLayout()
        self.grilla.addWidget(self.resultados, 1, 1)
        self.grilla.addWidget(self.info_monedas, 2, 1)
        self.grilla.addWidget(self.rondas_alcanzadas, 3, 1)
        self.grilla.addWidget(self.volver_menu, 5, 1)
        self.grilla.addWidget(self.b_salir, 5, 2)
        self.grilla.addWidget(self.espacio, 5, 3)
        self.grilla.addWidget(self.espacio, 6, 0)
        self.grilla.addWidget(self.espacio, 0, 0)
        self.setLayout(self.grilla)
        self.volver_menu.clicked.connect(self.volver)
        self.b_salir.clicked.connect(self.salir)

    def volver(self):
        self.hide()

    def salir(self):
        self.close()
        self.juego.close()
        self.principal.close()
