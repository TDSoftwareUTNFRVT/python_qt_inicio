# instalar: pip install mysql-connector-python

import mysql.connector

# Conectar a la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='tu_usuario',
    password='tu_contraseña',
    database='mi_base_de_datos'
)

# Crear un cursor para interactuar con la base de datos
cursor = conexion.cursor()

# Crear una tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    edad INT
)
''')

# Insertar un registro
cursor.execute('''
INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)
''', ('Juan', 30))

# Guardar (commit) los cambios
conexion.commit()

# Consultar los registros
cursor.execute('SELECT * FROM usuarios')
filas = cursor.fetchall()
for fila in filas:
    print(fila)

# Cerrar la conexión
conexion.close()