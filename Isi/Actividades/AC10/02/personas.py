class Jefe:
    def __init__(self, ataque):
        self.ataque = ataque

    def tiempo(self, progravenger):
        """Completar"""
        self.vida += 0.1 * self.vida_max
        progravenger.arma = True
        progravenger.vida += 0.1 * progravenger.vida_max
        nombre = progravenger.nombre
        print(
            'DrHenry ha ocupado el contenido del Tiempo contra ' + nombre)

    def poder(self, progravenger):
        """Completar"""
        progravenger.vida -= 0.2 * progravenger.vida_max
        nombre = progravenger.nombre
        print(
            'DrHenry ha ocupado el contenido del Poder contra ' + nombre)

    def realidad(self, progravenger):
        """Completar"""
        progravenger.arma = False
        nombre = progravenger.nombre
        print(
            'DrHenry ha ocupado el contenido de la Realidad contra ' + nombre)


class Programmer:
    def __init__(self, vida):
        self.vida_max = vida
        self._vida = vida

    def decodificar(self, enemigo):
        """Completar"""
        if enemigo._vida % self.ataque:
            vida = self.vida_max
            self.vida += 0.1 * vida
            return True
        else:
            return False

    @property
    def vida(self):
        """Completar"""
        return self._vida

    @vida.setter
    def vida(self, value):
        """Completar"""
        self._vida = value
        if self._vida < 0:
            self._vida = 0
            if self.nombre != 'Dr Henry':
                print('Dr Henry ha derrotado a ' + self.nombre)
        elif self._vida > self.vida_max:
            self._vida = self.vida_max


class Avenger:
    def __init__(self, fuerza, arma):
        self.fuerza = fuerza
        self.arma = arma
        self._ataque = self.fuerza

    @property
    def ataque(self):
        """Completar"""
        if self.arma == True:
            self._ataque = 1.5 * self.fuerza
        else:
            self._ataque = self.fuerza
        return self._ataque


class Progravenger(Avenger, Programmer):
    def __init__(self, vida, fuerza, arma, nombre):
        Avenger.__init__(self, fuerza, arma)
        Programmer.__init__(self, vida)

        self.nombre = nombre

    def atacar(self, henry):
        """Completar"""
        decodif = self.decodificar(henry)
        if decodif == True:
            print(self.nombre + ' ha decodificado a DrHenry')
        henry.vida -= self.ataque
        print(self.nombre + ' ha atacado a Dr Henry')


class DrHenry(Jefe, Programmer):
    def __init__(self, vida, ataque):
        Jefe.__init__(self, ataque)
        Programmer.__init__(self, vida)

    def atacar(self, progravenger):
        """Completar"""
        decodif = self.decodificar(progravenger)
        if decodif == True:
            print('Dr Henry ha decodificado a ' + progravenger.nombre)
        vida = progravenger._vida
        if progravenger.arma == True and vida < 0.6 * progravenger.vida_max:
            self.realidad(progravenger)
        elif self._vida < 0.05 * self.vida_max:
            self.tiempo(progravenger)
        else:
            self.poder(progravenger)
