from time import sleep
from Imagenes import GuardarImagen
from Eventos import Enviar, Imagen
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, \
    QVBoxLayout, QPushButton, QScrollArea, QListWidget, QDialog, QFileDialog
from time import sleep

from Eventos import Enviar, Imagen
from Imagenes import GuardarImagen
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, \
    QVBoxLayout, QPushButton, QScrollArea, QListWidget, QDialog, QFileDialog


class VentanaIngresoUsuario(QWidget):

    def __init__(self, signal, signal_imagen, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nombre_usuario = ""
        self.signal = signal
        self.signal_imagen = signal_imagen
        self.setWindowTitle("Timbiriche 99")
        self.setGeometry(100, 100, 800, 600)
        self.ventana_salas = VentanaSalas(self.signal, self.signal_imagen)
        self.ventana_salas.boton_cargar_foto.setEnabled(False)
        self.ventana_salas.boton_crear_sala.setEnabled(False)
        self.ventana_salas.boton_filtro.setEnabled(False)
        self.ventana_salas.boton_salir.setEnabled(False)
        self.ventana_salas.show()

        self.label_titulo = QLabel("Timbiriche 99", self)
        label_titulo_font = self.label_titulo.font()
        label_titulo_font.setPointSize(48)
        self.label_titulo.setFont(label_titulo_font)
        self.label_estado = QLabel('                                 ', self)
        self.label_usuario = QLabel("Usuario: ", self)
        label_usuario_font = self.label_usuario.font()
        label_usuario_font.setPointSize(12)
        self.label_usuario.setFont(label_usuario_font)
        self.user = QLineEdit("", self)
        user_font = self.user.font()
        user_font.setPointSize(10)
        self.boton_usuario = QPushButton("\t\tIngresar\t\t", self)
        boton_usuario_font = self.boton_usuario.font()
        boton_usuario_font.setPointSize(12)
        self.boton_usuario.clicked.connect(self.manejo_boton)
        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(self.label_usuario)
        hbox.addWidget(self.user)
        hbox.addStretch(2)
        hbox1 = QHBoxLayout()
        hbox1.addStretch(2)
        hbox1.addWidget(self.boton_usuario)
        hbox1.addStretch(2)
        hbox2 = QHBoxLayout()
        hbox2.addStretch(2)
        hbox2.addWidget(self.label_estado)
        hbox2.addStretch(2)
        title_hbox = QHBoxLayout()
        title_hbox.addStretch(1)
        title_hbox.addWidget(self.label_titulo)
        title_hbox.addStretch(1)
        vbox = QVBoxLayout()
        vbox.addLayout(title_hbox)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addStretch(3)

        self.setLayout(vbox)

    def invalido(self):
        self.label_estado.setText('El nombre de usuario esta ocupado')

    def manejo_boton(self):
        if len(self.user.text()) != 0:
            self.nombre_usuario = self.user.text()
            self.ventana_salas.nombre_usuario = self.nombre_usuario
            self.signal.emit(Enviar(
                {'status': "nuevo_usuario", "data": self.nombre_usuario}))

    def cerrar(self):
        self.ventana_salas.boton_cargar_foto.setEnabled(True)
        self.ventana_salas.boton_crear_sala.setEnabled(True)
        self.ventana_salas.boton_salir.setEnabled(True)
        self.ventana_salas.boton_filtro.setEnabled(True)
        self.ventana_salas.actualizar_usuario(self.nombre_usuario)
        self.close()


class VentanaSalas(QDialog):
    def __init__(self, signal, signal_imagen):
        super().__init__()
        self.nombre_usuario = ''
        self.signal = signal
        self.signal_imagen = signal_imagen
        self.setWindowTitle("Salas")
        self.setGeometry(100, 100, 800, 600)
        self.lista_salas = QListWidget()
        self.contador = 0
        self.nombres_salas = []
        self.perfil = QLabel("", self)
        self.label_usuario = QLabel("Usuario:                         ", self)
        self.salas_log_label = QLabel("", self)
        salas_log_label_font = self.salas_log_label.font()
        salas_log_label_font.setPointSize(12)
        self.boton_crear_sala = QPushButton("\t\tCrear Sala\t\t", self)
        self.boton_cargar_foto = QPushButton("\t\tCargar Foto\t\t", self)
        self.boton_filtro = QPushButton("\t\tFiltro Dibujo\t\t", self)
        self.boton_salir = QPushButton("\t\tSalir\t\t", self)
        self.boton_crear_sala.clicked.connect(self.signal_sala)
        self.boton_cargar_foto.clicked.connect(self.cargar)
        self.boton_filtro.clicked.connect(self.aplicar_filtro)
        self.boton_salir.clicked.connect(self.salir)
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.addWidget(QLabel(' ', self))
        vbox.addWidget(self.lista_salas)
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        self.setLayout(hbox)
        self.label_usuario.move(10, 100)
        self.boton_crear_sala.move(10, 450)
        self.boton_cargar_foto.move(10, 400)
        self.boton_filtro.move(120, 400)
        self.boton_salir.move(10, 500)
        self.lista_salas.clicked.connect(self.ingresar_sala)

    def signal_sala(self):
        self.signal.emit(Enviar(
            {'status': "crear_sala", 'data': self.nombre_usuario}))

    def salas_iniciales(self, string):
        lis = string.texto.split(" ")
        imprimir = f"{lis[1]} Participantes: {lis[2]} 'Jefe {lis[0]}'"
        self.nombres_salas.append(lis[1])
        self.lista_salas.insertItem(self.contador, imprimir)
        self.contador += 1

    def crear_sala(self, string):
        sleep(0.1)
        string = string.texto
        lista = string.split(' ')
        texto = f"Sala_{lista[1]} Participantes: {lista[2]} Jefe '{lista[0]}'"
        self.lista_salas.insertItem(self.contador, texto)
        self.nombres_salas.append(f"Sala_{lista[1]}")
        self.contador += 1
        if lista[0] == self.nombre_usuario:
            self.juego = Juego('Sala_' + lista[1], lista[0],
                               self.nombre_usuario, self.signal)
            self.juego.show()
            self.signal.emit(
                Enviar({'status': 'chat', 'data': self.nombre_usuario}))

    def salir_sala(self, string):
        string = string.texto
        lista = string.split(' ')
        numero = lista[1].split('_')
        texto = f"Sala_{lista[1]} Participantes: {lista[2]} Jefe '{lista[0]}'"
        self.lista_salas.insertItem(int(numero[1]) - 1, texto)

    def ingresar_sala(self):
        sala = self.lista_salas.currentRow()
        print('a')
        print('a')
        print((self.nombres_salas[sala]))
        self.signal.emit(
            Enviar({'status': 'entrar', 'usuario': self.nombre_usuario,
                    'sala': self.nombres_salas[sala]}))

    def entrar_sala(self, texto):
        lista = texto.texto.split(' ')
        self.juego = Juego(lista[1], lista[0], self.nombre_usuario, self.signal)
        self.juego.show()
        numero = lista[1].split('_')
        texto = f"{lista[1]} Participantes: {lista[2]} Jefe '{lista[0]}'"
        self.lista_salas.takeItem(int(numero[1]) - 1)
        self.lista_salas.insertItem(int(numero[1]) - 1, texto)
        self.signal.emit(
            Enviar({'status': 'chat', 'data': self.nombre_usuario}))

    def actualizar_lista(self,texto):
        lista=texto.texto.split(' ')
        numero=lista[1].split('_')
        self.lista_salas.takeItem(int(numero[1])-1)
        texto=f"{lista[1]} Participantes: {lista[2]} Jefe: {lista[0]}"
        self.lista_salas.insertItem(int(numero[1])-1,texto)

    def eliminar_sala(self, nombre):
        for i in range(len(self.nombres_salas)):
            if self.nombres_salas[i][0] == nombre:
                self.lista_salas.takeItem(i)
                self.nombres_salas.pop(i)

    def cargar(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        path = QFileDialog.getOpenFileName(self,
                                           "QFileDialog.getOpenFileName()",
                                           "", "PNG Files (*.png)",
                                           options=options)
        self.signal_imagen.emit(Imagen(
            {'status': 'cargar imagen', 'data': {'usuario': self.nombre_usuario,
                                                 'imagen': path[0]}}))

    def mostrar_imagen(self,matriz):
        imagen=GuardarImagen(matriz.texto,self.nombre_usuario)
        pixmap = QPixmap(self.nombre_usuario+'.png')
        self.perfil.setGeometry(10, 150, 200, 200)
        pixmap = pixmap.scaled(200, 200)
        self.perfil.setPixmap(pixmap)

    def aplicar_filtro(self):
        self.signal.emit(Enviar({'status':'filtro','data':self.nombre_usuario}))

    def actualizar_usuario(self, texto):
        self.label_usuario.setText('Usuario: ' + str(texto) + ' ')

    def salir(self):
        self.signal.emit(Enviar(
            {'status': "cerrar", 'data': self.nombre_usuario}))
        self.close()


class Juego(QWidget):
    def __init__(self, nombre, jefe, usuario, signal):
        super().__init__()
        self.jefe = jefe
        self.nombre_usuario = usuario
        self.signal = signal
        self.nombre = nombre
        self.setWindowTitle("Timbiriche 99")
        self.setGeometry(100, 100, 800, 600)
        self.label_usuario = QLabel(self.nombre_usuario, self)
        self.label_jefe = QLabel("Jefe: " + self.jefe, self)
        label_usuario_font = self.label_usuario.font()
        label_usuario_font.setPointSize(10)
        self.label_usuario.setFont(label_usuario_font)
        label_jefe_font = self.label_jefe.font()
        label_jefe_font.setPointSize(10)
        self.label_jefe.setFont(label_jefe_font)
        self.chat_log = ""
        self.label_titulo = QLabel("Timbiriche 99", self)
        label_titulo_font = self.label_titulo.font()
        label_titulo_font.setPointSize(35)
        self.label_titulo.setFont(label_titulo_font)
        self.chat_log_label = QLabel("", self)
        chat_log_label_font = self.chat_log_label.font()
        chat_log_label_font.setPointSize(12)
        self.users_scroll = QScrollArea(self)
        self.users_scroll.setWidgetResizable(True)
        self.users_scroll.setStyleSheet("background-color: transparent")
        self.user = QLineEdit("", self)
        user_font = self.user.font()
        user_font.setPointSize(12)
        self.user.setFont(user_font)
        self.boton_usuario = QPushButton("\t\tEnviar\t\t", self)
        self.boton_usuario.clicked.connect(self.manejo_boton)
        self.boton_salir = QPushButton("\t\tSalir\t\t", self)
        self.boton_salir.clicked.connect(self.salir)
        self.boton_comenzar = QPushButton("\t\tComenzar\t\t", self)
        self.boton_comenzar.move(315,250)
        self.boton_comenzar.clicked.connect(self.comenzar_juego)
        self.label_titulo.setGeometry(10, 0, 1000, 50)
        self.chat_log_label.setGeometry(10, 80, 300, 300)
        self.label_usuario.move(400, 100)
        self.label_jefe.move(400, 80)
        self.users_scroll.setWidget(self.chat_log_label)
        self.users_scroll.setGeometry(10, 80, 300, 300)
        self.chat_log_label.setAlignment(Qt.AlignTop)
        self.user.setGeometry(10, 400, 300, 50)
        self.user.setFocus()
        self.boton_usuario.setGeometry(315, 400, 80, 50)
        self.boton_salir.setGeometry(315, 80, 80, 50)
        if self.jefe != self.nombre_usuario:
            self.boton_comenzar.setEnabled(False)

    def manejo_boton(self):
        self.signal.emit(Enviar({'status': "mensaje",
                                 "data": {"usuario": self.nombre_usuario,
                                          "contenido": self.user.text(),
                                          "sala": self.nombre}}))
        self.user.setText("")

    def comenzar_juego(self):
        self.signal.emit(
            Enviar({'status': 'comenzar', 'data': self.nombre_usuario}))

    def comenzar(self):
        self.label_cuenta_regresiva = QLabel("5", self)
        label_cuenta_font = self.label_cuenta_regresiva.font()
        label_cuenta_font.setPointSize(20)
        self.label_cuenta_regresiva.setFont(label_cuenta_font)
        self.label_cuenta_regresiva.move(500, 10)
        sleep(1)
        self.label_cuenta_regresiva.setText('4')
        sleep(1)
        self.label_cuenta_regresiva.setText('3')
        sleep(1)
        self.label_cuenta_regresiva.setText('2')
        sleep(1)
        self.label_cuenta_regresiva.setText('1')
        sleep(1)
        self.label_cuenta_regresiva.setText('0')

    def actualizar_chat(self, mensaje):
        self.chat_log += f"{mensaje.texto}\n"
        print('holadas')
        self.chat_log_label.setText(self.chat_log)

    def salir(self):
        self.signal.emit(
            Enviar({'status': "cerrar_juego", 'sala': self.nombre,
                    'usuario': self.nombre_usuario}))
        self.close()
