#   Creado por: Osamudio
#   Fecha: 04-Junio-2025
#   Descripción: Práctica de expresiones regulares

import re
from os import system
system("cls")

# Declaración de variables
texto = "The quick brown fox jumps over de lazy dog"
valor = re.findall(r"^The.*dog$", texto)
if valor:
    print(f"El valor es: {valor}")
else:
    print("No se encuentra en patrón de texto")

# Eliminación de variables
del texto
del valor
