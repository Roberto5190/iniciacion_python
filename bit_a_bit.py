# Operadores bit a bit en Python

# Definimos dos números
a = 60   # 60 = 0011 1100 (en binario)
b = 13   # 13 = 0000 1101 (en binario)

# Operador AND (&)
and_result = a & b
print(f"Operación AND: {a} & {b} = {and_result} (binario: {bin(and_result)})")

# Operador OR (|)
or_result = a | b
print(f"Operación OR: {a} | {b} = {or_result} (binario: {bin(or_result)})")

# Operador XOR (^)
xor_result = a ^ b
print(f"Operación XOR: {a} ^ {b} = {xor_result} (binario: {bin(xor_result)})")

# Operador NOT (~)
not_result = ~a
print(f"Operación NOT: ~{a} = {not_result} (binario: {bin(not_result)})")

# Desplazamiento a la izquierda (<<)
shift_left_result = a << 2  # Desplaza a la izquierda 2 posiciones
print(f"Desplazamiento a la izquierda: {a} << 2 = {shift_left_result} (binario: {bin(shift_left_result)})")

# Desplazamiento a la derecha (>>)
shift_right_result = a >> 2  # Desplaza a la derecha 2 posiciones
print(f"Desplazamiento a la derecha: {a} >> 2 = {shift_right_result} (binario: {bin(shift_right_result)})")
