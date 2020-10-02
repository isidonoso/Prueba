import os


class Extraterrestre:
    def __init__(self, nombre, iu, numeros):
        self.nombre = nombre
        self.iu = iu
        self.numeros = numeros

    def __repr__(self):
        return f"Extraterrestre {self.nombre} con poder: {self.numeros}"


def cargar_extraterrestres(path_extraterrestres):
    """Completar"""
    diccionario = {}
    with open(path_extraterrestres, 'r', encoding='utf8') as file:
        for linea in file:
            l = linea.strip("/n")
            l = linea.strip()
            l = l.split(",")
            nombre = l[0]
            iu = l[1]
            l[2].strip(("/n"))
            numeros = set(l[2].split(';'))
            extraterrestre = Extraterrestre(nombre, iu, numeros)
            diccionario[iu] = extraterrestre
    return diccionario


def simular_guerra(extraterrestres, path_guerra):
    """Completar"""
    stack = []
    with open(path_guerra, 'r', encoding='utf8') as file:
        for linea in file:
            l = linea.strip("/n")
            l = linea.strip()
            if l == 'undo':
                ultima_accion = stack.pop()
                robados = ultima_accion[0]
                ataca = ultima_accion[1]
                defiende = ultima_accion[2]
                numeros_a = ataca.numeros
                numeros_d = defiende.numeros
                ataca.numeros = numeros_a - robados
                defiende.numeros = numeros_d | robados

            else:
                l = l.split(",")
                ataca = extraterrestres[l[0]]
                defiende = extraterrestres[l[1]]
                numeros_a = ataca.numeros
                numeros_d = defiende.numeros
                robados = numeros_d - numeros_a
                ataca.numeros = numeros_a | robados
                defiende.numeros = numeros_d - robados
                accion = [robados, ataca, defiende]
                stack.append(accion)


def encontrar_maximo_poder(extraterrestres):
    """Completar"""
    lista_extraterrestres = extraterrestres.values()
    mayor_nombre = ''
    numero_mayor = 0
    for extraterrestre in lista_extraterrestres:
        if len(extraterrestre.numeros) > numero_mayor:
            numero_mayor = len(extraterrestre.numeros)
            mayor_nombre = extraterrestre.nombre
    return mayor_nombre


if __name__ == "__main__":

    # Cambiar valor si quieres usar datos pequeños o grandes
    usar_mini = True

    if usar_mini:
        path_extraterrestres = os.path.join("data", "extraterrestres_mini.txt")
        path_guerra = os.path.join("data", "guerra_mini.txt")
    else:
        path_extraterrestres = os.path.join("data", "extraterrestres.txt")
        path_guerra = os.path.join("data", "guerra.txt")

    print("Cargando extraterrestres...")
    extraterrestres = cargar_extraterrestres(path_extraterrestres)

    if usar_mini:
        print("Los extraterrestres:")
        print(extraterrestres)

    print("Simulando guerra...")
    simular_guerra(extraterrestres, path_guerra)

    if usar_mini:
        print("Los extraterrestres:")
        print(extraterrestres)

    print("Buscando el mayor ladron de poder...")
    maximo_poder = encontrar_maximo_poder(extraterrestres)
    print(f"El con mayor poder es: {maximo_poder}")
