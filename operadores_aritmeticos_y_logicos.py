#OPERADORES ARITMETICOS
def operadores_aritmeticos():
    print("--- Operadores Aritméticos ---")
    
    num1 = 10
    num2 = 3
    
    # Suma
    suma = num1 + num2
    print("SUMA")
    print(f"{num1} + {num2} = {suma}")
    
    # Resta
    resta = num1 - num2
    print("\nRESTA")
    print(f"{num1} - {num2} = {resta}")
    
    # Multiplicación
    multiplicacion = num1 * num2
    print("\nMULTIPLICACIÓN")
    print(f"{num1} * {num2} = {multiplicacion}")
    
    # División
    division = num1 / num2
    print("\nDIVISIÓN")
    print(f"{num1} / {num2} = {division}")
    
    # División entera (sin decimales)
    division_entera = num1 // num2
    print("\nDIVISIÓN ENTERA")
    print(f"{num1} // {num2} = {division_entera}")
    
    # Módulo (resto de la división)
    modulo = num1 % num2
    print("\nMÓDULO")
    print(f"{num1} % {num2} = {modulo}")
    
    # Exponente (potencia)
    exponente = num1 ** num2
    print("\nEXPONENTE")
    print(f"{num1} ** {num2} = {exponente}")


#OPERADORES LOGICOS
def operadores_logicos():
    print("\n--- Operadores Lógicos ---")
    
    a = True
    b = False
    
    # AND
    and_result = a and b
    print("AND")
    print(f"{a} and {b} = {and_result}")
    
    # OR
    or_result = a or b
    print("\nOR")
    print(f"{a} or {b} = {or_result}")
    
    # NOT
    not_result = not a
    print("\nNOT")
    print(f"not {a} = {not_result}")
    
    # Combinación de operadores lógicos
    combo_result = (a or b) and not a
    print("\nCOMBINACIÓN OPERADORES LÓGICOS")
    print(f"(a or b) and not a = {combo_result}")



#MAIN
def main():
    # Usamos las funciones para mostrar los resultados
    operadores_aritmeticos()
    operadores_logicos()

# Ejecutamos el programa principal
if __name__ == "__main__":
    main()
