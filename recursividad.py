def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# USO
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")
