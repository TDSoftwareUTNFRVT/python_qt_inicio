from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Home')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label_bienvenida = QLabel('¡Bienvenido a la pantalla principal!')
        layout.addWidget(self.label_bienvenida)

        self.setLayout(layout)