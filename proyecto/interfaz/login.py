from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from database.db import verificar_usuario
from interfaz.home import Home

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Inicio de Sesión')
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.label_usuario = QLabel('Usuario:')
        self.input_usuario = QLineEdit()
        self.label_contraseña = QLabel('Contraseña:')
        self.input_contraseña = QLineEdit()
        self.input_contraseña.setEchoMode(QLineEdit.Password)

        self.btn_login = QPushButton('Iniciar Sesión')
        self.btn_login.clicked.connect(self.iniciar_sesion)

        layout.addWidget(self.label_usuario)
        layout.addWidget(self.input_usuario)
        layout.addWidget(self.label_contraseña)
        layout.addWidget(self.input_contraseña)
        layout.addWidget(self.btn_login)

        self.setLayout(layout)

    def iniciar_sesion(self):
        usuario = self.input_usuario.text()
        contraseña = self.input_contraseña.text()

        if verificar_usuario(usuario, contraseña):
            self.home = Home()
            self.home.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Error', 'Usuario o contraseña incorrectos')