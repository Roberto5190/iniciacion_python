# 1. Entero (int)
entero = 10
print("Tipo: Entero (int)")
print(f"Valor: {entero}")
print("Dominio: Enteros, pueden ser negativos, cero o positivos.")
print("Operadores: +, -, *, /, %, //, **")
print(f"Identificador: {type(entero)}\n")

# 2. Decimal (float)
decimal = 5.57
print("Tipo: Decimal (float)")
print(f"Valor: {decimal}")
print("Dominio: numero decimal, puede ser negativo, positivo, infinito")
print("Operadores: +, -, *, /, %, //, ** ")
print(f"Identificador: {type(decimal)}\n")

# 3. String (str)
cadena = "cadena de caracteres"
print("Tipo: (string)")
print(f"Valor: {cadena}")
print("Dominio: cualquier tipo de cadena de caracteres")
print("Operadores: concatenar (+), repetición (*), añadir (+=)")
print(f"Identificador: {type(cadena)}\n")

# 4. Booleano (bool)
booleano = True
print("Tipo: (bool)")
print(f"Valor: {booleano}")
print("Dominio: True o False")
print("Operadores: and, or, not")
print(f"Identificador: {type(booleano)}\n")

# 5. Lista
lista = ["Hola", 2, True]
print("Tipo: (list)")
print(f"Valor: {lista}")
print("Dominio: secuencia indexada por indice, pueden incluir cualquier tipo de dato. ")
print("Operadores: + (concatenación), * (repetición), len(), append(), remove()")
print(f"Identificador: {type(lista)}\n")

# 6. Tupla (tuple)
tupla = (1, 2, 3, 4)
print("Tipo: Tupla (tuple)")
print(f"Valor: {tupla}")
print(f"Dominio: Secuencia ordenada de elementos, es inmutable.")
print(f"Operadores: + (concatenación), * (repetición), len()")
print(f"Identificador: {type(tupla)}\n")

# 7. Diccionario (dict)
diccionario = {'nombre': 'Antonio', 'edad': 45}
print("Tipo: Diccionario (dict)")
print(f"Valor: {diccionario}")
print(f"Dominio: Colección de pares clave-valor.")
print(f"Operadores: keys(), values(), items(), get()")
print(f"Identificador: {type(diccionario)}\n")

# 8. Conjunto (set)
conjunto = {1, 2, 3, 4}
print("Tipo: Conjunto (set)")
print(f"Valor: {conjunto}")
print(f"Dominio: Colección de elementos únicos no ordenados.")
print(f"Operadores: union(), intersection(), difference(), add(), remove()")
print(f"Identificador: {type(conjunto)}\n")

# 9. Enumerados (Enumerations)
from enum import Enum

class Estado(Enum):
    APROBADO = 1
    REPROBADO = 2
    EN_CURSO = 3

estado = Estado.APROBADO
print("Tipo: Enumerado (Enum)")
print(f"Valor: {estado}")
print(f"Dominio: Un conjunto de constantes relacionadas con un nombre.")
print(f"Operadores: .name, .value")
print(f"Identificador: {type(estado)}\n")