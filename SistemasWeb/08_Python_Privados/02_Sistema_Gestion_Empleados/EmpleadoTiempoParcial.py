import Empleado


class EmpleadoTiempoParcial(Empleado.Empleado):
    def __init__(self, nombre, apellido, salario, horas_trabajadas_por_semana):
        super().__init__(nombre, apellido, salario)
        self.horas_trabajadas_por_semana = horas_trabajadas_por_semana

    def obtener_horas_trabajadas(self):
        return self.horas_trabajadas_por_semana
