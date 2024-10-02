import datetime


def menu():
    running = True
    while running:
        print("Bienvenido a la Hamburguesas IT")
        encargado = input("Ingrese el nombre del encargad@: ")

        print(f"Hamburguesas IT")
        print(f"Encargad@: {encargado}")
        print("Recuerda, siempre hay que recibir al cliente con una sonrisa :)")

        print("1. Ingreso nuevo pedido")
        print("2. Cambio de encargado")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cliente = input("Ingrese el nombre del cliente: ")
            cant_combo_s = int(input("Ingrese la cantidad de combos simples: "))
            cant_combo_d = int(input("Ingrese la cantidad de combos dobles: "))
            cant_combo_t = int(input("Ingrese la cantidad de combos triples: "))
            cant_flurby = int(input("Ingrese la cantidad de Flurbys: "))
            total = (
                cant_combo_s * 5 + cant_combo_d * 6 + cant_combo_t * 7 + cant_flurby * 2
            )
            print(f"Total a pagar: ${total}")
            abona = input(int(f"El cliente abona con: $"))
            vuelto = abona - total

            print(f"Pedido para {cliente}")
            print(f"Total a pagar: ${total}")
            print(f"Abona con: ${abona}")
            print(f"Vuelto: ${vuelto}")
            confirma = input("¿Desea confirmar el pedido? (S/N): ")

            while confirma.lower != "s" and confirma.lower != "n":
                print("Opción no válida. Por favor, intente de nuevo.")
                confirma = input("¿Desea confirmar el pedido? (S/N): ")

            if confirma.lower == "s":
                pedido()
            elif confirma.lower == "n":
                print("Pedido cancelado")

        elif opcion == "2":
            print("Cambiando encargado..")
            encargado = input("Ingrese el nombre del nuevo encargad@: ")

        elif opcion == "3":
            print("Saliendo...")
            running = False
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


def pedido(cliente, cant_combo_s, cant_combo_d, cant_combo_t, cant_flurby, total):
    print(f"Pedido")


# Llamado a la función menu
if __name__ == "__main__":
    menu()
