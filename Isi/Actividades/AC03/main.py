from leer_archivos import obtener_sistema


class Instalacion:
    def __init__(self, **kwargs):
        self.tipo = kwargs["tipo"]
        self.region = kwargs["region"]
        self.comuna = kwargs["comuna"]
        self.hijos = []
        self.consumo = float(kwargs["consumo"])
        self.energia = float(kwargs["energia"])

    def agregar_instalacion(self, instalacion):
        ### Caso Base
        if instalacion.tipo == "Distribuidora Regional":
            if self.tipo == "Generadora":
                self.hijos.append(instalacion)

        ### Caso comunal
        elif instalacion.tipo == "Distribuidora Comunal":
            if self.tipo == "Distribuidora Regional":
                if self.region == instalacion.region:
                    self.hijos.append(instalacion)
            ### Si yo no soy regional, si o si seré una generadora, por
            # enunciado nunca te van  pasar una instalación que este arriba
            # en el árbol, entonces alguno de mis hijos debe ser regional
            else:
                for hijo in self.hijos:
                    hijo.agregar_instalacion(instalacion)

        ### Caso casa
        elif instalacion.tipo == "Casa":
            # tengo que verificar que este en la misma región y comuna
            if self.tipo == "Distribuidora Comunal":
                if self.region == instalacion.region:
                    if self.comuna == instalacion.comuna:
                        self.hijos.append(instalacion)
            else:
                for hijo in self.hijos:
                    hijo.agregar_instalacion(instalacion)

    def distribuir_energia(self, energia):
        if len(self.hijos) > 0:
            e_hijo = (energia - self.consumo) / float(len(self.hijos))
            for hijo in self.hijos:
                hijo.energia = e_hijo
                hijo.distribuir_energia(e_hijo)

    def contar_casas(self):
        total = len(self.hijos)
        for hijo in self.hijos:
            total += hijo.contar_casas()
        return total

    def consumido(self):
        consumo = int(self.consumo)
        for hijo in self.hijos:
            consumo += int(hijo.consumo)
        return consumo


def resumen_sistema(sistema):
    region = sistema.region
    comuna = sistema.comuna
    consumo = sistema.consumo
    for hijo in sistema.hijos:
        consumo += hijo.consumo
        for nieto in hijo.hijos:
            consumo += nieto.consumo
            for bisnieto in nieto.hijos:
                consumo += bisnieto.consumo
    contar_casas = sistema.contar_casas()
    print("Resumen del sistema:")
    print("     La ubicación de la generadora es " + comuna + ", " + region)
    print("     Consumo total: " + str(consumo))
    print("     Número de instalaciones: " + str(contar_casas))


#### revisar consumo por casa, eso sumarlo y luego entregar
def comuna_mayor_gasto(sistema):
    consumo = 0
    comuna_region = []
    for region in sistema.hijos:
        energia_comuna = 0
        for comuna in region.hijos:
            energia_comuna += comuna.consumido()
        if energia_comuna > consumo:
            comuna_region = [comuna.comuna, comuna.region]
            consumo = energia_comuna
    print("")
    print("Comuna con mayor gasto:")
    print("     Comuna: " + comuna_region[0])
    print("     Región: " + comuna_region[1])


def casas_insuficiencia(sistema):
    insuficiencia = 0
    for region in sistema.hijos:
        for comuna in region.hijos:
            for casa in comuna.hijos:
                if casa.energia < casa.consumo:
                    insuficiencia += 1
    print("")
    print("Casas con energía insuficiente")
    print("     Número de casas: " + str(insuficiencia))


def instanciar_sistema(atributos_sistema):
    # No modificar.
    # Se crea la central generadora
    central_generadora = Instalacion(**atributos_sistema[0])

    # Se crean y agregan las demás instalaciones
    for atributos in atributos_sistema[1:]:
        nueva_instalacion = Instalacion(**atributos)
        central_generadora.agregar_instalacion(nueva_instalacion)

    # Se distribuye la energia a través del sistema
    central_generadora.distribuir_energia(central_generadora.energia)

    return central_generadora


if __name__ == '__main__':
    # No modificar
    # Se probará DCCableling para 4 sistemas electricos:
    for i in range(1, 5):
        print(f"CONSULTAS SISTEMA ELÉCTRICO N°{i}")
        print("---------------------" * 2)
        atributos_de_sistema = obtener_sistema()
        sistema_electrico = instanciar_sistema(atributos_de_sistema)
        resumen_sistema(sistema_electrico)
        comuna_mayor_gasto(sistema_electrico)
        casas_insuficiencia(sistema_electrico)
        print("---------------------" * 2)
