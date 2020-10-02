# Tarea 2: DCCivil War :school_satchel:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea este, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

Cada componente que debe tener HP lo contiene como entidad pero no se descuenta,
la barra de progreso del programa esta, pero no funciona.

El personaje no recolecta monedas, y estas no aparecen en el juego, si bien creé 
la función para que aparezcan (línea 225), al ocuparla (linea 200), comienza a 
"generarlas"pero no permite que el programa continue y queda en loop.

El programa no genera más de una ronda, ya que nunca se eliminan a los enemigos
y no implementé los cheats.

Todas las entidades respetan sus respectivos obstaculos, el movimiento 
del personaje principal solo funciona si esque se esta con SPEED=1, y el
movimiento de los enemigos no es tan fluido como corresponda, ya que si se
intenta mover a un espacio que es ocupado por un obstaculo, entonces se queda 
donde esta y no puede volver a entrar a los sitios de inicio. Aparte de eso su 
dirección de movimiento e imagen no se corresponden entre si, pero se puede 
arreglar cambiando lineas:

Cambiar las lineas:

* 82 por ""normal_18")).transformed(QTransform().scale(-1, 1)))"

* 90-91 por ""normal_45")))"

* 100 por ""normal_18")))"

* 109 por ""normal_15")))"

* 118 por ""normal_18")).transformed(QTransform().scale(-1, 1)))"

* 126-127 por ""normal_38")))"

* 136 por ""normal_18")))"

*  145 por ""normal_05")))"

* 228 por ""kamikaze_18")).transformed(QTransform().scale(-1, 1)))"

* 236-237 por ""kamikaze_09")))"

* 246 por ""kamikaze_18")))"

* 255 por ""kamikaze_30")))"

* 264 por ""kamikaze_17")).transformed(QTransform().scale(-1, 1)))"

* 272-273 por ""kamikaze_05")))"

* 282 por ""kamikaze_17")))"

* 291 por ""kamikaze_17")))"

Todos los botones de las tres ventanas funcionan, se descuentan las monedas en 
las compras y las ventanas si se ocupan correctamente no se caen.

Para tener a consideracion si se cierra la ventana del juego mientras se esta
jugando y luego se intenta comenzar denuevo desde la ventana inicial, la ventana
se caerá, no así, si esque se cierra sesión correctamente.

La barra de progreso del HP de la base esta implementada de la linea 92 a la 96,
pero si se implementa el programa se ralentiza mucho.

El programa se cae luego de un rato solo cuando los enemigos estan funcionando,
si no estan caminando, las ventanas no se cierran y a menor velocidad de los
enemigos, mayor será la duración de la ventana.

### Cosas implementadas y no implementadas :white_check_mark: :x:

