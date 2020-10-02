# Tarea 3: Timbitiche :school_satchel:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea este, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

Mi programa funciona el iniciar sesión, guardar datos, abrir salas, cargar fotos y guardarlas, aunque si hay imagenes guardadas de un usuario no las muestra.

Se hace el filtro dibujo.

Funcionan los chats pero no el comando chao.

Pueden entrar a las salas y estas iran aumentando en numero de participantes, pero no baja el numero si esque alguien sale de la sala, no desaparece de la lista de sala si queda sin participantes, ni limita
el ingreso de participantes.


No realice ningun bonus.


El juego en si no funciona ni aparece,

### Cosas implementadas y no implementadas :white_check_mark: :x:

* Parte <4<sub></sub>>: Hecha completa
* Parte <4<sub>1</sub>>: Hecha completa
* Parte <4<sub>2.1</sub>>: Hecha completa
* Parte <4<sub>2.2</sub>>: Hecha completa
* Parte <5<sub>1</sub>>: Hecha completa
* Parte <5<sub>2</sub>>: Hecha completa
* Parte <5<sub>3</sub>>: Me falto implementar que si habia una foto guardada por el usuario apareciera al iniciar sesión, limitar a 15 el máximo de usuarios por sala, y que si alguien salia de la sala, dismiuyera la cantidad de usuarios en todas las salas de espera
* Parte <5<sub>3.1</sub>>: Hecha completa
* Parte <5<sub>3.2</sub>>: Me faltó asignar un nuevo jefe si esque el actual se va y la cuenta regresiva si el jefe decide iniciar partida
* Parte <5<sub>3.3</sub>>: No esta implementada aunque igual estan los datos N y M en el server/parametros.json
* Parte <5<sub>4</sub>>: Me faltó que se registrara todo lo que ocurria en las salas, el comando /chao y a veces salen mensajes dobles
* Parte <6<sub></sub>>: Hecha completa
* Parte <7<sub></sub>>: Hecha completa
* Parte <8<sub></sub>>: Hecha completa
* Parte <10<sub></sub>>: No realicé ningun bonus



## Ejecución :computer:
Los módulos principales de la tarea a ejecutar son  ```main.py``` de la carpeta server y ```main.py``` de la carpeta client


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```math```-> ```sqrt```
2. ```zlib```-> ```compress``` , ```crc32```
3. ```pixel_collector```-> ```get_pixels``` 
4. ```json```
5. ```socket```
6. ```sys```
7. ```threading```-> ```th```
8. ```time```-> ```sleep```
9. ```PyQt5.QtCore```-> ```pyqtSignal```, ```Qt```
10. ```PyQt5.QtWidgets```-> ```QGraphicsObject```, ```QApplication```, ```QWidget```, ```QLabel```, ```QLineEdit```, ```QHBoxLayout```,```QVBoxLayout```, ```QPushButton```, ```QScrollArea```, ```QListWidget```, ```QDialog```, ```QFileDialog```
11. ```PyQt5.QtGui```-> ```QPixmap```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```Imagenes```-> De la carpeta Server que contine a ```FiltroDibujo```, ```GuardarImagen```, (ser general, tampoco es necesario especificar cada una)...
2. ```Imagenes```-> De la carppeta CLient que contiene a ```GuardarImagen```
3. ```Eventos``` -> Contiene a ```Enviar```, ```Imagen```
4. ```Main```-> De la carpeta Client que contiene a ```Cliente```
5. ```Main``` -> De a carpeta Server que contiene a ```Servidor```
6. ```FronEnd``` -> Contiene a ```VentanaIngresoUsuario```, ```VentanaSalas```, ```Juego```
7. ```Usuario``` -> Contiene a ```Leer```, ```Escribir```, ```Usuario```
8. ```Prueba``` -> Este modulo es una replica del client/Main.py que ocupaba para ver si funcionaba el programa, pero no se si esta con la ultima actualización del Main
9. ```Salas``` -> Contiene a ```Sala```


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Supuse que no se fuerza el cierre de ninguna ventana del interfaz ya que se cae el problema, y para eso se implementó un botón de 'salir' en cada ventana.
2. El nombre del usuario no contendrá comas "," , puntos "." o espacios " "
3. Si se presiona el botón de 'cargar imagen' se elegirá una imagen, no se cerrará sin haberlo hecho, ya que se cae el programa
4. Solo se utilizan imagenes png como se indicó en una issue.
5. Al cargar la imagen se demorá un poco, y en esa espera no se presiona ninguna parte de la interfaz, porque a veces el programa se cae el hacer eso.

## Referencias de código externo :book:


## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).