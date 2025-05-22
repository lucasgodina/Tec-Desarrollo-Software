import Empleado


class EmpleadoTiempoCompleto(Empleado.Empleado):
    def __init__(self, nombre, apellido, salario, bono_anual):
        super().__init__(nombre, apellido, salario)
        self.bono_anual = bono_anual

    def obtener_bono_anual(self):
        return self.bono_anual

    def calcular_salario_total(self):
        return super().calcular_salario_total() + self.bono_anual
