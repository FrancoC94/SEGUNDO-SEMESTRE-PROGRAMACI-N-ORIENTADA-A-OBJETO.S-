import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
   #SEMANA 2
        '1': 'Semana 2/Ejemplo-abstraccion.py',
        '2': 'Semana 2/Ejemplo-encapsulacion.py',
        '3': 'Semana 2/Ejemplo-herencia.py',
        '4': 'Semana 2/Ejemplo-polimorfismo.py',
            #SEMANA 3
        '5': 'Semana 3/Ejemplo Programacion Tradicional en Python..py',
        '6': 'Semana 3/Ejemplo Programación Orientada a Objetos (POO) en Python.py',
    #SEMANA 4
        '7': 'Semana 4/EjemplosMundoReal_POO.py',
    # SEMANA 5
        '8': 'Semana 5/Tarea Tipos de datos Identificadores.py',
        # SEMANA 6
        '9': 'Semana 6/Aplicación de Conceptos de Programación Orientada a Objetos (POO) en Python.py',
        # SEMANA 7
        '10': 'Semana 7/Implementación de Constructores y Destructores en Python.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()