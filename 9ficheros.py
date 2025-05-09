with open("./fichero.txt", "w") as archivo:
    archivo.write("Este es un fichero .txt")
    archivo.write("\nArchivo de prueba para el ejercicio.")

with open("./fichero.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# Lectura línea por línea (simulación de feof)
with open("./fichero.txt", "r") as archivo:
    while True:
        linea = archivo.readline()
        if not linea:  # Esto equivale a feof: si no hay más contenido, salir
            break
        print("Leyendo línea:", linea.strip())

# Recorrer fichero con bucle for
with open("./fichero.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip()) 