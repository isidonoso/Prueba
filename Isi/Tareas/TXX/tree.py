from json import load

class Node:
    def __init__(self, value, padre=None):
        self.value = value
        self.padre = padre
        self.right_child = None
        self.left_child = None

    def representar(self):
        if self.left_child == None:
            rep_left = "None"
        else:
            rep_left = self.left_child.representar()
        if self.right_child == None:
            rep_right = "None"
        else:
            rep_right = self.right_child.representar()
        representacion = {'value': self.value, 'left': rep_left,
                          'right': rep_right}
        return representacion
        # Puede agregar los atributos que quiera, pero debe usar
        # los anteriores de todos modos


class AlgarroboTree:
    def __init__(self):
        self.root = None
        self.contador = 0
        self.lista=[]
        # Puede agregar los atributos que quiera, pero debe usar
        # los anteriores de todos modos

    def insert(self, value):
        if self.contador == 0:
            self.root = Node(value)
            self.contador = 1
        else:
            cola = []
            cola.insert(len(cola), self.root)
            while len(cola) > 0:
                nodo_actual = cola.pop()
                if nodo_actual.left_child == None:
                    nuevo_nodo = Node(value, nodo_actual)
                    self.balance(nodo_actual, nuevo_nodo)
                    nodo_actual.left_child = nuevo_nodo
                    cola.insert(0, nodo_actual.left_child)
                    cola.insert(0, nodo_actual.right_child)
                    break
                elif nodo_actual.right_child == None:
                    nuevo_nodo = Node(value, nodo_actual)
                    self.balance(nodo_actual, nuevo_nodo)
                    nodo_actual.right_child = nuevo_nodo
                    cola.insert(0, nodo_actual.left_child)
                    cola.insert(0, nodo_actual.right_child)
                    break

                cola.insert(0, nodo_actual.left_child)
                cola.insert(0, nodo_actual.right_child)

    def balance(self, nodo_actual, nuevo_nodo):
        if nodo_actual.value > nuevo_nodo.value:
            actual = nodo_actual.value
            nodo_actual.value = nuevo_nodo.value
            nuevo_nodo.value = actual
            if nodo_actual.padre != None:
                if nodo_actual.padre.value > nodo_actual.value:
                    self.balance(nodo_actual.padre, nodo_actual)

    def buscar(self, start, end):
        cola = []
        cola.insert(len(cola), self.root)
        lista = [self.root.value]
        while True:
            nodo_actual = cola.pop()
            if nodo_actual != None:
                if nodo_actual.value == end:
                    break
                else:
                    cola.insert(0, nodo_actual.left_child)
                    cola.insert(0, nodo_actual.right_child)
                    if nodo_actual.left_child != None:
                        lista.append(nodo_actual.left_child.value)
                    if nodo_actual.right_child != None:
                        lista.append(nodo_actual.right_child.value)
        start_lista = []
        contador = 0
        while True:
            if lista[contador] != start:
                start_lista.append(lista[contador])
                contador += 1
            else:
                start_lista.append(lista[contador])
                break
        end_lista = []
        contador = 0
        while True:
            if lista[contador] != end:
                end_lista.append(lista[contador])
                contador += 1
            else:
                end_lista.append(lista[contador])
                break
        if start in start_lista and end in start_lista:
            lista_def = start_lista
        elif start in end_lista and end in end_lista:
            lista_def = end_lista
        lista_niveles = []
        elevado = 0
        while len(lista_def) > 0:
            nivel = []
            for i in range(2 ** elevado):
                if len(lista_def)!=0:
                    nivel.append(lista_def[0])
                    lista_def.pop(0)
            elevado += 1
            lista_niveles.append(nivel)
        camino_start = [start]
        camino_end = [end]
        for i in range(len(lista_niveles)):
            for j in range(len(lista_niveles[i])):
                if lista_niveles[i][j] == start:
                    posicion_start = [i, j]
                if lista_niveles[i][j] == end:
                    posicion_end = [i, j]
        while posicion_end != posicion_start:
            if posicion_end[0] > posicion_start[0]:
                nivel_end = posicion_end[0] - 1
                pos_nivel_end = posicion_end[1] // 2
                camino_end.append(lista_niveles[nivel_end][pos_nivel_end])
                posicion_end = [nivel_end, pos_nivel_end]
            elif posicion_start[0] > posicion_end[0]:
                nivel_start = posicion_start[0]-1
                pos_nivel_start= posicion_start[1] // 2
                posicion_start = [nivel_start, pos_nivel_start]
                camino_start.append(lista_niveles[nivel_start][pos_nivel_start])
            elif posicion_end[0] == posicion_start[0]:
                nivel_start = posicion_start[0] - 1
                nivel_end = posicion_end[0] - 1
                pos_nivel_start = posicion_start[1] // 2
                pos_nivel_end = posicion_end[1] // 2
                camino_start.append(lista_niveles[nivel_start][pos_nivel_start])
                camino_end.append(lista_niveles[nivel_end][pos_nivel_end])
                posicion_start = [nivel_start, pos_nivel_start]
                posicion_end = [nivel_end, pos_nivel_end]
        camino = camino_start
        camino_end.pop()
        largo = len(camino_end)
        for i in range(largo):
            camino.append(camino_end[len(camino_end)-1])
            camino_end.pop()
        return camino

    def cargar(self,value):
        if self.contador == 0:
            self.root = Node(value)
            self.contador = 1
        else:
            cola = []
            cola.insert(len(cola), self.root)
            while len(cola) > 0:
                nodo_actual = cola.pop()
                if nodo_actual.left_child == None:
                    nuevo_nodo = Node(value, nodo_actual)
                    nodo_actual.left_child = nuevo_nodo
                    cola.insert(0, nodo_actual.left_child)
                    cola.insert(0, nodo_actual.right_child)
                    break
                elif nodo_actual.right_child == None:
                    nuevo_nodo = Node(value, nodo_actual)
                    nodo_actual.right_child = nuevo_nodo
                    cola.insert(0, nodo_actual.left_child)
                    cola.insert(0, nodo_actual.right_child)
                    break

                cola.insert(0, nodo_actual.left_child)
                cola.insert(0, nodo_actual.right_child)

    def obtener_numeros(self,diccionario):
        numeros=[]
        valores=diccionario.values()
        for i in valores:
            if type(i)==int:
                numeros.append(i)
            elif type(i)==dict:
                agregar=self.obtener_numeros(i)
                numeros.append(agregar)
            else:
                break
        return numeros

    def es_algarrobo(self,arbol):
        uno=self.obtener_numeros(arbol)
        #Nunca caché como pasar directo del json a arbol:(
        return uno