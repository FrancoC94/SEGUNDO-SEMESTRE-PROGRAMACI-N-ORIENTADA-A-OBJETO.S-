import threading

# Variable compartida
contador_global = 0

# Creamos un objeto Lock
mutex = threading.Lock()

# Función que incrementa el contador de forma segura
def incrementar():
    global contador_global
    for _ in range(100000):
        with mutex:
            contador_global += 1

# Creamos hilos
hilo1 = threading.Thread(target=incrementar)
hilo2 = threading.Thread(target=incrementar)

# Iniciar hilos
hilo1.start()
hilo2.start()

# Esperar que ambos hilos terminen
hilo1.join()
hilo2.join()

# Resultado esperado: 200000
print(f"Contador final: {contador_global}")
