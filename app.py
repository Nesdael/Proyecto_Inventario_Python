from colors import *
from extras import cargando, deleteScreen, pauseScreen
from menu import menu
from archivos import *
from services import *

funciones = {
    "1": agregar_producto,
    "2": mostrar_inventario,
    "3": calcular_estadisticas,
    "4": buscar_producto,
    "5": actualizar_producto,
    "6": eliminar_producto,
    "7": guardar_inventario,
    "8": cargar_inventario,
}
# Variable de control para repetir el menú
continuar = "si" 
# Ciclo que mantiene el programa en ejecución
while continuar == "si":
    
    deleteScreen()  # Limpia la consola
    print("Presiona la opcion 8 para cargar los productos guardados")
    menu()
    opcion = input("Que opcion desea realizar?\n")
    # Evaluamos la opción elegida
    if opcion in funciones:
        funciones[opcion](inventario)
    elif opcion == "9":   
        continuar = salir()
    else:
        print("Ingrese una opcion valida")
        pauseScreen()
        continue    # Vuelve al inicio del menú
    # Mensaje final al salir del ciclo
print("\nGracias por utilizarlo, hasta luego")         