import datetime

def manejar_fechas():
    # 1. Obtener la fecha y hora actuales
    fecha_hora_actual = datetime.datetime.now()  # Fecha y hora actuales
    print(f"Fecha y hora actuales: {fecha_hora_actual}")

    # 2. Crear una fecha específica
    fecha_especifica = datetime.datetime(2025, 12, 25)  # 25 de diciembre de 2025
    print(f"Fecha específica (Navidad 2025): {fecha_especifica}")

    # 3. Formatear la fecha
    fecha_formateada = fecha_hora_actual.strftime("%d/%m/%Y %H:%M:%S")
    print(f"Fecha y hora formateada: {fecha_formateada}")

    # 4. Calcular la diferencia entre dos fechas
    fecha_futura = datetime.datetime(2025, 12, 31)
    diferencia = fecha_futura - fecha_hora_actual  # Resta entre fechas
    print(f"Diferencia entre fechas (en días): {diferencia.days} días")

    # 5. Realizar operaciones con fechas (sumar y restar días)
    # Sumar 10 días a la fecha actual
    nueva_fecha = fecha_hora_actual + datetime.timedelta(days=10)
    print(f"Fecha después de sumar 10 días: {nueva_fecha}")

    # Restar 5 días a la fecha actual
    fecha_resta = fecha_hora_actual - datetime.timedelta(days=5)
    print(f"Fecha después de restar 5 días: {fecha_resta}")

# Llamar a la función
manejar_fechas()
