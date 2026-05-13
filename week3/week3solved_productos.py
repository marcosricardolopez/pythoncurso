class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(self.nombre, "-", self.precio)


p1 = Producto("Laptop", 1000)
p2 = Producto("Mouse", 50)
p3 = Producto("Teclado", 80)


class Carrito:
    def __init__(self):
        self.productos = []


    def agregar(self, producto):
        self.productos.append(producto)


    def mostrar(self):
        for p in self.productos:
           p.mostrar()


    def total(self):
        suma = 0
        for p in self.productos:
            suma += p.precio
        print("Total:", suma)


carrito = Carrito()

carrito.agregar(p1)
carrito.agregar(p2)
carrito.agregar(p3)

carrito.mostrar()
carrito.total()