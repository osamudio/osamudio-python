#   Creado por: Osamudio
#   Fecha: 27-abril-2025
#   Descripción: Ejemplos de manipulación de archivos txt
#                Leer el contenido completo del archivo

# Importa el módulo "os" la función "system()"
from os import system
system("cls")

# Abre el archivo cmo.txt en el path indicado
archivo = open("00_clases\\archivo\\cmo.txt", encoding="UTF-8")

# Lee el contenido completo del archivo y lo imprime
contenido_archivo = archivo.read()
print(contenido_archivo)

# Cierra el archivo después de ser utilizado
archivo.close()

# Eliminación de variables
del archivo
del contenido_archivo
