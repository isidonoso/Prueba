########################################################################
#        Estas funciones las encontré en internet en la pagina         #
# https://recursospython.com/guias-y-manuales/drag-and-drop-con-pyqt-4/#
########################################################################

from os import path

from PyQt5.QtCore import QMimeData, Qt
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QApplication, QLabel, QFrame


class DropBox(QFrame):

    def __init__(self, parent):
        QFrame.__init__(self, parent)
        self.setAcceptDrops(True)  # Aceptar objetos
        self.setStyleSheet(
            path.join("sprites", "mapa", "towerDefense_tile231.png"))

    def dragEnterEvent(self, event):
        # Ignorar objetos arrastrados sin información
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        # Establecer el widget en una nueva posición
        pos = event.pos()
        self.label = event.source()
        self.label.setParent(self)
        self.label.setGeometry(0, 0, 30, 30)
        self.label.show()

        event.acceptProposedAction()


class DraggableLabel(QLabel):

    def __init__(self, parent):
        QLabel.__init__(self, parent)

    def mousePressEvent(self, event):
        # Inicializar el arrastre con el botón derecho
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        # Chequear que se esté presionando el botón derecho
        if not (event.buttons() and Qt.LeftButton):
            return

        # Verificar que sea una posición válida
        if ((event.pos() - self.drag_start_position).manhattanLength()
                < QApplication.startDragDistance()):
            return

        drag = QDrag(self)
        mime_data = QMimeData()

        # Establecer el contenido del widget como dato
        mime_data.setText(self.text())
        drag.setMimeData(mime_data)

        # Ejecutar la acción
        self.drop_action = drag.exec_(Qt.CopyAction | Qt.MoveAction)
