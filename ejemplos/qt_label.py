import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout

def main():
    app = QApplication(sys.argv)

    # Crear la ventana principal
    window = QWidget()
    window.setWindowTitle('Ventana con QGridLayout')
    window.setGeometry(100, 100, 480, 280)

    # Crear un layout de cuadrícula
    grid = QGridLayout()

    # Crear etiquetas y añadirlas al layout de cuadrícula
    label1 = QLabel('Etiqueta 1')
    label2 = QLabel('Etiqueta 2')
    label3 = QLabel('Etiqueta 3')
    label4 = QLabel('Etiqueta 4')
    grid.addWidget(label1, 0, 0)  # Fila 0, Columna 0
    grid.addWidget(label2, 0, 1)  # Fila 0, Columna 1
    grid.addWidget(label3, 1, 0)  # Fila 1, Columna 0
    grid.addWidget(label4, 1, 1)  # Fila 1, Columna 1

    # Establecer el layout en la ventana
    window.setLayout(grid)

    # Mostrar la ventana
    window.show()

    # Ejecutar la aplicación
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()