class Usuario:
    def __init__(self, nombre, path ,estado):
        self.nombre = nombre
        self.estado = estado
        self.path = path


class Leer:
    def __init__(self):
        self.usuarios = []
        with open('Base de Datos.txt', 'r') as base:
            for linea in base:
                l = linea.strip("/n")
                l = linea.strip()
                lista = l.split(",")
                usuario = Usuario(lista[0], linea[1], linea[2])
                self.usuarios.append(usuario)


class Escribir:
    def __init__(self, usuario):
        self.usuario = usuario
        with open('Base de datos.txt', "a") as base:
            if self.usuario.path != ' ':
                path = self.usuario.path + '.png'
            else:
                path=self.usuario.path
            linea = self.usuario.nombre + "," + path + "," + self.usuario.estado+"/n"
            base.write(linea)
