import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox

def main():
    app = QApplication(sys.argv)

    # Cargar el archivo CSS
    with open("ejemplo2/css/styles.css", "r") as f:
        app.setStyleSheet(f.read())

    # Crear la ventana principal
    window = QWidget()
    window.setWindowTitle('Formulario de Inicio de Sesión')
    window.setGeometry(100, 100, 300, 150)

    # Crear un layout de cuadrícula
    grid = QGridLayout()

    # Crear etiquetas y campos de entrada
    label_mail = QLabel('Correo:')
    label_dni = QLabel('DNI:')
    input_mail = QLineEdit()
    input_dni = QLineEdit()

    # Añadir etiquetas y campos de entrada al layout
    grid.addWidget(label_mail, 0, 0)
    grid.addWidget(input_mail, 0, 1)
    grid.addWidget(label_dni, 1, 0)
    grid.addWidget(input_dni, 1, 1)

    # Crear y añadir el botón de inicio de sesión
    button_login = QPushButton('Iniciar Sesión')
    grid.addWidget(button_login, 2, 0, 1, 2)

    # Conectar el botón a una función
    button_login.clicked.connect(lambda: verificar_credenciales(input_mail.text(), input_dni.text()))

    # Establecer el layout en la ventana
    window.setLayout(grid)

    # Mostrar la ventana
    window.show()

    # Ejecutar la aplicación
    sys.exit(app.exec_())

def verificar_credenciales(mail, dni):
    # Aquí puedes añadir la lógica para verificar las credenciales
    if mail == "usuario@example.com" and dni == "12345678":
        QMessageBox.information(None, 'Éxito', 'Inicio de sesión exitoso')
    else:
        QMessageBox.warning(None, 'Error', 'Credenciales incorrectas')

if __name__ == '__main__':
    main()