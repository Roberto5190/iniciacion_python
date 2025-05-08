# Función sin parámetros
def saludar():
    print("¡Hola, bienvenido a las funciones en Python!")

# Función con parámetros
def suma(a, b):
    return a + b

# Función con parámetros por referencia (modificando la lista dentro de la función)
def agregar_elemento(lista, elemento):
    lista.append(elemento)  # Modifica la lista directamente (por referencia)

# Función con parámetros por valor (trabajando con números)
def modificar_numero(numero):
    numero = 10  # Cambia el valor localmente, pero no afecta al argumento original
    print(f"Valor dentro de la función: {numero}")

# Procedimiento (una función que no retorna valor)
def imprimir_mensaje(mensaje):
    print(mensaje)





def main():
    # Ejemplo 1: Función sin parámetros
    saludar()

    # Ejemplo 2: Función con parámetros
    resultado = suma(5, 3)
    print(f"El resultado de la suma es: {resultado}")

    # Ejemplo 3: Parámetros por referencia
    lista_original = [1, 2, 3]
    agregar_elemento(lista_original, 4)  # La lista se modifica dentro de la función
    print(f"Lista después de agregar un elemento: {lista_original}")

    # Ejemplo 4: Parámetros por valor
    numero_original = 5
    modificar_numero(numero_original)  # El valor de numero_original no cambia
    print(f"Valor fuera de la función: {numero_original}")

    # Ejemplo 5: Procedimiento (sin retorno de valor)
    imprimir_mensaje("Este es un mensaje sin valor de retorno.")


# Ejecutar la función principal
if __name__ == "__main__":
    main()
