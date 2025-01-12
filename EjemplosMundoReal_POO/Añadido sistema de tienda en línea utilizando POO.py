# Definir la clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        # Atributos del producto
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto
        self.cantidad = cantidad  # Cantidad de productos disponibles

    def mostrar_detalles(self):
        """Muestra los detalles del producto (nombre, precio y stock)."""
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Stock disponible: {self.cantidad} unidades")


# Definir la clase Cliente
class Cliente:
    def __init__(self, nombre):
        # Atributos del cliente
        self.nombre = nombre  # Nombre del cliente
        self.carrito = []  # Lista que guardará los productos que compra el cliente

    def agregar_al_carrito(self, producto):
        """
        Si el producto tiene stock, lo agrega al carrito del cliente.
        Si no hay stock, muestra un mensaje de error.
        """
        if producto.cantidad > 0:
            self.carrito.append(producto)  # Agregar producto al carrito
            producto.cantidad -= 1  # Reducir el stock disponible
            print(f"{producto.nombre} ha sido agregado a tu carrito.")
        else:
            print(f"Lo siento, no hay stock de {producto.nombre}.")

    def mostrar_carrito(self):
        """Muestra los productos que están en el carrito del cliente."""
        print(f"Carrito de {self.nombre}:")
        if not self.carrito:
            print("Tu carrito está vacío.")
        for producto in self.carrito:
            print(f"- {producto.nombre} - ${producto.precio}")


# Código para probar la tienda

# Crear algunos productos
producto1 = Producto("Camiseta", 15.99, 10)  # 10 camisetas en stock
producto2 = Producto("Pantalón", 35.50, 5)  # 5 pantalones en stock
producto3 = Producto("Zapatos", 50.00, 2)  # 2 pares de zapatos en stock

# Crear un cliente
cliente = Cliente("Ashley")

# Mostrar los detalles de los productos disponibles
producto1.mostrar_detalles()
producto2.mostrar_detalles()
producto3.mostrar_detalles()

# Juan agrega productos a su carrito
cliente.agregar_al_carrito(producto1)  # Agregar camiseta
cliente.agregar_al_carrito(producto2)  # Agregar pantalón

# Mostrar los productos que Juan tiene en su carrito
cliente.mostrar_carrito()

# Intentar agregar productos sin stock
cliente.agregar_al_carrito(producto3)  # Agregar zapatos
cliente.agregar_al_carrito(producto3)  # Intentar agregar zapatos otra vez (ya no hay stock)
