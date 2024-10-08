import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host='localhost',
        user='tu_usuario',
        password='tu_contraseña',
        database='mi_base_de_datos'
    )

def verificar_usuario(usuario, contraseña):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s', (usuario, contraseña))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()
    return resultado is not None