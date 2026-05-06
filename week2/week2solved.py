import csv

def calcular_valor_inventario(precio, stock):
    return precio * stock


total_inventario = 0
total_activos = 0
productos_sin_stock = 0
categorias = {}

with open("C:/temp/pyexer/producto.csv", newline='', encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        precio = float(fila["precio"])
        stock = int(fila["stock"])
        activo = fila["activo"] == "True"

        # Contar productos sin stock (TODOS, no solo activos)
        if stock == 0:
            productos_sin_stock += 1

        # Procesar solo activos
        if activo:
            total_activos += 1

            valor = calcular_valor_inventario(precio, stock)
            total_inventario += valor

            producto = fila["producto"]
            categoria = fila["categoria"]

            # Conteo por categoría
            if categoria in categorias:
                categorias[categoria] += 1
            else:
                categorias[categoria] = 1

            # Imprimir info
            print(f"{producto} - {categoria} - Precio: {precio} - Stock: {stock} - Valor: {valor:.0f}")


print("\n--- RESUMEN ---")
print(f"Total productos activos: {total_activos}")
print(f"Valor total del inventario: {total_inventario}")
print(f"Productos sin stock: {productos_sin_stock}")

print("\n--- PRODUCTOS POR CATEGORÍA ---")
for cat, count in categorias.items():
    print(f"{cat}: {count}")