from os import system
import sys
import time


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
    deleteScreen()
    pauseScreen()