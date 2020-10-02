import threading
import time
import random


def desencriptar(texto):
    """"Funcion para desencriptar el problema dada por los ayudantes"""
    murci = "murcielago"
    numeros = "0123456789"
    nuevo_texto = ""

    for letras in texto:
        if letras in murci:
            nueva_letra = murci.index(letras)
            nuevo_texto += str(nueva_letra)
        elif letras in numeros:
            nueva_letra = numeros.index(letras)
            nuevo_texto += str(murci[int(nueva_letra)])
        else:
            nuevo_texto += letras
    return nuevo_texto


class Dragon(threading.Thread):

    def __init__(self, nombre, jinete, dani):
        super().__init__()
        self.jinete = jinete
        self.velocidad = random.randint(30, 40)
        self.nombre = nombre
        self.distancia_recorrida = self.velocidad
        self.disminuir = False
        self.dani=dani

    def comer(self):
        self.dani.convencer(self.nombre)

    def run(self):
        while True:
            time.sleep(1)
            prob_comer = random.randint(1, 10)
            if self.distancia_recorrida >= 500 and prob_comer == 1:
                print(self.nombre + " esta comiendo")
                self.comer()
            elif self.disminuir == True:
                disminuir = random.randint(0, 5)
                nueva = self.velocidad - disminuir
                if self.velocidad > 15:
                    if nueva >= 15:
                        self.velocidad = nueva
                    else:
                        self.velocidad = 15
                self.distancia_recorrida += self.velocidad
                self.disminuir = False
            else:
                original = self.distancia_recorrida
                self.distancia_recorrida += self.velocidad
                nueva = self.distancia_recorrida
                if original <= 500 and nueva >= 500:
                    self.disminuir = True
            if self.distancia_recorrida >= 1000:
                self.distancia_recorrida = 1000
                break

    def __str__(self):
        return "Nombre del dragón: "+self.nombre


class Dany:
    lock = "esto podría ser un lock..."

    def __init__(self):
        self.lock = threading.Lock()

    def convencer(self, dragon):
        self.lock.acquire()
        print("Dany esta convenciendo a " + dragon)
        tiempo = random.randint(2, 5)
        time.sleep(tiempo)
        self.lock.release()
        print("Dani se demoró " + str(tiempo) + " en convencer a " + dragon)


class Jinete(threading.Thread):
    lock = "esto podria ser un lock..."

    def __init__(self, nombre, dragon,dani):
        super().__init__()
        self.dragon = dragon
        self.nombre = nombre
        self.resuelto = "no"

    def __str__(self):
        return "Soy " + self.nombre + " y " + self.resuelto + " resolví el problema"

    def run(self):
        pass


class Viaje(threading.Thread):
    def __init__(self):
        super().__init__()
        self.dani = Dany()

    def agregar(self, nombre_dragon, nombre_jinete):
        jinete = Jinete(nombre_jinete, nombre_dragon, self.dani)
        dragon = Dragon(nombre_dragon, jinete, self.dani)
        return dragon, jinete

    def run(self):
        j1 = input(("Ingrese el nombre del primer jinete "))
        j2 = input(("Ingrese el nombre del segundo jinete "))
        j3 = input(("Ingrese el nombre del tercer jinete "))
        d1 = input(("Ingrese el nombre del primer dragón "))
        d2 = input(("Ingrese el nombre del segundo dragón "))
        d3 = input(("Ingrese el nombre del tercer dragón "))
        dragon1, jinete1 = self.agregar(d1, j1)
        dragon2, jinete2 = self.agregar(d2, j2)
        dragon3, jinete3 = self.agregar(d3, j3)
        dragon1.start()
        dragon2.start()
        dragon3.start()
        jinete1.start()
        jinete2.start()
        jinete3.start()
        print("Se crearon los dragones y los jinetes")

        #Revisar que haya terminado
        if dragon1.is_alive()==False and dragon2.is_alive()==False and dragon3.is_alive()==False and jinete1.is_alive()==False and jinete2.is_alive()==False and jinete3.is_alive()==False:
            print("Equipo 1")
            print(dragon1)
            print(dragon1.distancia_recorrida)
            print(jinete1)
            print("Equipo 3")
            print(dragon2)
            print(dragon2.distancia_recorrida)
            print(jinete2)
            print("Equipo 3")
            print(dragon3)
            print(dragon3.distancia_recorrida)
            print(jinete3)
            print(time.time())




if __name__ == "__main__":
    # Aca deben instanciar las distintas clases y empezar el rescate
    viaje=Viaje()
    viaje.start()
