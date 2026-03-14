print("Bienvenido a nuestro inventario")

# Variable de control para repetir el registro de productos
continuar = "si"

# Mientras continuar no sea diferencia a "si" el ciclo continuara hasta que este sea negativo
while continuar == "si":
    # Se le pide al usuario que agregue un producto
    nombre = str(input("Ingrese el nombre del producto\n"))
    # Si el usuario ingresa un digito en lugar de una letra le saltara este if, y el .replace permite letras y espacios
    # Por que .isalpha no permite espacios
    if not nombre.replace(" ", "").isalpha():
        print("Solo se pueden colocar letras")
        continue
    
    # Validación del precio (debe ser un número decimal)
    while True:
        try:
            # Se le pide al usuario que ingrese un precio del producto unitario
            precio = float(input("Ingrese el precio unitario del producto\n"))
            if precio <= 0:
                print("Error: No se puede colocar 0")
                continue
            break
        except ValueError:
                print("Error: Favor solo ingresar digitos")
                
        
    # Validación del precio (debe ser un número decimal)
    while True:
        try:
            # Se le pide al usuario que ingrese la cantidad que desea del producto
            cantidad = int(input("Ingrese la cantidad que desea del producto\n"))
            if cantidad <= 0:
                print("Error: No se puede colocar 0")
                continue
            break
        except ValueError:
                print("Error: Por favor solo ingresar numeros")
                
    # Calcula el costo total del producto
    total_costo = precio * cantidad
    print("")
    print("==========================================")
    print("")
    
    print("Factura")
    print(f"Producto: {nombre.capitalize()} | Precio: {round(precio, 2)} | Cantidad: {cantidad}")
    print(f"Costo total de los produdctos: {total_costo}" )
    
    print("")
    print("==========================================")
    print("")
    
    # Preguntar al usuario si desea registrar otro producto
    continuar = input("\n¿Desea registrar otro producto? (si/no): ").lower()
    
    # Mensaje final al salir del programa
    if continuar != "si":
        print("Gracias por utilizar nuestro inventario")