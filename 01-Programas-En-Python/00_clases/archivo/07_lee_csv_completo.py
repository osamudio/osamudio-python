#   Creado por: Osamudio
#   Fecha: 06-Mayo-2025
#   Descripción: Ejemplos de lectura de archivos csv

# importamos la libreria csv
import csv

from os import system
system("cls")

# Declaración de variables
# Abre el archivo en modo lectura "r" para leer el contenido
with open("00_clases\\archivo\\persona.csv", encoding="UTF-8") as archivo:
    # Nota: se recomienda manipular "csv" con librería panda
    contenido_archivo = csv.reader(archivo)
    for linea_archivo in contenido_archivo:
        print(linea_archivo)

# Eliminación de variables
del archivo
del contenido_archivo
del linea_archivo
