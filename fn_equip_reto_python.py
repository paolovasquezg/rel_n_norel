import json
import pandas as pd
import random

def leer_json(ruta_json):
    with open(ruta_json, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    return datos

def leer_excel(ruta_excel, hoja=0):
    df = pd.read_excel(ruta_excel, sheet_name=hoja, engine='openpyxl')
    return df

rel = leer_excel("data/BD_Relacional_Ventas_2022_2024.xlsx")
no_rel = leer_json("data/BD_NoRelacional_Productos_100.json")

rel["productos"] = None

for indice, fila in rel.iterrows():
    
    limite_productos = random.randint(10, 50)
    
    productos = []

    for i, producto in enumerate(no_rel):
        if i < limite_productos:
            productos.append(producto)
        else:
            break 

    rel.at[indice, "productos"] = json.dumps(productos, ensure_ascii=False)

print(rel.head())