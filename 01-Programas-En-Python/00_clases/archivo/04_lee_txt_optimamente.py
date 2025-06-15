#   Creado por: Osamudio
#   Fecha: 06-Mayo-2025
#   Descripción: Leer un archivo en python de manera
#                óptima.

from os import system
system("cls")

# Declaración de variables

# Abre el archivo para leer su contenido
# Nota: Con with open() no es neceario cerrar el archivo
# Abre el archivo en modo de lectura por defecto
with open("00_clases\\archivo\\cmo.txt", encoding="UTF-8") as archivo:
    contenido_archivo = archivo.read()
    print(contenido_archivo)

# Eliminación de variables
del contenido_archivo
del archivo
