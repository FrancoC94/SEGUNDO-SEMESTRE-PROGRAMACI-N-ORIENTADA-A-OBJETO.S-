# Definición de la clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def mostrar(self):
        # Muestra el producto de manera sencilla
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


# Definición de la clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        # Verifica si el producto ya está en el inventario por ID
        for p in self.productos:
            if p.id_producto == producto.id_producto:
                print("El ID ya existe. No se puede agregar el producto.")
                return
        self.productos.append(producto)
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        # Busca y elimina el producto por ID
        for p in self.productos:
            if p.id_producto == id_producto:
                self.productos.remove(p)
                print(f"Producto con ID {id_producto} eliminado.")
                return
        print("Producto no encontrado.")

    def mostrar_inventario(self):
        # Muestra todos los productos del inventario
        if self.productos:
            for p in self.productos:
                print(p.mostrar())
        else:
            print("El inventario está vacío.")


# Menú interactivo para el usuario
def menu():
    inventario = Inventario()

    while True:
        print("\n1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                # Solicitar datos para agregar un producto
                id_producto = int(input("Ingresa el ID del producto: "))
                nombre = input("Ingresa el nombre del producto: ")
                cantidad = int(input("Ingresa la cantidad del producto: "))
                precio = float(input("Ingresa el precio del producto: $"))
                nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(nuevo_producto)
            except ValueError:
                print("Por favor, ingresa datos válidos.")

        elif opcion == "2":
            try:
                # Solicitar ID para eliminar producto
                id_producto = int(input("Ingresa el ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("Por favor, ingresa un ID válido.")

        elif opcion == "3":
            # Mostrar todos los productos en el inventario
            inventario.mostrar_inventario()

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


# Ejecutar el programa
if __name__ == "__main__":
    menu()
