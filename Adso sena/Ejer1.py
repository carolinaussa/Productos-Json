import json
import pandas as pd

sena=pd.read_json("https://raw.githubusercontent.com/CesarMCuellarCha/archivosCSV/refs/heads/main/SENA.matriculados.json")
print("verificiacion: ",sena[sena["CODIGO_PROGRAMA"]==228118]["ESTADO_FICHA"].unique())
def filtrar_ADSO(sena):
    # eliminar espacios y puntos
    sena["PROGRAMA"] = sena["PROGRAMA"].str.strip().str.replace(".", "", regex=False)
    # filtro ADSO
    adso = sena[sena["PROGRAMA"] == "ANALISIS Y DESARROLLO DE SOFTWARE"]
    adso.to_json("dataset/ADSO-CTPI.json", orient="records", indent=4, force_ascii=False)
    return adso
def filtrar_ficha_3312932(sena):
    ficha_3312932 = sena[sena["FICHA"] == 3312932]
    ficha_3312932.to_json("dataset/ficha_3312932.json", orient="records", indent=4, force_ascii=False)
    return ficha_3312932
def Codigo_Programa(sena):
    filtro=sena[(sena["CODIGO_PROGRAMA"]==228118) & (sena["ESTADO_APRENDIZ"].str.contains("transito | tránsito"))]
    print(filtro)
    filtro.to_json("dataset/codigo_228118.json",orient="records", indent=4, force_ascii=False)
    return filtro
def Cantidad_aprendices(sena):
    filtro=Codigo_Programa(sena)
    cantidad=len(filtro)
    return cantidad
def menu():
    while True:
        print("1. Filtrar por programa ADSO")
        print("2. Filtrar por ficha 3312932")
        print("3. Filtrar por código de programa 228118 y estado 'En transito'")
        print("4. Cantidad de aprendices en el programa 228118 y estado 'En transito'")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                adso = filtrar_ADSO(sena)
                print(adso)
            case "2":
                ficha_3312932 = filtrar_ficha_3312932(sena)
                print(ficha_3312932)
            case "3":
                 Codigo_Programa(sena)
            case "4":
                cantidad = Cantidad_aprendices(sena)
                print(f"Cantidad de aprendices en el programa 228118 y estado 'En transito': {cantidad}")
            case "5":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")
menu()