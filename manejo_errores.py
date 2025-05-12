# MANEJO DE EXCEPCIONES
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except TypeError:
        print("Error: Ambos valores deben ser numéricos.")
    else:
        print(f"El resultado de la división es: {resultado}")
    finally:
        print("Operación finalizada.")

# Probando el programa con diferentes entradas
dividir(10, 2)  # División válida
dividir(10, 0)  # Error: División por cero
dividir(10, "a")  # Error: Tipo incorrecto


# LANZAMIENTO Y CAPTURA DE ERRORES
def verificar_edad(edad):
    if edad < 18:
        raise ValueError("La edad debe ser al menos 18 años.")
    else:
        print("Edad válida.")

# Probando con diferentes valores
try:
    verificar_edad(15)  # Error, menos de 18 años
except ValueError as e:
    print(f"Error: {e}")



# MANEJO EXCEPCIONES, LANZAMIENTO Y CAPTURA ERRORES
def calcular_promedio(lista):
    if not lista:  # Comprobamos si la lista está vacía
        raise ValueError("La lista no puede estar vacía.")
    return sum(lista) / len(lista)

try:
    # Intentamos calcular el promedio de una lista vacía
    promedio = calcular_promedio([])
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"El promedio es: {promedio}")
finally:
    print("Operación finalizada.")
