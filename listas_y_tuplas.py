# ✅ Trabajando con Listas

# Creación de una lista
frutas = ["manzana", "plátano", "cereza", "uva"]
print("Lista original:", frutas)

# Modificar un elemento de la lista
frutas[1] = "mango"  # Cambiar "plátano" por "mango"
print("Lista después de modificar un elemento:", frutas)

# Agregar un nuevo elemento
frutas.append("kiwi")
print("Lista después de agregar un nuevo elemento:", frutas)

# Eliminar un elemento
frutas.remove("uva")
print("Lista después de eliminar un elemento:", frutas)

# Recorrer la lista
print("Recorriendo la lista de frutas:")
for fruta in frutas:
    print(fruta)

# ✅ Trabajando con Tuplas

# Creación de una tupla
dias = ("lunes", "martes", "miércoles", "jueves", "viernes")
print("\nTupla original:", dias)

# Acceso a un elemento de la tupla
print("Acceso a un elemento de la tupla:", dias[2])  # miércoles

# Tupla dentro de una lista
dias_lista = list(dias)  # Convertimos la tupla a lista para poder modificarla
dias_lista.append("sábado")
dias_lista.append("domingo")
print("Lista de días (después de modificar la tupla):", dias_lista)

# Tupla dentro de una lista de tuplas (complejo)
personas = [("Juan", 28), ("Ana", 22), ("Carlos", 35)]
print("\nLista de tuplas (personas):")
for persona in personas:
    nombre, edad = persona  # Desempaquetado de tupla
    print(f"{nombre} tiene {edad} años.")
