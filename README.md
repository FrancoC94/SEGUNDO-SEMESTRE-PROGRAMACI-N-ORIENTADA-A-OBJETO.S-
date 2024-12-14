# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):  # Asumimos una semana de 7 días
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f} °C")

# Ejecutamos el programa
if __name__ == "__main__":
    main()
# Clase que representa el clima de un día
class ClimaDia:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    def obtener_temperatura(self):
        return self.temperatura

# Clase para gestionar una semana de clima
class SemanaClima:
    def __init__(self):
        self.dias = []

    def agregar_dia(self, clima_dia):
        self.dias.append(clima_dia)

    def calcular_promedio(self):
        total_temperaturas = sum(dia.obtener_temperatura() for dia in self.dias)
        return total_temperaturas / len(self.dias)

    def ingresar_temperaturas(self):
        for i in range(7):  # Asumimos una semana de 7 días
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            clima_dia = ClimaDia(temp)
            self.agregar_dia(clima_dia)

# Función principal
def main():
    semana = SemanaClima()
    semana.ingresar_temperaturas()
    promedio = semana.calcular_promedio()
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f} °C")

# Ejecutamos el programa
if __name__ == "__main__":
    main()
