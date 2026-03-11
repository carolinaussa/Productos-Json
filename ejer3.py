import json
import pandas as pd

#  FUNCION PARA LEER JSON 
def leer_datos():
    try:
        with open("datos.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return []

#  FUNCION PARA GUARDAR JSON 
def guardar_datos(datos):
    with open("datos.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)

#  FUNCION PARA AGREGAR REGISTRO 
def agregar_registro():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    ciudad = input("Ciudad: ")

    nuevo = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad
    }

    datos = leer_datos()
    datos.append(nuevo)
    guardar_datos(datos)

    print("Registro agregado correctamente")

#  FUNCION PARA GENERAR REPORTE 
def generar_reporte():
    datos = leer_datos()
    df = pd.DataFrame(datos)

    print("REPORTE ESTADISTICO")
    print(df.describe())

    # Exportar a CSV
    df.to_csv("reporte.csv", index=False)

    # Exportar a JSON desde Pandas
    df.to_json("reporte_pandas.json", orient="records", indent=4)

    print("\nArchivos reporte.csv y reporte_pandas.json creados")

# - MENU PRINCIPAL 
while True:
    print("1. Ver datos")
    print("2. Agregar registro")
    print("3. Generar reporte")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        print(leer_datos())

    elif opcion == "2":
        agregar_registro()

    elif opcion == "3":
        generar_reporte()

    elif opcion == "4":
        break

    else:
        print("Opcion no valida")