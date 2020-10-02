import json
import socket
import sys
import threading as th
from time import sleep

from Eventos import Enviar, Imagen
from FrontEnd import VentanaIngresoUsuario
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QGraphicsObject

from pixel_collector import get_pixels

with open('parametros.json', 'r') as file:
    parametros = json.load(file)


class Cliente(QGraphicsObject):
    texto_sig = pyqtSignal(Enviar)
    manejar_b1 = pyqtSignal()
    actualizar_sig = pyqtSignal(Enviar)
    invalido_sig = pyqtSignal()
    crear_salas = pyqtSignal(Enviar)
    salas_iniciales = pyqtSignal(Enviar)
    entrar_sala = pyqtSignal(Enviar)
    chat = pyqtSignal(Enviar)
    cerrar_juego = pyqtSignal(Enviar)
    comenzar = pyqtSignal()
    cargar_imagen = pyqtSignal(Enviar)
    imagen = pyqtSignal(Imagen)
    actualizar_lista = pyqtSignal(Enviar)

    def __init__(self):
        super().__init__()

        self.parametros = parametros
        self.host = self.parametros['host']
        self.port = self.parametros['port']
        print("Inicializando cliente...")
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.texto_sig.connect(self.recibir_signal)
        self.ventana = VentanaIngresoUsuario(self.texto_sig, self.imagen)
        self.crear_salas.connect(self.ventana.ventana_salas.crear_sala)
        self.manejar_b1.connect(self.ventana.manejo_boton)
        self.invalido_sig.connect(self.ventana.invalido)
        self.salas_iniciales.connect(self.ventana.ventana_salas.salas_iniciales)
        self.entrar_sala.connect(self.ventana.ventana_salas.entrar_sala)
        self.cerrar_juego.connect(self.ventana.ventana_salas.salir_sala)
        self.cargar_imagen.connect(self.ventana.ventana_salas.mostrar_imagen)
        self.imagen.connect(self.recibir_imagen)
        self.actualizar_lista.connect(
            self.ventana.ventana_salas.actualizar_lista)
        self.ventana.show()

        try:
            self.socket_cliente.connect((self.host, self.port))
            print("Cliente conectado exitosamente al servidor")
            self.conectado = True
            print("Escuchando al servidor...")
            escuchar_servidor = th.Thread(target=self.escuchar, daemon=True)
            escuchar_servidor.start()
            user = self.manejar_b1.emit()
            if user != None:
                self.send(user)
        except ConnectionRefusedError:
            self.terminar_conexion()

    def recibir_signal(self, mensaje):
        para_enviar = mensaje.texto
        self.send(para_enviar)

    def recibir_imagen(self, imagen):
        path = imagen.path['data']['imagen']
        print(path)
        matriz = get_pixels(path)
        self.send({'status': 'cargar imagen', 'data': {'matriz': matriz,
                                                       'usuario':
                                                           imagen.path['data'][
                                                               'usuario']}})

    def escuchar(self):
        while self.conectado:
            try:
                tamano_mensaje_bytes = self.socket_cliente.recv(4)
                tamano_mensaje = int.from_bytes(tamano_mensaje_bytes,
                                                byteorder="big")
                contenido_mensaje_bytes = bytearray()
                while len(contenido_mensaje_bytes) < tamano_mensaje:
                    contenido_mensaje_bytes += self.socket_cliente.recv(256)
                contenido_mensaje = contenido_mensaje_bytes.decode("utf-8")
                mensaje_decodificado = json.loads(contenido_mensaje)
                self.manejar_comando(mensaje_decodificado)
            except ConnectionResetError:
                self.terminar_conexion()

    def manejar_comando(self, dic):
        print(f"Mensaje recibido: {dic}")
        if dic['status'] == 'usuarios' and dic['data'] != 'invalido':
            self.ventana.cerrar()
        elif dic['status'] == 'usuarios' and dic['data'] == 'invalido':
            self.invalido_sig.emit()
        elif dic["status"] == "mensaje":
            data = dic["data"]
            usuario = data["usuario"]
            contenido = data["contenido"]
            print('emit')
            self.actualizar_sig.emit(Enviar(usuario + ': ' + contenido))
        elif dic['status'] == 'cerrar':
            self.terminar_conexion()
        elif dic['status'] == 'crear_sala':
            que_enviar = dic['data']
            self.crear_salas.emit(Enviar(que_enviar))
        elif dic['status'] == 'chat':
            self.actualizar_sig.connect(
                self.ventana.ventana_salas.juego.actualizar_chat)
        elif dic['status'] == 'comenzar':
            usuario = dic['data']
            self.comenzar.connect(self.ventana.ventana_salas.juego.comenzar)
            self.comenzar.emit()
            self.actualizar_sig.emit(Enviar(usuario + ': cinco'))
            sleep(1)
            self.actualizar_sig.emit(Enviar(usuario + ': cuatro'))
            sleep(1)
            self.actualizar_sig.emit(Enviar(usuario + ': tres'))
            sleep(1)
            self.actualizar_sig.emit(Enviar(usuario + ': dos'))
            sleep(1)
            self.actualizar_sig.emit(Enviar(usuario + ': uno'))
            sleep(1)
            self.actualizar_sig.emit(Enviar(usuario + ': cero'))
        elif dic['status'] == 'lista salas':
            self.salas_iniciales.emit(Enviar(dic['data']))
        elif dic['status'] == 'entrar':
            self.entrar_sala.emit(Enviar(dic['data']))
        elif dic['status'] == 'imagen':
            enviar = dic['data']['matriz']
            self.cargar_imagen.emit(Enviar(enviar))
        elif dic['status'] == 'filtro':
            self.cargar_imagen.emit(Enviar(dic['data']))
        elif dic['status'] == 'cerrar_sala':
            self.cerrar_juego.emit(Enviar(dic['data']))
        elif dic['status'] == 'actualizar':
            self.actualizar_lista.emit(Enviar(dic['data']))

    def send(self, mensaje):
        print(mensaje)
        mensaje_codificado = json.dumps(mensaje)
        contenido_mensaje_bytes = mensaje_codificado.encode("utf-8")
        tamano_bytes = len(contenido_mensaje_bytes).to_bytes(4, byteorder="big")
        print(tamano_bytes + contenido_mensaje_bytes)
        self.socket_cliente.send(tamano_bytes + contenido_mensaje_bytes)

    def terminar_conexion(self):
        print("Conexión terminada")
        self.connected = False
        self.socket_cliente.close()
        exit()


if __name__ == "__main__":
    app = QApplication([])
    cliente = Cliente()
    sys.exit(app.exec_())
