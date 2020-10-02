from math import sqrt
from zlib import crc32


class FiltroDibujo:
    def __init__(self, path, nombre):
        self.path = path
        self.nombre = nombre
        if self.path:
            imagen = []
            i_grises = []
            conv1 = []
            conv2 = []
            D1 = []
            D2 = []
            gradiente = []
            i_binaria = []
            bin_invertida = []
            final = []
            M1 = [[1, 0], [0, -1]]
            M2 = [[0, 1], [-1, 0]]
            imagen = get_pixels(self.path)
            for i in range(len(imagen)):
                fila = []
                for j in range(len(imagen[0])):
                    x = int(round(
                        imagen[i][j][0] * 0.299 + imagen[i][j][1] * 0.587 +
                        imagen[i][j][2] * 0.114, 0))
                    fila.append(x)
                i_grises.append(fila)

            for i in range(len(i_grises) - 1):
                fila = []
                for j in range(len(i_grises[0]) - 1):
                    Y = i_grises[i][j] * M1[0][0] + i_grises[i][j + 1] * M1[0][
                        1] + \
                        i_grises[i + 1][j] * M1[1][0] + \
                        i_grises[i + 1][j + 1] * M1[1][1]
                    fila.append(Y)
                conv1.append(fila)

            for i in range(len(i_grises) - 1):
                fila = []
                for j in range(len(i_grises[0]) - 1):
                    Y = i_grises[i][j] * M2[0][0] + i_grises[i][j + 1] * M2[0][
                        1] + \
                        i_grises[i + 1][j] * M2[1][0] + \
                        i_grises[i + 1][j + 1] * M2[1][1]
                    fila.append(Y)
                conv2.append(fila)

            for i in range(len(conv1)):
                fila = []
                for j in range(len(conv1[0])):
                    Z = conv1[i][j] ** 2
                    fila.append(Z)
                D1.append(fila)

            for i in range(len(conv2)):
                fila = []
                for j in range(len(conv2[0])):
                    Z = conv2[i][j] ** 2
                    fila.append(Z)
                D2.append(fila)

            for i in range(len(D1)):
                fila = []
                for j in range(len(D1[0])):
                    G = sqrt(D1[i][j] + D2[i][j])
                    fila.append(G)
                gradiente.append(fila)

            for i in range(len(gradiente)):
                fila = []
                for j in range(len(gradiente[0])):
                    if gradiente[i][j] <= 30:
                        fila.append(0)
                    else:
                        fila.append(255)
                i_binaria.append(fila)

            for i in range(len(i_binaria)):
                fila = []
                for j in range(len(i_binaria[0])):
                    if i_binaria[i][j] == 0:
                        fila.append(255)
                    else:
                        fila.append(0)
                bin_invertida.append(fila)

            for i in range(len(bin_invertida)):
                fila = []
                for j in range(len(bin_invertida[0])):
                    lin = (
                        bin_invertida[i][j], bin_invertida[i][j],
                        bin_invertida[i][j])
                    fila.append(lin)
                final.append(fila)
            imagen = final
            alto = len(imagen)
            ancho = len(imagen[0])
            if len(imagen[0][1]) == 3:
                tipo = 2
            else:
                tipo = 6

            tipo_i = 'I'.encode()
            tipo_ii = 'H'.encode()
            tipo_iii = 'D'.encode()
            tipo_iv = 'R'.encode()

            ancho_byte = int.to_bytes(ancho, 4, "big")
            alto_byte = int.to_bytes(alto, 4, "big")
            prof_byte = int.to_bytes(8, 1, "big")
            tipo_byte = int.to_bytes(tipo, 1, "big")
            comp_byte = int.to_bytes(0, 1, "big")
            filtro_byte = int.to_bytes(0, 1, "big")
            entre_byte = int.to_bytes(0, 1, "big")

            tipo2_i = 'I'.encode()
            tipo2_ii = 'D'.encode()
            tipo2_iii = 'A'.encode()
            tipo2_iv = 'T'.encode()

            tipo3_i = 'I'.encode()
            tipo3_ii = 'E'.encode()
            tipo3_iii = 'N'.encode()
            tipo3_iv = 'D'.encode()

            lista_inicio = bytearray()
            lista_inicio.extend(int.to_bytes(137, 1, "big"))
            lista_inicio.extend(int.to_bytes(80, 1, "big"))
            lista_inicio.extend(int.to_bytes(78, 1, "big"))
            lista_inicio.extend(int.to_bytes(71, 1, "big"))
            lista_inicio.extend(int.to_bytes(13, 1, "big"))
            lista_inicio.extend(int.to_bytes(10, 1, "big"))
            lista_inicio.extend(int.to_bytes(26, 1, "big"))
            lista_inicio.extend(int.to_bytes(10, 1, "big"))

            lista_ihdr = bytearray()
            lista_ihdr.extend(tipo_i)
            lista_ihdr.extend(tipo_ii)
            lista_ihdr.extend(tipo_iii)
            lista_ihdr.extend(tipo_iv)
            lista_ihdr.extend(ancho_byte)
            lista_ihdr.extend(alto_byte)
            lista_ihdr.extend(prof_byte)
            lista_ihdr.extend(tipo_byte)
            lista_ihdr.extend(comp_byte)
            lista_ihdr.extend(filtro_byte)
            lista_ihdr.extend(entre_byte)

            lista_idat = bytearray()
            lista_idat.extend(tipo2_i)
            lista_idat.extend(tipo2_ii)
            lista_idat.extend(tipo2_iii)
            lista_idat.extend(tipo2_iv)

            lista_idata = bytearray()

            for i in range(len(imagen)):
                lista_idata.extend(int.to_bytes(0, 1, "big"))
                for j in range(len(imagen[0])):
                    if tipo == 2:
                        R = imagen[i][j][0]
                        G = imagen[i][j][1]
                        B = imagen[i][j][2]
                        lista_idata.extend(int.to_bytes(R, 1, "big"))
                        lista_idata.extend(int.to_bytes(G, 1, "big"))
                        lista_idata.extend(int.to_bytes(B, 1, "big"))
                    else:
                        R = imagen[i][j][0]
                        G = imagen[i][j][1]
                        B = imagen[i][j][2]
                        A = imagen[i][j][3]
                        lista_idata.extend(int.to_bytes(R, 1, "big"))
                        lista_idata.extend(int.to_bytes(G, 1, "big"))
                        lista_idata.extend(int.to_bytes(B, 1, "big"))
                        lista_idata.extend(int.to_bytes(A, 1, "big"))

            lista_idat.extend(compress(lista_idata))
            lista_iend = bytearray()
            lista_iend.extend(tipo3_i)
            lista_iend.extend(tipo3_ii)
            lista_iend.extend(tipo3_iii)
            lista_iend.extend(tipo3_iv)

            largo_ihdr = int.to_bytes(len(lista_ihdr) - 4, 4, "big")
            largo_idat = int.to_bytes(len(lista_idat) - 4, 4, "big")
            largo_iend = int.to_bytes(len(lista_iend) - 4, 4, "big")

            crc_1 = crc32(lista_ihdr)
            crc_2 = crc32(lista_idat)
            crc_3 = crc32(lista_iend)

            crc_ihdr = int.to_bytes(crc_1, 4, "big")
            crc_idat = int.to_bytes(crc_2, 4, "big")
            crc_iend = int.to_bytes(crc_3, 4, "big")

            lista_total = bytearray()
            lista_total.extend(lista_inicio)
            lista_total.extend(largo_ihdr)
            lista_total.extend(lista_ihdr)
            lista_total.extend(crc_ihdr)
            lista_total.extend(largo_idat)
            lista_total.extend(lista_idat)
            lista_total.extend(crc_idat)
            lista_total.extend(largo_iend)
            lista_total.extend(lista_iend)
            lista_total.extend(crc_iend)
            self.matriz = lista_total

            with open(self.nombre + '_filtro.png', 'wb') as file:
                file.write(lista_total)


