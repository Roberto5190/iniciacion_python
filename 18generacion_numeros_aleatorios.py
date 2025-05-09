import random

# Numero aleatorio entero entre 1 y 10
entero = random.randint(1, 10)
print("Numero entero aleatorio entre 1 y 10: ", entero)

# Numero decimal aleatorio entre 0 y 1
decimal = random.random()
print("Numero decimal aleatorio entre 0 y 1: ", decimal)

# Numero entero aleatorio entre 5 y 9, el 10 no se incluye
entero_rango = random.randrange(5, 10)
print("Numero entero aleatorio entre 5 y 9: ", entero_rango)

# Numero decimal aleatorio entre 5 y 10
decimal_rango = random.uniform(5, 10)
print("Numero decimal aleatorio entre 5 y 10: ", decimal_rango)

# # Elegir un elemento aleatorio de una lista
opciones = ["piedra", "papel", "tijera"]
eleccion = random.choice(opciones)
print("Elección aleatoria de de una lista: ", eleccion)




# SIMULACIÓN LANZAMIENTO DE UN DADO 
resultados = {i : 0 for i in range(1, 7)}

for _ in range(100):
    lanzamiento = random.randint(1, 6)
    resultados[lanzamiento] += 1

print("Lanzamiento del dado: ")
for cara, veces in resultados.items(): # for clave, valor in resultados.items() //.items() recorre todas las clave:valor del diccionario
    print(f"Cara {cara}: {veces} veces ")