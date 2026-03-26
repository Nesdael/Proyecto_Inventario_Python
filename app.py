from colors import *
from extras import cargando, deleteScreen, pauseScreen
from menu import menu
from services import *


# Variable de control para repetir el menú
continuar = "si" 
# Ciclo que mantiene el programa en ejecución
while continuar == "si":
    deleteScreen()  # Limpia la consola
    print("Presiona la opcion 8 para cargar los productos guardados")
    opcion = menu()
    # Evaluamos la opción elegida
    if opcion == 1:
        deleteScreen()
        agregar_producto() # Llamamos la función
    elif opcion == 2:
        deleteScreen()
        mostrar_inventario() # Llamamos la función
        pauseScreen()
    elif opcion == 3:
        deleteScreen()
        calcular_estadisticas() # Llamamos la función
        pauseScreen()
    elif opcion == 4:
        deleteScreen()
        buscar_producto()
        pauseScreen()
    elif opcion == 5:
        deleteScreen()
        actualizar_producto()
        pauseScreen()
    elif opcion == 6:
        deleteScreen()
        eliminar_producto()
        pauseScreen()
    elif opcion == 7:
        deleteScreen()
        guardar_inventario()
        pauseScreen()
    elif opcion == 8:
        deleteScreen()
        cargar_inventario()
        pauseScreen()  
    elif opcion == 9:   
        continuar = salir()
    else:
        print("Ingrese una opcion valida")
        pauseScreen()
        continue    # Vuelve al inicio del menú
    # Mensaje final al salir del ciclo
print("\nGracias por utilizarlo, hasta luego")         