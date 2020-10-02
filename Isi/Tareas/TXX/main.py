from tree import AlgarroboTree
from exceptions import NotFoundFile, InvalidTree, NotFoundValue
from json import load,dump


def search(tree_path, value):
    try:
        with open(tree_path, 'r') as file:
            diccionario = load(file)
            arbol=AlgarroboTree()
            a=arbol.es_algarrobo(diccionario)
            if value in a:
                pass
            else:
                raise NotFoundValue(value)

    except FileNotFoundError:
        raise NotFoundFile(tree_path)
    return []


def build_and_save(data, output_path):
    arbol=AlgarroboTree()
    for i in data:
        arbol.insert(i)
    diccionario=arbol.root.representar()
    with open(output_path,'w') as file:
        dump(diccionario,file)
    return None


def route(data, start_value, end_value):
    arbol=AlgarroboTree()
    for i in data:
        arbol.insert(i)
    lista=arbol.buscar(start_value,end_value)
    return lista
