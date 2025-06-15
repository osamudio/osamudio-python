#   Creado por: Osamudio
#   Fecha: 04-Junio-2025
#   Descripción: Práctica de expresiones regulares
#                Reemplazar una cadena con un patrón

import re
from os import system
system("cls")

# Declaración de variables
text_date = "La fecha es 23/06/2025 y el teléfono es +1-555-555-5555"
text_phone = "La fecha es 23/06/2025 y el teléfono es +507-6570-0022"

# Patrón a buscar dd/mm/yyyy
pattern_date = r"\d{2}/\d{2}/\d{4}"
pattern_phone = r"\d{3}-\d{4}-\d{4}"
# Texto con el que se reemplazará el patrón
replacement_date = "01/06/2030"
replacement_phone = "507-6981-6455"

# Reemplaza todas las apariciones del patron en la cadena de texto
firts_text = re.sub(pattern_date, replacement_date, text_date)
second_text = re.sub(pattern_phone, replacement_phone, text_phone)

# Imprime el nuevo texto
print(f"New Text 01: {firts_text}")
print(f"New Text 02: {second_text}")


# Eliminación de variables
del text_date
del text_phone
del pattern_date
del pattern_phone
del replacement_date
del replacement_phone
del firts_text
del second_text