

# CADENA DE CARACTERES
def manipular_cadenas():
    # Entrada del usuario
    texto = input("Introduce una cadena de texto: ")

    # 1. Concatenación
    cadena_adicional = " es genial"
    texto_completo = texto + cadena_adicional
    print(f"\nConcatenación: {texto_completo}")

    # 2. Slicing (obtener subcadenas)
    subcadena = texto[1:5]  # Desde el índice 1 hasta el 5 (sin incluir el índice 5)
    print(f"Slicing (subcadena de la posición 1 a la 5): {subcadena}")

    # 3. Conversión de mayúsculas y minúsculas
    texto_mayusculas = texto.upper()
    texto_minusculas = texto.lower()
    print(f"Texto en mayúsculas: {texto_mayusculas}")
    print(f"Texto en minúsculas: {texto_minusculas}")

    # 4. Buscar una subcadena
    subcadena_buscar = input("\n¿Qué palabra quieres buscar en la cadena? ")
    if subcadena_buscar in texto:
        print(f"La palabra '{subcadena_buscar}' se encuentra en la cadena.")
    else:
        print(f"La palabra '{subcadena_buscar}' no se encuentra en la cadena.")

    # 5. Reemplazo de texto
    palabra_reemplazar = input("\n¿Qué palabra deseas reemplazar? ")
    nueva_palabra = input("¿Por qué palabra quieres reemplazarla? ")
    texto_reemplazado = texto.replace(palabra_reemplazar, nueva_palabra)
    print(f"Texto después del reemplazo: {texto_reemplazado}")

    # 6. Eliminar espacios en blanco
    texto_sin_espacios = texto.strip()  # Elimina los espacios al principio y al final
    print(f"Texto sin espacios al principio y al final: '{texto_sin_espacios}'")


# Llamamos a la función
manipular_cadenas()
