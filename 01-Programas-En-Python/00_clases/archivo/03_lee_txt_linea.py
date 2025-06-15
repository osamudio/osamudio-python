#   Creado por: Osamudio
#   Fecha: 06-Mayo-2025
#   Descripción: Lee el contenido de un archivo de texto
#                línea por línea

from os import system
system("cls")

# Declaración de variables
try:
    archivo = open("00_clases\\archivo\\cmo.txt", encoding="UTF-8")
    linea_archivo = archivo.readline()

    # Imprime el contenido de la linea eliminando
    # espacios en blanco al final
    while linea_archivo:
        print(linea_archivo.strip())
        linea_archivo = archivo.readline()

    # Cierre del archivo
    archivo.close()

    # Eliminación de variables
    del archivo
    del linea_archivo
except FileNotFoundError:
    print("El archivo '00_clases\\archivo\\cmo.txt' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
