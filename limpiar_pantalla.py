import os

# Función para limpiar la consola
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Se ejecuta solo si se corre este archivo directamente
if __name__ == "__main__":
    limpiar_pantalla()