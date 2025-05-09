from enum import Enum

class SEMANA(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

# Recorre todos los elementos el enum: SEMANA
for dia in SEMANA:
    print(dia.name)


# Uso del enumerado
def es_dia_laboral(dia):
    if dia in (SEMANA.SABADO, SEMANA.DOMINGO):
        return False
    return True

# Ejemplo de uso
dia = SEMANA.LUNES
print(f"Día seleccionado: {dia.name} ({dia.value})")

if es_dia_laboral(dia):
    print("Es un día laboral.")
else:
    print("Es fin de semana.")
