# Este es un programa para convertir temperaturas entre grados Celsius y Fahrenheit
# La idea es que puedas convertir fácilmente las temperaturas sin tener que hacer cálculos manuales.
# El programa usa distintos tipos de datos y permite al usuario elegir qué conversión desea realizar.

def convertir_celsius_a_fahrenheit(celsius):
    """
    Convierte la temperatura de grados Celsius a Fahrenheit.

    Argumento:
    celsius (float): La temperatura en grados Celsius que se desea convertir.

    Retorna:
    float: La temperatura equivalente en grados Fahrenheit.
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def convertir_fahrenheit_a_celsius(fahrenheit):
    """
    Convierte la temperatura de grados Fahrenheit a Celsius.

    Argumento:
    fahrenheit (float): La temperatura en grados Fahrenheit que se desea convertir.

    Retorna:
    float: La temperatura equivalente en grados Celsius.
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def main():
    """
    Esta es la función principal. Se encarga de interactuar con el usuario y pedirle los datos necesarios.
    El usuario podrá elegir si desea convertir de Celsius a Fahrenheit o viceversa.
    """
    print("¡Hola! Bienvenido al conversor de temperaturas.")
    seguir = True

    while seguir:
        # Preguntamos al usuario qué tipo de conversión desea realizar
        seleccion = input(
            "Elige una opción:\n1. Convertir de Celsius a Fahrenheit\n2. Convertir de Fahrenheit a Celsius\n3. Salir\n")

        if seleccion == '1':
            # Si elige convertir de Celsius a Fahrenheit
            celsius = float(input("Introduce la temperatura en grados Celsius: "))
            fahrenheit = convertir_celsius_a_fahrenheit(celsius)
            print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.\n")

        elif seleccion == '2':
            # Si elige convertir de Fahrenheit a Celsius
            fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
            celsius = convertir_fahrenheit_a_celsius(fahrenheit)
            print(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius.\n")

        elif seleccion == '3':
            # Si elige salir
            print("Gracias por usar el conversor de temperaturas. ¡Hasta luego!")
            seguir = False

        else:
            print("Ups, esa opción no es válida. Por favor, elige una opción del menú.\n")


# Ejecutamos el programa
if __name__ == "__main__":
    main()
