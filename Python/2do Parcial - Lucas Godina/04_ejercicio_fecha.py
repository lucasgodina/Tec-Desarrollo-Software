from datetime import datetime, timedelta

# Obtener la fecha y hora actual sin microsegundos, para luego darle formato DD/MM/AAAA HH:MM:SS
fecha_actual = datetime.now().replace(microsecond=0)
fecha_formateada = fecha_actual.strftime("%d/%m/%Y %H:%M:%S")
print("Fecha y hora actual:", fecha_formateada)

# Agregar 10 días a la fecha actual, para luego darle formato DD/MM/AAAA HH:MM:SS
fecha_futura = fecha_actual + timedelta(days=10)
fecha_futura_formateada = fecha_futura.strftime("%d/%m/%Y %H:%M:%S")
print("Fecha y hora en 10 días:", fecha_futura_formateada)
