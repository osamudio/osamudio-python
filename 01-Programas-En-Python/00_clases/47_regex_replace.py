#   Creado por: Osamudio
#   Fecha: 04-Junio-2025
#   Descripción: Práctica de expresiones regulares
#                Reemplazar las vocales por asterisco

import re
from os import system
system("cls")

# Declaración de variables
text = "Reemplazando todas las vocales por asteriscos en una cadena"

new_text = re.sub("[aeiou]", "*", text)

# Imprime el nuevo texto
print(f"Texto inicial: {text}")
print(f"Texto nuevo: {new_text}")

# Eliminación de variables
del text
del new_text
