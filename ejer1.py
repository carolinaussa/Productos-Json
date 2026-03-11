import json

productos = [
    {"producto": "computador", "precio": 250000, "cantidad": 4},
    {"producto": "teclado", "precio": 130000, "cantidad": 8},
    {"producto": "torre", "precio": 200000, "cantidad": 3}
]

total_inventario = 0
bajo_stock = []

print("VALOR POR PRODUCTO")

for p in productos:
    total_producto = p["precio"] * p["cantidad"]
    print(p["producto"], ":", total_producto)

    total_inventario += total_producto

    if p["cantidad"] < 5:
        bajo_stock.append(p)

print("TOTAL INVENTARIO")
print(total_inventario)

# Guardar productos con bajo stock
with open("bajo_stock.json", "w") as archivo_bajo:
    json.dump(bajo_stock, archivo_bajo, indent=4)

print("Archivo bajo_stock.json creado")