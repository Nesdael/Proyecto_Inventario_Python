# Importamos la lista donde se guardan los productos
from inventario import inventario
from colors import *
import csv
from extras import deleteScreen, pauseScreen

# Función para agregar productos
def agregar_producto(inventario):
    # Variable de control para repetir el menú
    continuar = "si"
    # Ciclo para agregar varios productos
    while continuar == "si":
        print(f"{F_VERDE}Haz elegido la opcion agregar producto{RESET}\n")
        # Pedimos nombre del producto
        nombre_producto = input("Ingrese el nombre del producto\n")
        existe = False
        # Validamos que solo tenga letras
        if not nombre_producto.replace(" ", "").isalpha() or len(nombre_producto) == 0:
                print("Solo se pueden colocar letras")
                continue # Vuelve a pedir el nombre  
        for i in inventario:
            if i['nombre'] == nombre_producto:
                existe = True
                break     
        if existe:
            print('Este producto ya esta en el inventario')
            continue  
        # Validación del precio    
        while True:
            try:
                precio = float(input(f"Ingrese el precio unitario de {nombre_producto}\n"))
                if precio <= 0:
                    print("Error: No se puede colocar 0")
                    continue
                break
            except ValueError:
                print("Error: Favor solo ingresar digitos")     
        # Validación de la cantidad        
        while True:
            try:
                cantidad = int(input(f"Ingrese la cantidad que desea de {nombre_producto}\n"))
                if cantidad <= 0:
                    print("Error: No se puede colocar 0")
                    continue
                break
            except ValueError:
                print("Error: Por favor solo ingresar numeros")   
        # Creamos un diccionario con los datos del producto        
        producto = {}   
        producto['nombre'] = nombre_producto
        producto['precio'] = precio
        producto['cantidad'] = cantidad                  
        # Guardamos el producto en la lista inventario        
        inventario.append(producto)
        
        
        # Preguntamos si desea seguir agregando productos
        continuar = input("\nDesea seguir agregando productos? (Si/No)\n").lower()
        deleteScreen()
    return producto
    
# Función para mostrar el inventario        
def mostrar_inventario(inventario):
    print(f"{F_VERDE}Haz elegido la opcion mostrar producto{RESET}\n")
    # Si el inventario está vacío
    if len(inventario) == 0:
        print("Aun no hay nada ")
        pauseScreen()
        return
    else:
        print("----INVENTARIO----")    
        # Recorremos la lista de productos
        for producto in inventario:
            print(f"producto: {producto['nombre'].capitalize()} | precio: {producto['precio']} | cantidad: {producto['cantidad']}" )
            print()
        pauseScreen()
        return 
        
# Función para calcular estadísticas            
def calcular_estadisticas(inventario):
    print(f"{F_VERDE}Haz elegido la opcion calcular estadisticas{RESET}\n")
    print(inventario)
    cantidad_total = 0 # Total de productos
    valortotal = 0 # Valor total del inventario
    # Recorremos el inventario
    for producto in inventario:
        cantidad_total += producto['cantidad']
        valortotal += producto['precio'] * producto['cantidad']
    # Mostramos resultados    
    print(f"La cantidad total de productos registrados es: {cantidad_total}\n")
    print(f"El valor total del inventario es: {valortotal}\n")
    pauseScreen()
    return

def buscar_producto(inventario):
    buscar = input('Que producto desea buscar?\n ').strip()
    
    print(f"Buscando: '{buscar}'")
    for producto in inventario:
        if producto['nombre'] == buscar:
            print('Producto encontrado')
            print(f"Nombre: {producto['nombre'].capitalize()}")
            print(f"precio: {producto['precio']}")
            print(f"cantidad: {producto['cantidad']}")
            return
    print("El producto no se encontro")
    
def actualizar_producto(inventario):
    buscar = input("Que producto desea actualizar?\n").lower().strip()
    
    for producto in inventario:
        if producto['nombre'] == buscar:
            print("Que desea actualizar?")
            print("1. Valor")
            print("2. Cantidad")
            print("3. Nombre")
            while True:
                opcion = int(input())

                if opcion == 1:
                    producto['precio'] = float(input("Ingrese el nuevo precio: \n"))
                elif opcion == 2:
                    producto['cantidad'] = int(input("Ingrese la nueva cantidad: \n"))
                elif opcion == 3:
                    producto['nombre'] = input("Ingrese el nuevo nombre del producto: \n")
                else:
                    print("Ingrese una opcion valida")
                    continue

                print("Producto actualizado correctamente")
                return    
        print("El producto no se encontro")
    
    
    
def eliminar_producto(inventario):
    for producto in inventario:
        print("Nombre:", producto['nombre'].capitalize(), "Precio:", producto['precio'], "Cantidad:", producto['cantidad'])
        
    nombre_eliminar = input('Que producto desea eliminar?\n')
    
    for producto in inventario:
        if producto['nombre'] == nombre_eliminar:
            inventario.remove(producto)
            print('Eliminado exitosamente')
            
    for producto in inventario:
        print("Nombre:", producto['nombre'].capitalize(), "Precio:", producto['precio'], "Cantidad:", producto['cantidad'])   
    return


def guardar_inventario(inventario):
    with open("productos.csv", "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "precio", "cantidad"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        
        escritor.writeheader()          # escribe la primera fila: nombre,precio,cantidad
        escritor.writerows(inventario)
        return
    
def cargar_inventario(inventario):
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
                        return
                if not existe:
                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
    except FileNotFoundError:
        pass
    return
            
def salir():
    continuar = "no"
    print("Has salido del menu de inventario, vuelva pronto")
    return continuar
        


# Este bloque solo se ejecuta si este archivo se ejecuta directamente    
if __name__ == "__main__": 
    agregar_producto()
    mostrar_inventario()
    calcular_estadisticas()
                
                        
                
                