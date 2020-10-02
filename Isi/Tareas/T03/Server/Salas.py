class Sala:
    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.usuarios = []
        self.chao = {}
        self.jefe = jefe

    def comando_chao(self, user):
        devolver = False
        if user in self.usuarios:
            if user in self.chao.keys():
                self.chao[user] += 1
                if self.chao[user] >= (len(self.chao) / 2):
                    self.eliminar(user)
                    devolver = True
        return devolver

    def eliminar(self, user):
        del self.chao[user]
        for i in range(len(self.usuarios)):
            if self.usuarios[i] == user:
                self.usuarios.pop(i)

    def salir(self, user):
        for i in self.usuarios:
            if self.usuarios[i] == user:
                self.usuarios.pop(i)

    def anadir_usuario(self, user):
        if user not in self.usuarios:
            self.usuarios.append(user)
            self.chao[user] = 0
