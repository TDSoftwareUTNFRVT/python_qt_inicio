import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

def main():
    app = QApplication(sys.argv)

    # Crear la ventana principal
    window = QWidget()
    window.setWindowTitle('Ventana con QVBoxLayout y QHBoxLayout')
    window.setGeometry(100, 100, 480, 280)

    # Crear un layout vertical
    vbox = QVBoxLayout()

    # Crear botones y añadirlos al layout vertical
    button1 = QPushButton('Botón 1')
    button2 = QPushButton('Botón 2')
    vbox.addWidget(button1)
    vbox.addWidget(button2)

    # Crear un layout horizontal
    hbox = QHBoxLayout()
    button3 = QPushButton('Botón 3')
    button4 = QPushButton('Botón 4')
    hbox.addWidget(button3)
    hbox.addWidget(button4)

    # Añadir el layout horizontal al layout vertical
    vbox.addLayout(hbox)

    # Establecer el layout en la ventana
    window.setLayout(vbox)

    # Mostrar la ventana
    window.show()

    # Ejecutar la aplicación
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()