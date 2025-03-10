import threading
import time

# Creamos un semáforo con 2 permisos
semaforo = threading.Semaphore(2)

# Función que simula el uso de un recurso
def usar_recurso(hilo_numero):
    print(f"Hilo {hilo_numero} esperando para acceder al recurso")
    semaforo.acquire()  # Adquirir el semáforo (acceso al recurso)
    print(f"Hilo {hilo_numero} accediendo al recurso")
    time.sleep(2)  # Simula el uso del recurso
    print(f"Hilo {hilo_numero} liberando el recurso")
    semaforo.release()  # Liberar el semáforo (liberar el recurso)

# Creamos hilos
hilos = [threading.Thread(target=usar_recurso, args=(i,)) for i in range(4)]

# Iniciar los hilos
for hilo in hilos:
    hilo.start()

# Esperar que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print("Todos los hilos han terminado")
