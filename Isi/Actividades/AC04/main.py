import json

PATH_EXPORTACIONES = 'exportaciones.json'


class Pais:
    """
    Clase Pais que almacena su nombre y sus exportaciones.
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.exportaciones = set()

    def agregar_exportacion(self, producto, destino):
        """
        Agrega una exportacion a lista de tuplas
        """
        tupla = (producto, destino)
        self.exportaciones.add(tupla)

    def exporta_esto(self, producto):
        """
        Recibe un producto y retorna True si esta
        presente dentro de sus exportaciones, sino retorna False
        """
        exporta = False
        for tipo_producto in range(len(self.exportaciones)):
            if self.exportaciones[tipo_producto][0] == producto:
                exporta = True
        return exporta


class RedComercio:
    """
    Clase RedComercio que almacena a los paises que la componen
    """

    def __init__(self, data_exportaciones):
        """
        Aquí se deberán crear los nodos pais y agregar sus exportaciones
        """
        self.paises = []
        llaves = data_exportaciones.keys()
        for i in llaves:
            pais = Pais(i)
            self.paises.append(pais)
        item = data_exportaciones.items()
        items = list(item)
        for i in range(len(items)):
            exp = items[i][1]
            expo = exp.items()
            exportacion = list(expo)
            for pais_exportador in range(len(items)):
                pais_a_agregar = items[pais_exportador][0]
                imp = items[pais_exportador][1]
                importa = imp.items()
                importador = list(importa)
                for importadores in range(len(importador)):
                    for pais in range(len(self.paises)):
                        producto = importador[importadores][1]
                        if importador[importadores][0] == self.paises[
                            pais].nombre:
                            for a in range(len(self.paises)):
                                if pais_a_agregar == self.paises[a].nombre:
                                    self.paises[a].agregar_exportacion(producto,
                                                                       self.paises[
                                                                           pais])

    def productos_importados(self, nombre_pais):
        """
        Retorna un set con todos los productos que son importados
        en un país determinado
        """
        productos_importados = set()
        for i in range (len(self.paises)):
            if self.paises[i].nombre == nombre_pais:
                nombre_p =self.paises[i]
        for pais in range(len(self.paises)):
            if self.paises[pais].nombre != nombre_pais:
                exportaciones_pais = list(self.paises[pais].exportaciones)
                for i in range(len(exportaciones_pais)):
                    if exportaciones_pais[1] == nombre_p:
                        productos_importados.add(exportaciones_pais[0])
        return productos_importados

    def productos_producidos(self, nombre_pais):
        """
        Retorna un set de todos los productos que produce un país
        """
        pass

    def paises_clientes_finales(self, producto, nombre_pais):
        """
        Retorna un set con todos los países a los que llega finalmente
        un producto desde un país dado
        """
        pass


if __name__ == "__main__":
    # Esta sección carga el archivo en EXPORTACIONES, no la modifiques
    with open(PATH_EXPORTACIONES, "r", encoding="utf8") as file:
        EXPORTACIONES = json.load(file)
    # La siguiente línea instancia a la clase RedComercio para crear el grafo
    COMERCIO = RedComercio(data_exportaciones=EXPORTACIONES)

    # Las siguientes líneas llaman a las consultas por implementar
    # para que compares tus resultados de consultas
    print(COMERCIO.productos_importados("Bélgica"))
    print(COMERCIO.productos_importados("Dinamarca"))
    print(COMERCIO.productos_importados("Estonia"))

    print(COMERCIO.productos_producidos("Estonia"))
    print(COMERCIO.productos_producidos("España"))
    print(COMERCIO.productos_producidos("Finlandia"))

    print(COMERCIO.paises_clientes_finales("Oro", "Albania"))
    print(COMERCIO.paises_clientes_finales("Oro", "Estonia"))
    print(COMERCIO.paises_clientes_finales("Carbón", "España"))
    print(COMERCIO.paises_clientes_finales("Trigo", "Finlandia"))

for i in range(len(COMERCIO.paises)):
    print(COMERCIO.paises[i].nombre)
    print(COMERCIO.paises[i].exportaciones)
