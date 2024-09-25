import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

def main():
    app = QApplication(sys.argv)

    # Crear la ventana principal
    window = QWidget()
    window.setWindowTitle('Ventana Simple')
    window.setGeometry(100, 100, 480, 280)

    # Crear un botón
    button = QPushButton('Presionar', window)
    button.clicked.connect(lambda: print('Botón presionado'))

    # Personalizar el botón
    button.setText('Nuevo Texto')
    button.setFixedSize(150, 50)
    button.setFont(QFont('Arial', 14))
    button.setStyleSheet("""
        QPushButton {
            background-color: #0000FF; /* Azul */
            border: none;
            color: white;
            padding: 15px;
            text-align: center;
            font-size: 16px;
            margin: 4px 2px;
        }
        QPushButton:hover {
            background-color: #45a049; /* Verde más oscuro */
        }
    """)

    # Crear un layout y añadir el botón
    layout = QVBoxLayout()
    layout.addWidget(button)
    layout.setAlignment(button, Qt.AlignCenter)  # Centrar el botón en el layout
    window.setLayout(layout)

    # Mostrar la ventana
    window.show()

    # Ejecutar la aplicación
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()