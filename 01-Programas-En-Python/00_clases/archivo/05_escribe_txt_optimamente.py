#   Creado por: Osamudio
#   Fecha: 06-Mayo-2025
#   Descripción: Escribe un archivo en python de manera
#                óptima.

from os import system
system("cls")

# Declaración de variables

# Abre el archivo para leer su contenido
# Nota: Con with open() no es neceario cerrar el archivo
# Abre el archivo en modo de escritura "w"
with open("00_clases\\archivo\\soc.txt", "w", encoding="UTF-8") as archivo:
    # Escribe una linea en el archivo
    # archivo.write("El renacimiento de Optimus Prime")

    # Escribe información en el archivo
    # más de una línea
    archivo.writelines(["Teoría del reactor ARC\n",
                        "Creado por Osamudio\n"])
    # Si utilizo otro writelines() agrega más información
    # No lo sobre escribe
    archivo.writelines(["Teoría del reactor de Fusión\n",
                        "Creado por leosam\n"])

# Eliminación de variables
del archivo
