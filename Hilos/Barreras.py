import threading

# Crear una barrera para 2 hilos
barrera = threading.Barrier(2)

# Función que usa la barrera
def trabajar():
    print("Hilo iniciado")
    barrera.wait()  # Esperar a que ambos hilos lleguen a este punto
    print("Hilo continuando")

# Crear hilos
hilo1 = threading.Thread(target=trabajar)
hilo2 = threading.Thread(target=trabajar)

# Iniciar hilos
hilo1.start()
hilo2.start()

# Esperar que ambos hilos terminen
hilo1.join()
hilo2.join()

print("Programa terminado")
