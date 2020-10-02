import json
import socket
import threading as th
from time import sleep
from pixel_collector import get_pixels

from Imagenes import GuardarImagen,FiltroDibujo
from Salas import Sala
from Usuarios import Leer, Usuario, Escribir

with open('parametros.json', 'r') as file:
    parametros = json.load(file)


class Servidor:

    def __init__(self):
        self.parametros = parametros
        self.host = self.parametros['host']
        self.port = self.parametros['port']
        self.contador_salas = 0
        self.salas = []

        users = Leer()
        self.usuarios = users.usuarios

        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        print(f"Servidor escuchando en {self.host}:{self.port}...")

        thread = th.Thread(target=self.aceptar_conexiones_thread, daemon=True)
        thread.start()
        self.sockets = {}
        print("Servidor aceptando conexiones...")

    def aceptar_conexiones_thread(self):

        while True:
            client_socket, _ = self.socket_servidor.accept()
            self.sockets[client_socket] = None
            print("Servidor conectado a un nuevo cliente...")

            listening_client_thread = th.Thread(
                target=self.escuchar_cliente_thread, args=(client_socket,),
                daemon=True)
            listening_client_thread.start()
            if len(self.sockets) == 5:
                break

    def escuchar_cliente_thread(self, client_socket):

        while True:
            try:
                response_bytes_length = client_socket.recv(4)
                response_length = int.from_bytes(response_bytes_length,
                                                 byteorder="big")
                print('qué pasa ahora?')
                response = bytearray()
                while len(response) < response_length:
                    response += client_socket.recv(4096)
                print('pase el while')
                response = response.decode()
                decoded = json.loads(response)
                print(decoded)
                self.manejar_comando(decoded, client_socket)
                print('envie')

            except ConnectionResetError:
                print('pasa por aqui?')
                break

    def manejar_comando(self, recibido, client_socket):
        print("Mensaje Recibido: {}".format(recibido))
        if recibido['status'] == "mensaje":
            mensaje = recibido['data']['contenido'].split(' ')
            if mensaje[0] == '/chao':
                for i in self.salas:
                    if i.nombre == recibido['data']['sala']:
                        chao = i.comando_chao(recibido['data']['usuario'])
                        if chao == True:
                            mandar = f"{i.jefe} {i.nombre} {(len(i.usuarios))}"
                            for skt in self.sockets.items():
                                if skt[1] == recibido['data']['usuario']:
                                    self.send({'status': 'cerrar_juego',
                                               'data': mandar}, skt[0])
            msj = {'status': "mensaje",
                   "data": {"usuario": self.sockets[client_socket],
                            "contenido": recibido["data"]["contenido"]}}
            for i in self.salas:
                print(i.nombre)
                print(recibido['data']['sala'])
                if i.nombre == recibido['data']['sala']:
                    print(i.nombre)
                    for j in self.sockets.items():
                        if j[1] in i.usuarios:
                            self.send(msj, j[0])

        elif recibido['status'] == 'cargar imagen':
            im = GuardarImagen(recibido['data']['matriz'],
                               recibido['data']['usuario'])
            for i in self.usuarios:
                if i.nombre == recibido['data']['usuario']:
                    i.path = recibido['data']['usuario'] + '.png'
                    print(i.path)
            self.send({'status': 'imagen', 'data': recibido['data']}, client_socket)

        elif recibido['status']=='filtro':
            im = FiltroDibujo(recibido['data']+'.png',recibido['data'])
            for i in self.usuarios:
                if i.nombre == recibido['data']:
                    i.path = recibido['data'] + '_filtro.png'
                    print(i.path)
            matriz=get_pixels(i.path)
            self.send({'status': 'filtro', 'data': matriz}, client_socket)

        elif recibido['status'] == "nuevo_usuario":
            if recibido['data'] not in self.sockets.values():
                self.sockets[client_socket] = recibido["data"]
                user = Usuario(recibido['data'], ' ', 'activo')
                self.usuarios.append(user)
                self.send({'status': 'usuarios', 'data': recibido['data']},
                          client_socket)
                for sala in range(len(self.salas)):
                    sleep(0.01)
                    self.send({'status': 'lista salas',
                               'data': self.salas[sala].jefe + ' ' + self.salas[
                                   sala].nombre + ' ' + str(
                                   len(self.salas[sala].usuarios))},
                              client_socket)
            else:
                for i in range(len(self.usuarios)):
                    if recibido['data'] == self.usuarios[i].nombre and \
                            self.usuarios[i].estado == 'inactivo':
                        self.usuarios[i].estado = 'activo'
                        for skt in self.sockets.keys():
                            self.send(
                                {'status': 'usuarios',
                                 'data': recibido['data']},
                                skt)
                    else:
                        for skt in self.sockets.keys():
                            self.send(
                                {'status': 'usuarios', 'data': 'invalido'},
                                skt)

        elif recibido['status'] == 'cerrar_juego':
            for i in self.salas:
                if recibido['sala'] == i.nombre:
                    i.eliminar(recibido['usuario'])
                    mandar = f"{i.jefe} {i.nombre} {(len(i.usuarios))}"
                    self.send({'status': 'cerrar_juego', 'data': mandar},
                              client_socket)


        elif recibido['status'] == 'chat':
            enviar = str(
                recibido['data'] + ' ' + str(self.contador_salas) + ' 1')
            for skt in self.sockets.keys():
                self.send({'status': 'chat', 'data': enviar}, skt)


        elif recibido['status'] == 'comenzar':
            for skt in self.sockets.keys():
                self.send({'status': 'comenzar','data':recibido['data']}, skt)


        elif recibido['status'] == 'crear_sala':
            self.contador_salas += 1
            numero = str(self.contador_salas)
            sala = Sala(f"Sala_{numero}", recibido['data'])
            sala.anadir_usuario(recibido['data'])
            self.salas.append(sala)
            for skt in self.sockets.keys():
                enviarr = str(
                    recibido['data'] + ' ' + str(self.contador_salas) + ' 1')
                self.send({'status': 'crear_sala', 'data': enviarr}, skt)

        elif recibido['status'] == 'entrar':
            for i in range(len(self.salas)):
                print(self.salas[i].nombre)
                if recibido['sala'] == self.salas[i].nombre:
                    self.salas[i].anadir_usuario(recibido['usuario'])
                    jefe = self.salas[i].jefe
                    participantes = len(self.salas[i].usuarios)
                    mandar = f"{jefe} {self.salas[i].nombre} {participantes}"
                    for skt in self.sockets.values():
                        if skt == recibido['usuario']:
                            self.send({'status': 'entrar', 'data': mandar},
                                      client_socket)
                    for skt in self.sockets.keys():
                        self.send({'status':'actualizar','data': mandar},skt)

        elif recibido['status'] == "cerrar":
            for i in self.usuarios:
                if i.nombre == recibido['data']:
                    print('hola')
                    i.estado = 'inactivo'
                    Escribir(i)
            del self.sockets[client_socket]

    @staticmethod
    def send(valor, socket):
        msg_json = json.dumps(valor)
        msg_bytes = msg_json.encode()
        msg_length = len(msg_bytes).to_bytes(4, byteorder="big")
        socket.send(msg_length + msg_bytes)


if __name__ == "__main__":
    server = Servidor()
    while True:
        pass