* Parte <2>: Hecha completa
* Parte <5<sub>1</sub>>: Me faltó que los enemigos ataquen la base, torres que si se
intentan mover a un lugar que no pueden, lo hagan en otra dirección (si intenta 
ocupar un lugar prohibido, entonces se queda quieto hasta que le toque 
moverse denuevo), disminuir su HP, que mueran, y liberar monedas al hacerlo
* Parte <5<sub>2</sub>>: Me faltó que recolecara monedas
* Parte <5<sub>3</sub>>: Solo esta instanciada y cambia según el enemigo 
correspondiente la imagen que aparece.
* Parte <5<sub>4</sub>>: Existen las dos entidades y se crean sus respectivas
instancias al momento de creearlas, tienen un en monedas que se respeta cuando
se intenta comprar y se pueden colocar correctamente en el mapa, pero no atacan 
y no mueren.
* Parte <6>: Esta la clase Moneda ```Monedas.py```, pero no se 
ocupa en el programa principal, ya que al hacerlo, este entra en loop.
* Parte <7>: Hecha completa, esta el botón y se implementa a cada una de las
torres, pero no se muestra graficamente, ya que las torres no atacan.
* Parte <8>: Hecha completa, pero el programa solo muestra el que este primero,
en la carpeta Mapa, porque se lee así y nunca cambia de ronda, pero si se cambia
ese archivo, el programa funciona igual, ya que lee y se adapta a cualquier tipo
de mapa
* Parte <9>: Aquí lo único que hice fue leer el archivo ```puntajes.txt``` y que
aparezca en la ventana inicial.
* Parte <10<sub>1</sub>>: Hecha completa
* Parte <10<sub>2</sub>>: Hecha completa
* Parte <10<sub>3.1</sub>>: Hecha completa, pero no funcion la barra de progreso
* Parte <10<sub>3.2</sub>>: Solo comienza al apretar el botón de "Empezar ronda",
se inhabilitan los botones de la parte inicial, estan las monedas totales con
las que comienzan según un parametro MONEDAS_I, y se van descontando según las 
compras, aparece la ronda en la que se encentra solo porque se puede jugar 1 
ronda, el botón de pausa funciona correctamente y se ve en la pantalla.
* Parte <10<sub>3</sub>>: Hecha completa, excepto porque los kamikazes no
explotan y los enemigos no cambian de movimiento al atacar la base porque no lo 
hacen. Y si los enemigos intentan avanzar a un lugar prohibidos estos no se
mueven hasta que les toque moverse denuevo, y en el programa aparece incorrecto
el movimiento y la dirección a la que miran los enemigos, pero ya indiqué arriba
como arreglarlo.
* Parte <11>: No hice nada
* Parte <12>: Hecha completa
* Parte <13>: Hecha completa


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```Ventana.py```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5.QtWidgets```-> ```QLabel```,```QWidget```,```QApplication```,
```QPushButton```,```QLineEdit```,```QRadioButton```,```QVBoxLayout```,
```QHBoxLayout```,```QProgressBar```,```QGridLayout```,```QFrame```
2. ``` os ```-> ```getcwd```,```listdir```,```path``` 
3. ``` random ```-> ```randint``` 
4. ```PyQt5.QtGui```-> ```QPixmap```,```QTransform```,```QDrag```
5. ``` PyQt5.QtCore ```-> ```pyqtSignal```,```Qt```,```QThread```,```QMimeData``` 
6. ``` time ```-> ```sleep``` 


...

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```Ventana.py```-> Contine a ```Menu```
2. ```Mapas.py```-> Hecha para leer los archivos de los mapas y puntajes
3. ```parametros.py```-> Hecha para contener todos los parametroc ocupados
4. ```Resultados.py```-> Contiene a ```Resultado```
5. ```Eventos.py```-> Contiene a ```Mover```,```MoverEntidad```
6. ```Jugador.py```-> Contiene a ```Personaje```
7. ```Enemigos.py```-> Contiene a ```EnemigoNormal```,```EnemigoKamikaze```
8. ```Torres.py```-> Contiene a ```Racimo```,```Francotirador```
9. ```Monedas.py```-> Contiene a ```Moneda```
10. ```Base.py```-> Contiene a ```EdificioBase```
11. ```DragDrop.py```-> Contiene a ```DropBox```,```DraggableLabel```



## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Los enemigos aparecen todos juntos, ya que se daba la opción
2. Se incluye un parametro inicial de MONEDAS_I que es el dinero
que tiene el usuario al comenzar y con el que puede comprar torres
y sus mejoras correspondientes
3. Por comodidad nunca se cierra la pantalla inicial, para que cuando intente
cerrar sesión sea más facil, pero se limpian los parametros que estaban 
ingresados
4. No intenta cerrar la ventana con los enemigos caminando e intenta 
iniciar sesión luego de hacer eso, ya que el programa se cae

-------

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. (https://recursospython.com/guias-y-manuales/drag-and-drop-con-pyqt-4/): este
 hace que funcione el drag y drop para colocar las torres y está implementado 
 en el archivo ```DragDrop.py``` es prácticamente todo el archivo, solo le 
 cambié un par de lineas y lo que hace es crear las funciones necesarias para el
 arrastre de las torres y que se puedan colocar en el lugar correcto



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).