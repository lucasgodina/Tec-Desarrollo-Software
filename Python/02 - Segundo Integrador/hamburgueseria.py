import tkinter as tk


def menu():
    correr = True
    while correr:
        print("Bienvenido a la Hamburguesas IT")
        encargado = input("Ingrese el nombre del encargad@: ")

        print(f"Hamburguesas IT")
        print(f"Encargad@: {encargado}")
        print("Recuerda, siempre hay que recibir al cliente con una sonrisa :)")

        print("1. Ingreso nuevo pedido")
        print("2. Cambio de encargado")
        print("3. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            cliente = input("Ingrese el nombre del cliente: ")
            cant_combo_s = int(input("Ingrese la cantidad de combos simples: "))
            cant_combo_d = int(input("Ingrese la cantidad de combos dobles: "))
            cant_combo_t = int(input("Ingrese la cantidad de combos triples: "))
            cant_flurby = int(input("Ingrese la cantidad de Flurbys: "))

            realizar_pedido()
        elif choice == "2":
            print("Cambiar encargado")
            # Aquí puedes agregar el código para hacer un pedido
            cambiar_encargado()
        elif choice == "3":
            print("Saliendo...")
            correr = False
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


def realizar_pedido():
    return


def cambiar_encargado():
    return


if __name__ == "__main__":
    # Llamar a la función menu
    menu()
