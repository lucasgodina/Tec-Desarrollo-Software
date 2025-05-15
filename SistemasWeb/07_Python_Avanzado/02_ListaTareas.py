"""
Crea una clase "ListaTareas" que contenga una lista de tareas pendientes.
Implementa métodos para agregar una tarea, marcar una tarea como
completada y mostrar todas las tareas
"""


class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append({"tarea": tarea, "completada": False})

    def marcar_completada(self, index):
        if 0 <= index < len(self.tareas):
            self.tareas[index]["completada"] = True
        else:
            print("Índice de tarea inválido.")

    def mostrar_tareas(self):
        for i, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"Tarea {i}: {tarea['tarea']} - {estado}")


# Ejemplo de uso
lista = ListaTareas()
lista.agregar_tarea("Hacer la compra")
lista.agregar_tarea("Estudiar Python")
lista.agregar_tarea("Limpiar la casa")
lista.mostrar_tareas()
lista.marcar_completada(1)
lista.mostrar_tareas()
