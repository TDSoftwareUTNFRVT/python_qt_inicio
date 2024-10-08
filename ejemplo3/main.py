import sys
import os
from PyQt5.QtWidgets import QApplication
from interfaz.ventana_principal import VentanaPrincipal

def main():
    app = QApplication(sys.argv)

    # Construir la ruta absoluta del archivo CSS
    script_dir = os.path.dirname(os.path.abspath(__file__))
    css_path = os.path.join(script_dir, 'css', 'styles.css')

    # Cargar el archivo CSS
    with open(css_path, "r") as f:
        app.setStyleSheet(f.read())

    # Crear y mostrar la ventana principal
    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()