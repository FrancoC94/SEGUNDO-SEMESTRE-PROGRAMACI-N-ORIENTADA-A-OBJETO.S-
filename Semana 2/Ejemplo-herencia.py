class Animal:
    @staticmethod
    def comer():
        return "Comiendo..."

class Perro(Animal):
    @staticmethod
    def ladrar():
        return "Guau"

# Crea instancia
perro = Perro()
print(perro.comer())  # Comiendo...
print(perro.ladrar())  # Guau
