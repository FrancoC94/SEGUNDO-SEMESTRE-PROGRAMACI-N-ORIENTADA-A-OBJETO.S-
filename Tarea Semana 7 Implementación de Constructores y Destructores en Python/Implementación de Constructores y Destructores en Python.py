# Definimos la clase Carro que utiliza un constructor y un destructor
class Carro:
    # El constructor (__init__) inicializa los atributos del objeto
    def __init__(self, marca, modelo, año):
        # Atributos del carro
        self.marca = marca
        self.modelo = modelo
        self.año = año
        print(f"Carro creado: {self.marca} {self.modelo} {self.año}")

    # El destructor (__del__) se utiliza para realizar limpieza o liberar recursos
    def __del__(self):
        # Este mensaje se imprime cuando el objeto es destruido
        print(f"Carro destruido: {self.marca} {self.modelo} {self.año}")


# Ejemplo de uso de la clase Carro
def prueba_carro():
    # Creamos un objeto de la clase Carro con la marca Chevrolet Sail
    mi_carro = Carro("Chevrolet", "Sail", 2017)

    # Realizamos algunas acciones con el objeto, si es necesario
    print(f"Mi carro es un {mi_carro.marca} {mi_carro.modelo} del año {mi_carro.año}")

    # El objeto se destruirá al final de la función, lo cual activará el destructor


# Llamamos a la función de prueba
prueba_carro()

# Aseguramos que el objeto es destruido cuando se sale del ámbito de la función
# El destructor se ejecuta automáticamente en este caso