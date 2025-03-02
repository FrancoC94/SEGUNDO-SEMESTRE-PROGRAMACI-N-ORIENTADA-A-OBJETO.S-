import pickle


# Clase de  Producto: Representa los productos de nuentro inventario.
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos para obtener los atributos
    def obtener_id(self):
        return self.id_producto

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    # Métodos para actualizar los atributos
    def establecer_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def establecer_precio(self, nuevo_precio):
        self.precio = nuevo_precio


# Clase Inventario: Aquí es donde guardamos todos nuestros productos.
class Inventario:
    def __init__(self):
        self.productos = {}  # Usamos un diccionario para tener acceso rápido a cada producto

    # Añadir un nuevo producto al inventario
    def añadir_producto(self, producto):
        if producto.obtener_id() not in self.productos:
            self.productos[producto.obtener_id()] = producto
        else:
            print(f"¡Ups! El producto con ID {producto.obtener_id()} ya está en el inventario.")

    # Eliminar un producto por su ID
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado correctamente.")
        else:
            print(f"No se encontró el producto con ID {id_producto}.")

    # Actualizar la cantidad o el precio de un producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.establecer_cantidad(cantidad)
            if precio is not None:
                producto.establecer_precio(precio)
            print(f"Producto con ID {id_producto} actualizado correctamente.")
        else:
            print(f"No se encontró el producto con ID {id_producto}.")

    # Buscar productos por nombre
    def buscar_producto(self, nombre):
        resultados = [producto for producto in self.productos.values() if
                      nombre.lower() in producto.obtener_nombre().lower()]
        return resultados

    # Mostrar todos los productos del inventario
    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario actual:")
            for producto in self.productos.values():
                print(
                    f"ID: {producto.obtener_id()} | Nombre: {producto.obtener_nombre()} | Cantidad: {producto.obtener_cantidad()} | Precio: ${producto.obtener_precio():.2f}")

    # Guardar el inventario en un archivo
    def guardar_inventario(self, archivo):
        with open(archivo, 'wb') as file:
            pickle.dump(self.productos, file)
            print(f"Inventario guardado correctamente en {archivo}.")

    # Cargar el inventario desde un archivo
    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'rb') as file:
                self.productos = pickle.load(file)
            print(f"Inventario cargado correctamente desde {archivo}.")
        except FileNotFoundError:
            print(f"No se pudo encontrar el archivo {archivo}.")


# Función para mostrar las opciones del menú
def mostrar_menu():
    print("\n--- Menu de Gestión de Inventario ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar inventario")
    print("6. Guardar inventario")
    print("7. Cargar inventario")
    print("8. Salir")
    print("------------------------------------")


# Función principal que controla el menú interactivo
def menu():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\nAñadir un nuevo producto:")
            try:
                id_producto = int(input("Introduce ID del producto: "))
                nombre = input("Introduce nombre del producto: ")
                cantidad = int(input("Introduce cantidad del producto: "))
                precio = float(input("Introduce precio del producto: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("¡Error! Por favor ingresa valores válidos.")

        elif opcion == "2":
            print("\nEliminar un producto:")
            try:
                id_producto = int(input("Introduce el ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("¡Error! Ingresa un ID válido.")

        elif opcion == "3":
            print("\nActualizar un producto:")
            try:
                id_producto = int(input("Introduce el ID del producto a actualizar: "))
                cantidad = input("Introduce nueva cantidad (deja vacío si no quieres cambiarla): ")
                precio = input("Introduce nuevo precio (deja vacío si no quieres cambiarlo): ")

                # Si la cantidad o el precio no se cambian, dejamos en None
                if cantidad != "":
                    cantidad = int(cantidad)
                else:
                    cantidad = None

                if precio != "":
                    precio = float(precio)
                else:
                    precio = None

                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("¡Error! Ingresa valores válidos.")

        elif opcion == "4":
            print("\nBuscar productos por nombre:")
            nombre = input("Introduce el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                print("Resultados encontrados:")
                for producto in resultados:
                    print(
                        f"ID: {producto.obtener_id()} | Nombre: {producto.obtener_nombre()} | Cantidad: {producto.obtener_cantidad()} | Precio: ${producto.obtener_precio():.2f}")
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            archivo = input("Introduce el nombre del archivo donde guardar el inventario: ")
            inventario.guardar_inventario(archivo)

        elif opcion == "7":
            archivo = input("Introduce el nombre del archivo para cargar el inventario: ")
            inventario.cargar_inventario(archivo)

        elif opcion == "8":
            print("¡Hasta luego! El programa se cerrará.")
            break

        else:
            print("Opción no válida, por favor elige una opción válida.")


# Ejecutar el menú
if __name__ == "__main__":
    menu()
