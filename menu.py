from colors import *

def menu():

    print(f"{F_VERDE}--- Menu de inventario ---{RESET}")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Estadisticas")
    print("4. Buscar producto")
    print("5. Actualizar producto")
    print("6. Eliminar producto")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    # Pedimos al usuario una opción
    try:
        opcion = int(input("Que opcion desea realizar?\n"))
    except ValueError:
        print("Error: Ingrese solo numeros")
        input("Presione una tecla...") 
    return opcion
    