"""
Crea una clase "CuentaBancaria" con atributos como número de cuenta y
saldo. Implementa métodos para depositar y retirar dinero, y muestra el
saldo actual.
"""


class CuentaBancaria:
    def __init__(self, numero_cuenta):
        self.numero_cuenta = numero_cuenta
        self.saldo = 0

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito realizado: {cantidad}. Saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= cantidad
            print(f"Retiro realizado: {cantidad}. Saldo actual: {self.saldo}")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")


# Ejemplo de uso
cuenta = CuentaBancaria("30580279")
cuenta.depositar(1000)
cuenta.retirar(500)
cuenta.retirar(1500)
cuenta.mostrar_saldo()
