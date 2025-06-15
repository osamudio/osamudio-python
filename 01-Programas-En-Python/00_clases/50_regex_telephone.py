#   Creado por: Osamudio
#   Fecha: 04-Junio-2025
#   Descripción: Práctica de expresiones regulares
#                Reemplazar una cadena con un patrón

import re
from os import system
system("cls")

# Declaración de variables
text = "Saludos, los contactos son: +54 11 4321-4321 y +54 11 4421-4523"

# Patrón a buscar dd/mm/yyyy
pattern = r"\+\d{2}\s\d{2}\s\d{4}-\d{4}"

# Texto con el que se reemplazará el patrón
replacement = "+XX AA AEIO-UIEO"

# Reemplaza todas las apariciones del patron en la cadena de texto
new_text = re.sub(pattern, replacement, text)

# Imprime el nuevo texto
print(new_text)

# Eliminación de variables
del text
del pattern
del replacement
del new_text
