a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
c = float(input("Introduce el tercer número: "))

if a > b:
    mayor = a
else:
    mayor = b

if c > mayor:
    mayor = c

mayor_entero = int(mayor)
print(f"El número mayor es: {mayor}, su entero: {mayor_entero}")