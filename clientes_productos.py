class Persona:
    def __init__(self, nombre_persona):
        self.nombre = nombre_persona
class Cliente(Persona):
    def __init__(self, nombre_cliente, saldo_cliente):
        super().__init__(nombre_cliente)
        self.saldo = saldo_cliente
class Producto:
    def __init__(self, nombre_producto, precio_producto):
        self.nombre = nombre_producto
        self.precio = precio_producto
def comprar_producto_cliente(cliente, producto, uds):
    total = producto.precio * uds
    if cliente.saldo >= total:
        cliente.saldo -= total
        print(f"El cliente con nombre {cliente.nombre} ha comprado el producto con nombre {producto.nombre} por un precio unitario de {producto.precio} y un total de {uds} unidades.")
        print(f"Saldo restante: {cliente.saldo}€")
    else:
        print(f"{cliente.nombre} no tiene saldo suficiente para comprar {uds} unidad(es) de {producto.nombre}.")
cliente1 = Cliente("Sergio", 50)
producto1 = Producto("Camiseta", 15)

comprar_producto_cliente(cliente1, producto1, 2)