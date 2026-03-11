import json

ventas = [
    {"vendedor": "jose", "mes": "dciembre", "ventas": 1100000},
    {"vendedor": "carlos", "mes": "Enero", "ventas": 800000},
    {"vendedor": "Ana", "mes": "enero", "ventas": 2000000},
    {"vendedor": "jose", "mes": "Febrero", "ventas": 2100000},
    {"vendedor": "Carlos", "mes": "Enero", "ventas": 600000}
]

totales = {}

# Total por vendedor
for v in ventas:
    nombre = v["vendedor"]
    monto = v["ventas"]

    if nombre in totales:
        totales[nombre] += monto
    else:
        totales[nombre] = monto

print("TOTAL POR VENDEDOR")
for vendedor, total in totales.items():
    print(vendedor, ":", total)

# Promedio mensual general
total_general = sum(totales.values())
cantidad_vendedores = len(totales)
promedio = total_general / cantidad_vendedores

print("PROMEDIO GENERAL DE VENTAS")
print(promedio)

# Vendedor con mayores ventas
mayor_vendedor = max(totales, key=totales.get)
print("VENDEDOR CON MAYORES VENTAS")
print(mayor_vendedor, "con", totales[mayor_vendedor])

# Ranking (de mayor a menor)
ranking = sorted(totales.items(), key=lambda x: x[1], reverse=True)

ranking_lista = []
for vendedor, total in ranking:
    ranking_lista.append({"vendedor": vendedor, "total": total})

# Exportar ranking a JSON
with open("ranking_ventas.json", "w") as archivo:
    json.dump(ranking_lista, archivo, indent=4)

print("\nArchivo ranking_ventas.json creado")