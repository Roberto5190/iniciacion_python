# Memoización con functools.lru_cache
from functools import lru_cache

def fibonacci_lento(n):
    if n <= 1:
        return n
    return fibonacci_lento(n - 1) + fibonacci_lento(n - 2)


# Optimización con memoización
@lru_cache(maxsize=None)
def fibonacci_rapido(n):
    if n <= 1:
        return n
    return fibonacci_rapido(n - 1) + fibonacci_rapido(n - 2)

# Evitar bucles innecesarios
# Ineficiente: O(n^2)
def contar_unicos_lento(lista):
    unicos = []
    for i in lista:
        if i not in unicos:
            unicos.append(i)
    return len(unicos)


# Eficiente: O(n)
def contar_unicos_rapido(lista):
    return len(set(lista))


# Uso de diccionarios para acceso rápido
def contar_frecuencias(texto):
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia




if __name__ == "__main__":
    print("🔄 Fibonacci sin optimización:", fibonacci_lento(10))  # lento
    print("⚡ Fibonacci optimizado:", fibonacci_rapido(100))       # instantáneo

    lista = [1, 2, 2, 3, 4, 4, 4, 5]
    print("📊 Únicos lentos:", contar_unicos_lento(lista))
    print("📊 Únicos rápidos:", contar_unicos_rapido(lista))

    texto = "python código código eficiente python optimización"
    print("📚 Frecuencias:", contar_frecuencias(texto))
    # Prueba de rendimiento