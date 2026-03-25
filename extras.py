from os import system
import sys
import time


def cargando(iteraciones):
    for i in range(iteraciones):
        puntos = "." * (i % 4)
        espacios = " " * (3- (i % 4))
        print(f"\rActualizando{puntos}{espacios}", end="")
        sys.stdout.flush()
        time.sleep(0.5)
        
    print("\n Todo actualizado")

def deleteScreen():
    if sys.platform == "linux" or sys.platform == "darwin":
        system("clear")
    else:
        system("cls")


def pauseScreen():
    if sys.platform == "linux" or sys.platform == "darwin":
        pause = input("Presione una tecla para continuar...")
    else:
        system("pause")

if __name__ == "__main__": 
    cargando()
    deleteScreen()
    pauseScreen()