# ✅ Diccionario: Almacenamiento de datos clave-valor
contactos = {
    "Juan": "juan@example.com",
    "Ana": "ana@example.com",
    "Carlos": "carlos@example.com"
}

# Acceso a valores a través de claves
print("\nCorreo de Juan:", contactos["Juan"])

# Modificar un valor
contactos["Juan"] = "juan_nuevo@example.com"
print("\nNuevo correo de Juan:", contactos["Juan"])

# Agregar un nuevo par clave-valor
contactos["Pedro"] = "pedro@example.com"
print("\nLista de contactos actualizada:", contactos)

# Eliminar un elemento
del contactos["Carlos"]
print("\nLista de contactos después de eliminar a Carlos:", contactos)

# Recorrer el diccionario
print("\nRecorriendo el diccionario de contactos:")
for nombre, correo in contactos.items():
    print(f"Nombre: {nombre}, Correo: {correo}")

# ✅ Conjunto: Operaciones con conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Unión de conjuntos
union = conjunto1 | conjunto2
print("\nUnión de conjuntos:", union)

# Intersección de conjuntos
interseccion = conjunto1 & conjunto2
print("Intersección de conjuntos:", interseccion)

# Diferencia de conjuntos
diferencia = conjunto1 - conjunto2 #elementos que están en el conjunto1 pero no en el 2
print("Diferencia de conjuntos (conjunto1 - conjunto2):", diferencia)

# Verificar si un elemento está en un conjunto
if 3 in conjunto1:
    print("El 3 está en conjunto1.")
else:
    print("El 3 no está en conjunto1.")

# Agregar un nuevo elemento al conjunto
conjunto1.add(6)
print("Conjunto1 después de agregar un 6:", conjunto1)

# Eliminar un elemento del conjunto
conjunto1.remove(6)
print("Conjunto1 después de eliminar el 6:", conjunto1)