from zlib import compress
from pixel_collector import get_pixels


class GuardarImagen:
    def __init__(self, matriz, nombre):
        self.nombre = nombre
        self.matriz = matriz
        if self.matriz:
            imagen = self.matriz
            alto = len(imagen)
            ancho = len(imagen[0])
            if len(imagen[0][1]) == 3:
                tipo = 2
            else:
                tipo = 6

            tipo_i = 'I'.encode()
            tipo_ii = 'H'.encode()
            tipo_iii = 'D'.encode()
            tipo_iv = 'R'.encode()

            ancho_byte = int.to_bytes(ancho, 4, "big")
            alto_byte = int.to_bytes(alto, 4, "big")
            prof_byte = int.to_bytes(8, 1, "big")
            tipo_byte = int.to_bytes(tipo, 1, "big")
            comp_byte = int.to_bytes(0, 1, "big")
            filtro_byte = int.to_bytes(0, 1, "big")
            entre_byte = int.to_bytes(0, 1, "big")

            tipo2_i = 'I'.encode()
            tipo2_ii = 'D'.encode()
            tipo2_iii = 'A'.encode()
            tipo2_iv = 'T'.encode()

            tipo3_i = 'I'.encode()
            tipo3_ii = 'E'.encode()
            tipo3_iii = 'N'.encode()
            tipo3_iv = 'D'.encode()

            lista_inicio = bytearray()
            lista_inicio.extend(int.to_bytes(137, 1, "big"))
            lista_inicio.extend(int.to_bytes(80, 1, "big"))
            lista_inicio.extend(int.to_bytes(78, 1, "big"))
            lista_inicio.extend(int.to_bytes(71, 1, "big"))
            lista_inicio.extend(int.to_bytes(13, 1, "big"))
            lista_inicio.extend(int.to_bytes(10, 1, "big"))
            lista_inicio.extend(int.to_bytes(26, 1, "big"))
            lista_inicio.extend(int.to_bytes(10, 1, "big"))

            lista_ihdr = bytearray()
            lista_ihdr.extend(tipo_i)
            lista_ihdr.extend(tipo_ii)
            lista_ihdr.extend(tipo_iii)
            lista_ihdr.extend(tipo_iv)
            lista_ihdr.extend(ancho_byte)
            lista_ihdr.extend(alto_byte)
            lista_ihdr.extend(prof_byte)
            lista_ihdr.extend(tipo_byte)
            lista_ihdr.extend(comp_byte)
            lista_ihdr.extend(filtro_byte)
            lista_ihdr.extend(entre_byte)

            lista_idat = bytearray()
            lista_idat.extend(tipo2_i)
            lista_idat.extend(tipo2_ii)
            lista_idat.extend(tipo2_iii)
            lista_idat.extend(tipo2_iv)
            lista_idata = bytearray()
            print("hola")
            for i in range(len(imagen)):
                lista_idata.extend(int.to_bytes(0, 1, "big"))
                for j in range(len(imagen[0])):
                    if tipo == 2:
                        R = imagen[i][j][0]
                        G = imagen[i][j][1]
                        B = imagen[i][j][2]
                        lista_idata.extend(int.to_bytes(R, 1, "big"))
                        lista_idata.extend(int.to_bytes(G, 1, "big"))
                        lista_idata.extend(int.to_bytes(B, 1, "big"))
                    elif tipo == 6:
                        R = imagen[i][j][0]
                        G = imagen[i][j][1]
                        B = imagen[i][j][2]
                        A = imagen[i][j][3]
                        lista_idata.extend(int.to_bytes(R, 1, "big"))
                        lista_idata.extend(int.to_bytes(G, 1, "big"))
                        lista_idata.extend(int.to_bytes(B, 1, "big"))
                        lista_idata.extend(int.to_bytes(A, 1, "big"))

            lista_idat.extend(compress(lista_idata))

            lista_iend = bytearray()
            lista_iend.extend(tipo3_i)
            lista_iend.extend(tipo3_ii)
            lista_iend.extend(tipo3_iii)
            lista_iend.extend(tipo3_iv)

            len_ihdr = len(lista_ihdr) - 4
            largo_ihdr = int.to_bytes((len_ihdr), 4, "big")
            largo_idat = int.to_bytes((len(lista_idat) - 4), 4, "big")
            largo_iend = int.to_bytes((len(lista_iend) - 4), 4, "big")

            crc_1 = crc32(lista_ihdr)
            crc_2 = crc32(lista_idat)
            crc_3 = crc32(lista_iend)

            crc_ihdr = int.to_bytes(crc_1, 4, "big")
            crc_idat = int.to_bytes(crc_2, 4, "big")
            crc_iend = int.to_bytes(crc_3, 4, "big")

            lista_total = bytearray()
            lista_total.extend(lista_inicio)
            lista_total.extend(largo_ihdr)
            lista_total.extend(lista_ihdr)
            lista_total.extend(crc_ihdr)
            lista_total.extend(largo_idat)
            lista_total.extend(lista_idat)
            lista_total.extend(crc_idat)
            lista_total.extend(largo_iend)
            lista_total.extend(lista_iend)
            lista_total.extend(crc_iend)
        self.bytes = lista_total

        with open(self.nombre + '.png', 'wb') as file:
            file.write(lista_total)
