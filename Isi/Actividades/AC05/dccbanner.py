import json
from alumnos import Alumno
from excepcion_propia import ErrorDatos
import csv


class DCCBanner:
    def __init__(self):
        self.cursos = dict()
        self.alumnos = list()

    def chequear_rut(self, alumno):
        '''
        Recibe un alumno y levanta una excepción en caso de que su rut no siga
        el formato correcto.
        '''
        rut = alumno.rut
        lista_rut = list(rut)
        if "." in lista_rut:
            raise ValueError("El formato del rut es incorrecto", 0)
        if "-" not in lista_rut:
            raise ValueError("El formato del rut es incorrecto", 1)

    def chequear_numero_alumno(self, alumno):
        '''
        Recibe un alumno y levanta una excepción en caso de que su nro. de
        alumno no siga el formato correcto.
        '''
        año_ingreso = alumno.ano_ingreso
        n_alumno = alumno.num_alumno
        carrera = alumno.carrera
        if carrera == "Ingenieria":
            carrera = "63"
        else:
            carrera = "61"
        lista_n_alumno = list(n_alumno)
        ultimo = lista_n_alumno[len(lista_n_alumno) - 1]
        if ultimo.isdigit() == False and ultimo != "J":
            raise ValueError(
                "La letra incluida en el numero de alumno es incorrecta", 0)
        for i in range(len(lista_n_alumno)):
            if lista_n_alumno[i].isdigit() == False and i != (
                    len(lista_n_alumno) - 1):
                raise ValueError(" Hay una letra donde no corresponde", 1)
        lista_año = list(año_ingreso)
        lista_año = lista_año[2:]
        lista_carrera = list(carrera)
        if lista_n_alumno[0:2] != lista_año:
            raise ValueError(
                " El numero de alumno no contiene el año de ingreso correcto",
                2)
        if lista_n_alumno[2:4] != lista_carrera:
            raise ValueError(
                "El código de carrera inscrito por el alumno es incorrecto", 3)

    def chequear_curso(self, alumno):
        '''
        Recibe un alumno y levanta una excepción en caso de que el curso que
        haya pedido no siga el formato correcto.
        '''
        curso = alumno.curso
        seccion = alumno.seccion
        lista_cursos = self.cursos.keys()
        if curso not in lista_cursos:
            raise KeyError("El curso solicitado no es válido", 0)
        if seccion.isdigit() == False:
            raise ValueError("El formato de la sección es incorrecto", 0)
        if curso in lista_cursos:
            secciones = self.cursos[curso]
            lista_secciones = secciones.keys()
            if seccion not in lista_secciones:
                raise KeyError("La sección ingresada no existe", 1)
        lista_curso = list(curso)
        for i in range(len(lista_curso)):
            if lista_curso[i] == " ":
                raise ValueError(
                    "El nombre del curso esta en un formato equivocado", 1)

    def inscribir_alumnos(self):
        '''
        Para cada uno de los alumnos en file_path chequea que su información
        esté correcta, si no lo está la corrige. Finalmente los inscribe al
        curso pedido.
        '''
        while True:
            try:
                self.chequear_rut(alumno)

            except ValueError as err:
                error = err.args
                if error[1] == 0:
                    rut = alumno.rut
                    lista_rut = list(rut)
                    lista_rut.remove(".")
                    lista_rut.remove(".")
                    rut = "".join(lista_rut)
                    alumno.rut = rut
                elif error[1] == 1:
                    rut = alumno.rut
                    lista_rut = list(rut)
                    lista_rut.insert(8, "-")
                    rut = "".join(lista_rut)
                    alumno.rut = rut
            else:
                break

        while True:
            try:
                self.chequear_numero_alumno(alumno)

            except ValueError as err:
                error = err.args
                año_ingreso = alumno.ano_ingreso
                n_alumno = alumno.num_alumno
                carrera = alumno.carrera
                lista_año = list(año_ingreso)
                lista_año = lista_año[2:]
                lista_carrera = list(carrera)
                if carrera == "Ingenieria":
                    carrera = "63"
                else:
                    carrera = "61"
                lista_n_alumno = list(n_alumno)
                if error[1] == 0:
                    lista_n_alumno.pop()
                    lista_n_alumno.appens("J")
                elif error[1] == 1:
                    for i in range(len(lista_n_alumno)):
                        if lista_n_alumno[i].isdigit() == False and i != (
                                len(lista_n_alumno) - 1):
                            lista_n_alumno.remove(i)
                            lista_n_alumno.append("J")
                elif error[1] == 2:
                    lista_n_alumno.pop(0)
                    lista_n_alumno.pop(0)
                    lista_n_alumno.insert(0, lista_año[1])
                    lista_n_alumno.insert(0, lista_año[0])
                elif error[1] == 3:
                    lista_n_alumno.pop(2)
                    lista_n_alumno.pop(2)
                    lista_n_alumno.insert(2, lista_carrera[1])
                    lista_n_alumno.insert(2, lista_carrera[0])
                n_alumno = "".join(lista_n_alumno)
                alumno.num_alumno = n_alumno
            else:
                break

        while True:
            try:
                chequear_curso(alumno)

            except KeyError as err:
                error=err.args
                curso = alumno.curso
                if error[1]==0:
                    self.cursos[curso]={"1":[]}
                elif error[1]==1:
                    alumno.seccion="1"

            except ValueError as err:
                error=err.args
                curso = alumno.curso
                seccion = alumno.seccion
                if error[1]==0:
                    if seccion=="todas":
                        alumno.seccion="1"
                    else:
                        alumno.seccion=seccion[8]
                elif error[1]==1:
                    lista_curso = list(curso)
                    for i in range(len(lista_curso)):
                        if lista_curso[i] == " ":
                            lista_curso.pop(i)
                            curso="".join(lista_curso)
                            alumno.curso=curso
            else:
                break
        ################################################################
        ####################AQUI INSCRIBIR AL ALUMNO####################
        ################################################################


    def cargar_cursos(self, archivo_cursos):
        '''
        Carga los cursos iniciales en el DCCBanner. No deben hacer nada
        con este método.
        '''
        with open(archivo_cursos, 'r') as file:
            cursos = json.load(file)
            for nombre_curso, secciones in cursos.items():
                self.cursos[nombre_curso] = secciones

    def cargar_alumnos(self, archivo_alumnos):
        '''
        Para cada uno de los alumnos en file_path los carga al atributo
        self.alumnos
        '''
        with open(archivo_alumnos, 'r') as file:
            alumnos = csv.reader(file, delimiter=';')
            for line in alumnos:
                line = [attr.strip() for attr in line]
                self.alumnos.append(Alumno(*line))

    def cargar_datos(self, archivo_cursos, archivo_alumnos):
        '''
        Carga los datos de alumnos y cursos, en caso de fallar, captura la
        excepción y manda un mensaje explicando que falló.
        '''
        pass


if __name__ == '__main__':
    DCCBanner = DCCBanner()
    # Este try intenta cargar un archivo que no existe, por lo que el sistema
    # no se poblaría y debería entrar al except ErrorDatos. Lo que deben hacer
    # es buscar donde hacer raise de dicha excepción. Acá nada.
    try:
        DCCBanner.cargar_datos('cursos.json', 'hernan.jpg')
        DCCBanner.inscribir_alumnos()

    except ErrorDatos as ex:
        print(ex.message)

    finally:
        # Después puedes cambiar este alumnos.csv por big_alumnos.csv
        DCCBanner.cargar_datos('cursos.json', 'alumnos.csv')
        DCCBanner.inscribir_alumnos()
    # Lo siguiente es para debuggear. Para el archivo de datos más grande de
    # alumnos les recomendamos cambiar el print(alumno) por print(alumno.nombre)
    for curso, secciones in DCCBanner.cursos.items():
        print(f'Curso: {curso}\n')
        for seccion in secciones:
            print(f'Seccion {seccion}\n')
            alumnos = secciones[seccion]
            for alumno in alumnos:
                print(alumno)
        print('*' * 40)
