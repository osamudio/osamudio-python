#   Creado por: Osamudio
#   Fecha: 27-abril-2025
#   Descripción: Ejemplos de manipulación de archivos txt
#                leer todas las líneas

# Importa el módulo "os" la función "system()"
from os import system
system("cls")

# Abre el archivo cmo.txt en el path indicado
archivo = open("00_clases\\archivo\\cmo.txt", encoding="UTF-8")

# Leel el contenido del archivo de todas las líneas
# Devuelve una lista y se utiliza con archivos pequeños
# ya que puede consumir la memoria RAM del equipo.
contenido_lineas = archivo.readlines()
print(contenido_lineas)

# Cierra el archivo después de ser utilizado
archivo.close()

# Eliminación de variables
del archivo
del contenido_lineas
