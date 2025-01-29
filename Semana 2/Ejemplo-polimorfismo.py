class Animal:
    def hacer_sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

# Crea instancia
animal = Animal()
perro = Perro()

print(animal.hacer_sonido())  # Sonido genérico
print(perro.hacer_sonido())   # Guau
