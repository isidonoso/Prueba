from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, \
    QLineEdit, QRadioButton, QVBoxLayout, QHBoxLayout

from GuiJuego import Juego
from Mapas import ranking


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.init_GUI()
        self.usuario = ''

    def init_GUI(self):
        self.setWindowTitle("DCCivil War")
        self.setGeometry(100, 100, 300, 400)
        self.etiqueta = QLabel("Nombre Jugador: ", self)
        self.nombre = QLineEdit("", self)
        self.status1 = QLabel('Status: No has iniciado sesion', self)
        self.etiqueta1 = QLabel("Elige un equipo: ", self)
        self.pinguino = QRadioButton("Pinguinos", self)
        self.pinguino.toggled.connect(self.onClickedP)
        self.gatos = QRadioButton("Gatos", self)
        self.gatos.toggled.connect(self.onClickedG)
        self.b_empezar = QPushButton('Empezar', self)
        self.b_nombre = QPushButton('Iniciar Sesión')
        self.status2 = QLabel('Status: No has escogido equipo', self)
        self.status3 = QLabel('', self)
        self.ranking = QLabel('Ranking 10 mejores puntajes:', self)
        self.r1 = QLabel("1. " + ranking[0][1] + " " + ranking[0][0], self)
        self.r2 = QLabel("2. " + ranking[1][1] + " " + ranking[1][0], self)
        self.r3 = QLabel("3. " + ranking[2][1] + " " + ranking[2][0], self)
        self.r4 = QLabel("4. " + ranking[3][1] + " " + ranking[3][0], self)
        self.r5 = QLabel("5. " + ranking[4][1] + " " + ranking[4][0], self)
        self.r6 = QLabel("6. " + ranking[5][1] + " " + ranking[5][0], self)
        self.r7 = QLabel("7. " + ranking[6][1] + " " + ranking[6][0], self)
        self.r8 = QLabel("8. " + ranking[7][1] + " " + ranking[7][0], self)
        self.r9 = QLabel("9. " + ranking[8][1] + " " + ranking[8][0], self)
        self.r10 = QLabel("10. " + ranking[9][1] + " " + ranking[9][0], self)
        r16 = QHBoxLayout()
        r16.addWidget(self.r1)
        r16.addWidget(self.r6)
        r27 = QHBoxLayout()
        r27.addWidget(self.r2)
        r27.addWidget(self.r7)
        r38 = QHBoxLayout()
        r38.addWidget(self.r3)
        r38.addWidget(self.r8)
        r49 = QHBoxLayout()
        r49.addWidget(self.r4)
        r49.addWidget(self.r9)
        r51 = QHBoxLayout()
        r51.addWidget(self.r5)
        r51.addWidget(self.r10)
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.etiqueta)
        hbox.addWidget(self.nombre)
        hbox.addWidget(self.b_nombre)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        vbox.addWidget(self.status1)
        vbox.addStretch(1)
        vbox.addWidget(self.etiqueta1)
        vbox.addWidget(self.pinguino)
        vbox.addWidget(self.gatos)
        vbox.addStretch(1)
        vbox.addWidget(self.status2)
        vbox.addStretch(1)
        vbox.addWidget(self.b_empezar)
        vbox.addStretch(1)
        vbox.addWidget(self.status3)
        vbox.addStretch(1)
        vbox.addWidget(self.ranking)
        vbox.addLayout(r16)
        vbox.addLayout(r27)
        vbox.addLayout(r38)
        vbox.addLayout(r49)
        vbox.addLayout(r51)
        vbox.addStretch(2)
        self.setLayout(vbox)
        self.b_empezar.clicked.connect(self.empezar)
        self.b_nombre.clicked.connect(self.nombre_usuario)

    def nombre_usuario(self):
        self.usuario = self.nombre.text()
        if self.nombre.text() == '':
            pass
        else:
            self.status1.setText(
                'Status: ' + self.nombre.text() + ' has iniciado sesión')

    def onClickedP(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.enemigos = "gato"
            self.equipo = "pinguino"
            self.status2.setText(
                'Status: Elegiste el equipo de Pinguinos')

    def onClickedG(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.enemigos = "pinguino"
            self.equipo = "gato"
            self.status2.setText(
                'Status: Elegiste el equipo de Gatos')

    def empezar(self):
        if self.status1.text() == 'Status: No has iniciado sesion' or self.status2.text() == 'Status: No has escogido equipo':
            self.status3.setText(
                'Aun no ha ingresado todos los datos necesarios')
        else:
            self.start()

    def start(self):
        self.nombre.setText((''))
        self.juego = Juego(self, self.enemigos, self.equipo, self.usuario)
        self.juego.show()


if __name__ == '__main__':
    app = QApplication([])
    inicio = Menu()
    inicio.show()
    app.exec_()
### atribute error
