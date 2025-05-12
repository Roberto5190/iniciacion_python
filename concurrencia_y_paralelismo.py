# CONCURRENCIA
import threading
import time

def descargar_archivo(nombre, tiempo):
    print(f"🟡 Comenzando descarga: {nombre}")
    time.sleep(tiempo)
    print(f"✅ Descarga completada: {nombre}")

if __name__ == "__main__":
    t1 = threading.Thread(target=descargar_archivo, args=("archivo1.zip", 3))
    t2 = threading.Thread(target=descargar_archivo, args=("archivo2.zip", 2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("🚀 Todas las descargas han finalizado.")

# En este ejemplo, se utilizan hilos para descargar archivos de manera concurrente.
# Esto permite que las descargas se realicen al mismo tiempo, mejorando la eficiencia.



# PARALELISMO
import multiprocessing
import time

def calcular_potencia(numero):
    print(f"⚙️ Calculando {numero} ** 1000000")
    _ = numero ** 1000000
    print(f"✅ Cálculo finalizado para {numero}")

if __name__ == "__main__":
    numeros = [10, 20]

    procesos = []
    for n in numeros:
        p = multiprocessing.Process(target=calcular_potencia, args=(n,))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print("💥 Cálculos pesados completados.")
# En este ejemplo, se utilizan hilos para descargar archivos y procesos para realizar cálculos pesados.
# La descarga de archivos es una tarea I/O-bound, donde la concurrencia es más eficiente.
