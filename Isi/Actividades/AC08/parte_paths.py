import os
import random

# lista de pizzas
PIZZAS = ["Pepperoni", "PolloBBQ", "Queso", "Vegetariana", "Napolitana",
          "Hawaiiana", "MeatLovers", "Jaiba", "SinQueso"]

# path de "La ultima tarea"
ULTIMA_TAREA = "la_ultima_tarea.jpg"


# Debes comenzar a editar a partir de aquí
def generar_carpetas(lista):
    """
    Función que se encarga de generar las carpetas solicitadas a partir de una
    lista.

    :param lista: Lista que contiene los strings de los nombres de las pizzas
    """

    os.makedirs("Boveda", exist_ok=True)

    for pizza in range(len(lista)):
        path = os.path.join("Boveda", lista[pizza])
        os.makedirs(path, exist_ok=True)
        while len(os.listdir(path)) < 5:
            carpeta = random.choice(lista)
            path2 = os.path.join("Boveda", lista[pizza], carpeta)
            os.makedirs(path2, exist_ok=True)
            if len(os.listdir(path)) == 5:
                break


def generar_path():
    """
    Función que se encarga de buscar entre todas las rutas existentes que
    cumplan con el requisito de que contenga a lo menos dos sub carpetas
    a partir de Boveda y elige una al azar.

    :returns: Una ruta en formato correspondiente
    """
    lista_path = []
    for raiz, boveda, archivos in os.walk("Boveda", topdown=True):
        r=raiz.split(os.sep)
        if len (r)==3:
            lista_path.append(raiz)
    path_final = random.choice(lista_path)
    return path_final


def esconder_obras(imagen, ruta):
    """
    Función que se encarga de generar una copia de la imagen  a la ruta
    entregada.

    :param imagen: String con el nombre de la imagen 1 con su extensión.
    :param ruta: Ruta de la carpeta destino al que se moverá el archivo.
    """

    path = os.path.join(ruta, imagen)
    for raiz, boveda, archivos in os.walk("Boveda", topdown=True):
        r=raiz.split(os.sep)
        if imagen in r:
            os.remove(raiz)



    file = open(imagen, "rb")
    string=file.read()
    file.close()

    final = open(path, "wb")
    final.write(string)
    final.close()

# Ejecutando
if __name__ == "__main__":

    # Está prohibido modificar cualquier parte de esta sección
    print("\nGenerando las carpetas solicitadas...")

    try:
        generar_carpetas(PIZZAS)
    except FileExistsError:
        print("ERROR: ya existen una o más carpetas con el mismo nombre.")

    print("\nGenerando la ruta donde se esconderan los archivos...")
    path_generado = generar_path()
    print("\nEl path generado es {}".format(path_generado))

    print("\nEscondiendo la obra super secreta en el path anterior...")

    try:
        esconder_obras(ULTIMA_TAREA, path_generado)
    except FileNotFoundError:
        print("ERROR: el path de la imagen y/o del generado son inválidos.")
