class Carro:
    def __init__(self, marca):
        self.__marca = marca  # Atributo privado

    def get_marca(self):
        return self.__marca


# Crea instancia
Carro = Carro("Mazda")
print(Carro.get_marca())  # Mazda
