# ✅ Creación de un array (lista)
numeros = [10, 20, 30, 40, 50]
print("Array original:", numeros)

# ✅ Acceso a elementos
print("Primer elemento:", numeros[0])       # 10
print("Último elemento:", numeros[-1])      # 50

# ✅ Modificación de elementos
numeros[2] = 99  # Cambia el tercer elemento (índice 2)
print("Array modificado:", numeros)

# ✅ Agregar elementos
numeros.append(60)
print("Array con nuevo elemento:", numeros)

# ✅ Eliminar elementos
numeros.remove(20)  # Elimina el valor 20
print("Array tras eliminar 20:", numeros)

# ✅ Recorrido del array
print("Recorriendo el array:")
for numero in numeros:
    print(numero)

# ✅ Recorrido con índice
print("Recorriendo con índices:")
for i in range(len(numeros)):
    print(f"Índice {i}: Valor {numeros[i]}")
