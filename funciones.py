# Importamos la lista donde se guardan los productos
from diccionario_producto import inventario
    

# Función para agregar productos
def agregar_producto():
    
    # Variable de control para repetir el menú
    continuar = "si"
    
    # Ciclo para agregar varios productos
    while continuar == "si":
        
        # Pedimos nombre del producto
        nombre_producto = input("Ingrese el nombre del producto\n")
        
        # Validamos que solo tenga letras
        if not nombre_producto.replace(" ", "").isalpha():
                print("Solo se pueden colocar letras")
                continue # Vuelve a pedir el nombre
            
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
        producto = {
            'nombre': nombre_producto,
            'precio': precio,
            'cantidad': cantidad          
            }
                
                
        # Guardamos el producto en la lista inventario        
        inventario.append(producto)
                
        # Preguntamos si desea seguir agregando productos
        continuar = input("\nDesea seguir agregando productos? (Si/No)\n").lower()
        
# Función para mostrar el inventario        
def mostrar_inventario():
    
    # Si el inventario está vacío
    if len(inventario) == 0:
        print("Aun no hay nada ")
        return
    
    else:
        print("----INVENTARIO----")
        
        # Recorremos la lista de productos
        for producto in inventario:
            print(f"producto: {producto['nombre']} | precio: {producto['precio']} | cantidad: {producto['cantidad']}" )
            print()
            
# Función para calcular estadísticas            
def calcular_estadisticas():
    
    cantidad_total = 0 # Total de productos
    valortotal = 0 # Valor total del inventario
    
    # Recorremos el inventario
    for producto in inventario:
        cantidad_total += producto["cantidad"]
        valortotal += producto["precio"] * producto["cantidad"]
        
    # Mostramos resultados    
    print(f"La cantidad total de productos registrados es: {cantidad_total}\n")
    print(f"El valor total del inventario es: {valortotal}\n")        
            

# Este bloque solo se ejecuta si este archivo se ejecuta directamente    
if __name__ == "__main__": 
    agregar_producto()
    mostrar_inventario()
    calcular_estadisticas()
                
                        
                
                
        
                    
                

    
    
                


