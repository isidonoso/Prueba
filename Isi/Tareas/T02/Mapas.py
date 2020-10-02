from os import getcwd, listdir

lista_mapas = (listdir(getcwd() + "\\mapas"))
mapa_para_traducir = []
for i in range(len(lista_mapas)):
    mini_mapa = lista_mapas[i]
    mapa_individual = []
    with open(getcwd() + "\\mapas\\" + str(mini_mapa),
              encoding='utf8') as mapa:

        for linea in mapa:
            l = linea.strip("/n")
            l = linea.strip()
            l = l.split(" ")
            l = "".join(l)
            mapa_individual.append(l)
    mapa_para_traducir.append(mapa_individual)

lista_puntajes = []
with open(getcwd() + "\\puntajes.txt", encoding='utf8') as puntaje:
    for linea in puntaje:
        l = linea.strip("/n")
        l = linea.strip()
        r = l.split(",")
        lista_puntajes.append(r)
lista_puntajes.sort(reverse=True)
ranking = lista_puntajes[0:10]
