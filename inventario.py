# Importamos colores para darle estilo al menú
from colores import *

# Importamos función para limpiar la pantalla
from limpiar_pantalla import limpiar_pantalla

# Importamos funciones principales del sistema
from funciones import agregar_producto, mostrar_inventario, calcular_estadisticas


# Función principal del menú
def menu():
    
    # Variable de control para repetir el menú
    continuar = "si"
    
    # Ciclo que mantiene el programa en ejecución
    while continuar == "si":
        limpiar_pantalla()  # Limpia la consola
        
        # Mostramos las opciones del menú
        print(f"{F_VERDE}--- Menu de inventario ---{RESET}")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadisitcas")
        print("4. Salir")
    
        # Pedimos al usuario una opción
        try:
            opcion = int(input("Que opcion desea realizar?\n"))
        except ValueError:
            print("Error: Ingrese solo numeros")
            input("Presione una tecla...")
            continue 
    
    
        # Evaluamos la opción elegida
        if opcion == 1:
            limpiar_pantalla()
            print(f"{F_VERDE}Haz elegido la opcion agregar producto{RESET}\n")
            agregar_producto() # Llamamos la función
        elif opcion == 2:
            limpiar_pantalla()
            print(f"{F_VERDE}Haz elegido la opcion mostrar producto{RESET}\n")
            mostrar_inventario() # Llamamos la función
        elif opcion == 3:
            limpiar_pantalla()
            print(f"{F_VERDE}Haz elegido la opcion calcular estadisticas{RESET}\n")
            calcular_estadisticas() # Llamamos la función
        elif opcion == 4:
            print("Has salido del menu de inventario, vuelva pronto") 
            exit()
        else:
            print("Ingrese una opcion valida")
            input("Oprima cualquier boton para intentar de nuevo...")
            continue    # Vuelve al inicio del menú
        
        # Preguntamos si desea continuar
        continuar = input("\nDesea hacer otra consulta? (Si/No)\n").lower()
        
        # Mensaje final al salir del ciclo
        print("\nGracias por utilizarlo, hasta luego")
        

# Llamamos la función principal        
menu()               

# Este programa es un sistema de inventario desarrollado en Python.
# Permite al usuario agregar productos, visualizar el inventario y calcular
# estadísticas como la cantidad total y el valor total de los productos.
# El programa utiliza listas y diccionarios para almacenar la información
# y cuenta con validaciones para evitar errores en los datos ingresados.