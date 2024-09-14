import sqlite3
import pathlib

def main():
    # Conectar a la base de datos (se creará si no existe)
    db_path = pathlib.Path(__file__).parent / 'productos.sqlite'
    conn = sqlite3.connect(db_path)

    # Crear un cursor
    cursor = conn.cursor()

    # Crear una tabla
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL)
    ''')

    # Confirmar los cambios
    conn.commit()

    insertar_producto(cursor, conn, 'Teclado', 25)
    insertar_producto(cursor, conn, 'Mouse', 18)
    insertar_producto(cursor, conn, 'Monitor', 300)
    insertar_producto(cursor, conn, 'Parlantes', 100)

    # Cerrar la conexión
    conn.close()

    print("Base de datos y tabla creadas exitosamente.")

def insertar_producto(cursor, conn, nombre, precio):
    cursor.execute('''
    INSERT INTO productos(nombre, precio)
    VALUES(?, ?)
    ''', (nombre, precio))
    conn.commit()

    
if __name__ == "__main__":
    main()