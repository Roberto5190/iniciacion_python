#  1. De float a int (trunca la parte decimal)
x = 9.87
entero = int(x)
print(entero)  # Resultado: 9


#  2. De int a float
x = 10
decimal = float(x)
print(decimal)  # Resultado: 10.0


#  3. De str a int o float
texto = "42"
numero = int(texto)
print(numero + 10)  # Resultado: 52

decimal = float("3.14")
print(decimal * 2)  # Resultado: 6.28


# 4. De int o float a str
edad = 25
mensaje = "Tienes " + str(edad) + " años."
print(mensaje)  # Resultado: Tienes 25 años.


# 5. Redondear un número en vez de truncar
x = 5.76
redondeado = round(x)
print(redondeado)  # Resultado: 6
