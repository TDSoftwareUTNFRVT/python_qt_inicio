import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

def main():
    app = QApplication(sys.argv)

    # Crear la ventana principal
    window = QWidget()
    window.setWindowTitle('Ventana con QGridLayout')
    window.setGeometry(100, 100, 480, 280)

    # Crear un layout de cuadrícula
    grid = QGridLayout()

    # Crear botones y añadirlos al layout de cuadrícula
    button1 = QPushButton('Botón 1')
    button2 = QPushButton('Botón 2')
    button3 = QPushButton('Botón 3')
    button4 = QPushButton('Botón 4')
    grid.addWidget(button1, 0, 0)  # Fila 0, Columna 0
    grid.addWidget(button2, 0, 1)  # Fila 0, Columna 1
    grid.addWidget(button3, 1, 0)  # Fila 1, Columna 0
    grid.addWidget(button4, 1, 1)  # Fila 1, Columna 1

    # Establecer el layout en la ventana
    window.setLayout(grid)

    # Mostrar la ventana
    window.show()

    # Ejecutar la aplicación
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()