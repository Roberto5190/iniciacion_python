# LECTURA Y ESCRITURA

# Escribir en un archivo
with open("ejemplo.txt", "w") as archivo:
    archivo.write("Hola, este es un archivo de ejemplo.\n")
    archivo.write("Python es muy útil para interactuar con el sistema operativo.\n")

# Leer el archivo
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)



# NAVEGACIÓN POR DIRECTORIOS
import os

# Ver el directorio actual
print("Directorio actual:", os.getcwd())
arch = os.listdir()
print("Archivos del directorio actual: ", arch)

# Cambiar de directorio
os.chdir("../")

# Listar los archivos y directorios en el directorio actual
archivos = os.listdir()
print("Archivos en el directorio:", archivos)

