import os
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QRadioButton, QButtonGroup, QFileDialog, QMessageBox)

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Seleccionar Archivos')
        self.setGeometry(100, 100, 400, 200)

        # Crear un layout de cuadrícula
        grid = QGridLayout()

        # Crear etiquetas y campos de entrada
        label_buscar = QLabel('Buscar por nombre:')
        self.input_buscar = QLineEdit()

        # Crear radio buttons para seleccionar la extensión
        self.radio_pdf = QRadioButton('PDF')
        self.radio_xlsx = QRadioButton('XLSX')
        self.radio_txt = QRadioButton('TXT')
        self.radio_py = QRadioButton('PY')
        self.radio_doc = QRadioButton('DOC')

        # Agrupar los radio buttons
        self.radio_group = QButtonGroup()
        self.radio_group.addButton(self.radio_pdf)
        self.radio_group.addButton(self.radio_xlsx)
        self.radio_group.addButton(self.radio_txt)
        self.radio_group.addButton(self.radio_py)
        self.radio_group.addButton(self.radio_doc)

        # Crear y añadir el botón de seleccionar archivo
        self.btn_seleccionar = QPushButton('Seleccionar Archivo')
        self.btn_seleccionar.clicked.connect(self.seleccionar_archivo)

        # Añadir widgets al layout
        grid.addWidget(label_buscar, 0, 0)
        grid.addWidget(self.input_buscar, 0, 1, 1, 3)
        grid.addWidget(self.radio_pdf, 1, 0)
        grid.addWidget(self.radio_xlsx, 1, 1)
        grid.addWidget(self.radio_txt, 1, 2)
        grid.addWidget(self.radio_py, 1, 3)
        grid.addWidget(self.radio_doc, 1, 4)
        grid.addWidget(self.btn_seleccionar, 2, 0, 1, 5)

        # Configurar el layout en la ventana
        self.setLayout(grid)

    def seleccionar_archivo(self):
        opciones = QFileDialog.Options()
        opciones |= QFileDialog.ReadOnly

        # Obtener la extensión seleccionada
        extension = ''
        if self.radio_pdf.isChecked():
            extension = 'PDF (*.pdf)'
        elif self.radio_xlsx.isChecked():
            extension = 'XLSX (*.xlsx)'
        elif self.radio_txt.isChecked():
            extension = 'TXT (*.txt)'
        elif self.radio_py.isChecked():
            extension = 'PY (*.py)'
        elif self.radio_doc.isChecked():
            extension = 'DOC (*.doc)'

        # Abrir el cuadro de diálogo para seleccionar archivo
        archivo, _ = QFileDialog.getOpenFileName(self, 'Seleccionar Archivo', '', extension, options=opciones)
        if archivo:
            QMessageBox.information(self, 'Archivo Seleccionado', f'Has seleccionado: {archivo}')