# Importamos la lista donde se guardan los productos
from inventario import inventario
from colors import *
from extras import deleteScreen, pauseScreen

# Función para agregar productos
def agregar_producto(inventario):
    """
    Agrega un nuevo producto al inventario.
    Parámetros: lista de diccionarios donde se guardan los productos
    Retorno: None   
    """
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
    return
    
# Función para mostrar el inventario        
def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario en consola.
    Parámetros: lista de diccionarios donde se guardan los productos
    Retorno: None  
    """
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
    """
    Calcula y muestra estadísticas del inventario.
    Parámetros: lista de diccionarios donde se guardan los productos
    Retorno: None
    """
    if len(inventario) == 0:
        print("El inventario está vacío")
        pauseScreen()
        return

    cantidad_total = 0
    valortotal = 0
    producto_mas_caro = inventario[0]      # empieza con el primero
    producto_mayor_stock = inventario[0]   # empieza con el primero

    for producto in inventario:
        cantidad_total += producto['cantidad']
        valortotal += producto['precio'] * producto['cantidad']

        # Si el precio actual es mayor al guardado, lo reemplaza
        if producto['precio'] > producto_mas_caro['precio']:
            producto_mas_caro = producto

        # Si la cantidad actual es mayor a la guardada, la reemplaza
        if producto['cantidad'] > producto_mayor_stock['cantidad']:
            producto_mayor_stock = producto

    # Lambda para subtotal de cada producto
    subtotal = lambda p: p["precio"] * p["cantidad"]

    print(f"Unidades totales: {cantidad_total}")
    print(f"Valor total: {valortotal}")
    print(f"Producto mas caro: {producto_mas_caro['nombre']} - ${producto_mas_caro['precio']}")
    print(f"Producto mayor stock: {producto_mayor_stock['nombre']} - {producto_mayor_stock['cantidad']} unidades")
    print("\nSubtotales:")
    for producto in inventario:
        print(f"  {producto['nombre']}: ${subtotal(producto)}")

    pauseScreen()

def buscar_producto(inventario):
    """
    Busca un producto por nombre y muestra sus datos.
    Parámetros: lista de diccionarios donde se guardan los productos
    Retorno: None
    """
    buscar = input('Que producto desea buscar?\n ').strip()
    
    print(f"Buscando: '{buscar}'")
    for producto in inventario:
        if producto['nombre'] == buscar.capitalize():
            print('Producto encontrado')
            print(f"Nombre: {producto['nombre'].capitalize()}")
            print(f"precio: {producto['precio']}")
            print(f"cantidad: {producto['cantidad']}")
            return
    print("El producto no se encontro")
    
def actualizar_producto(inventario):
    """
    Actualiza precio, cantidad o nombre de un producto existente.
    Parámetros: lista de diccionarios donde se guardan los productos
    Retorno: None
    """
    buscar = input("Que producto desea actualizar?\n").lower().strip()
    
    for producto in inventario:
        if producto['nombre'] == buscar.capitalize():
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
    """
    Elimina un producto del inventario por nombre.
    Parámetros: lista de diccionarios donde se guardan los productos
    Retorno: None
    """
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


def salir():
    """
    Termina el programa.
    Parámetros: ninguno
    Retorno: contnuar = "no" es para poder terminar el programa
    """
    continuar = "no"
    print("Has salido del menu de inventario, vuelva pronto")
    return continuar
        


# Este bloque solo se ejecuta si este archivo se ejecuta directamente    
if __name__ == "__main__": 
    agregar_producto()
    mostrar_inventario()
    calcular_estadisticas()
                
                        
                
                