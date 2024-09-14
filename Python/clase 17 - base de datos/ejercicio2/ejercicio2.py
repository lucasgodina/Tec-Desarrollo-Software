import sqlite3

def conectar_bd():
    return sqlite3.connect('productos.sqlite')

def crear_tabla(conexion):
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre TEXT NOT NULL,
                       precio REAL NOT NULL)''')
    conexion.commit()

def agregar_producto(conexion):
    cursor = conexion.cursor()
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombre, precio))
    conexion.commit()
    print("Producto agregado exitosamente.")

def ver_productos(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    if productos:
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}")
    else:
        print("No hay productos en la base de datos.")

def menu(conexion):
    while True:
        print("\nMenu:")
        print("1- Agregar productos")
        print("2- Ver productos")
        print("3- Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_producto(conexion)
        elif opcion == '2':
            ver_productos(conexion)
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def main():
    conexion = conectar_bd()
    crear_tabla(conexion)
    menu(conexion)
    conexion.close()

if __name__ == "__main__":
    main()