# Clase base: Animal
class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo encapsulado
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    def mostrar_detalles(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.edad} años")

    def hacer_sonido(self):
        print("El animal hace un sonido")

# Clase derivada: Perro
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        print(f"{self.get_nombre()} dice: ¡Guau!")

# Clase derivada: Gato
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        print(f"{self.get_nombre()} dice: ¡Miau!")

# Clase que demuestra polimorfismo
class Veterinario:
    def escuchar_sonido(self, animal):
        animal.hacer_sonido()

# Crear animales y demostrar polimorfismo
perro = Perro("Max", 4, "Pitbull")
gato = Gato("Michi", 2, "Negro")

perro.mostrar_detalles()
gato.mostrar_detalles()

veterinario = Veterinario()
veterinario.escuchar_sonido(perro)  # Output: Max dice: ¡Guau!
veterinario.escuchar_sonido(gato)   # Output: Michi dice: ¡Miau!
