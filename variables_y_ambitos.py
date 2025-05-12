# Variable GLOBAL
x = 10

def funcion_global():
    global x  # Usamos la variable global 'x'
    x = 20  # Modificamos la variable global
    print(f"En funcion_global, x (global modificada): {x}")

def funcion_local():
    # Variable LOCAL en funcion_local
    x = 5
    print(f"En funcion_local, x (local): {x}")

def funcion_externa():
    # Definimos una variable no local
    y = 15
    
    def funcion_interna():
        nonlocal y  # Referencia a la variable 'y' fuera de esta función, pero dentro de funcion_externa
        y = 25  # Modificamos la variable no local
        print(f"En funcion_interna, y (nonlocal modificada): {y}")
    
    funcion_interna()
    print(f"En funcion_externa, y (después de la función interna): {y}")



def main():
    print(f"Valor de x (global antes de llamadas): {x}")
    
    # Llamada a las funciones para ver cómo afecta el ámbito
    funcion_global()  # Modifica la variable global 'x'
    funcion_local()  # Modifica la variable local 'x'
    funcion_externa()  # Modifica la variable no local 'y'
    
    # Verificamos el valor final de x
    print(f"Valor de x (global después de modificarse): {x}")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()
