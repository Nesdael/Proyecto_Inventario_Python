from inventario import inventario
from extras import *
import csv

def guardar_inventario(inventario):
    """
    Guarda el inventario en un archivo CSV.
    Parámetros: lista de diccionarios donde se guardan los productos
    Retorno: None
    """
    deleteScreen()
    with open("productos.csv", "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "precio", "cantidad"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)  
        escritor.writeheader()          # escribe la primera fila: nombre,precio,cantidad
        escritor.writerows(inventario)
        print("Guardado")
        pauseScreen()
        return
    
def cargar_inventario(inventario):
    """
    Carga productos desde un CSV y pregunta si sobrescribir o fusionar.
    Parámetros: lista de diccionarios donde se guardan los productos
    pass significa "si ocurre este error, no hagas nada y sigue".
    """
    deleteScreen()
    try:
        with open("productos.csv", "r", encoding="utf-8") as archivo: 
            lector = csv.DictReader(archivo)
            for fila in lector:
                nombre = fila['nombre'] 
                precio= float(fila["precio"])
                cantidad= int(fila["cantidad"])
                existe = False
                for i in inventario:
                    if i['nombre'].lower() == nombre.lower():
                        existe = True
                        break
                if not existe:
                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
            print(f"Productos cargados: {len(inventario)}")
            pauseScreen()
    except FileNotFoundError:
        pass