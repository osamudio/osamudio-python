#   Creado por: Osamudio
#   Fecha: 04-Junio-2025
#   Descripción: Práctica de expresiones regulares
#                Validar una cadena con un URL

import re
from os import system
system("cls")

# Declaración de variables
url = """Esto es un ejemplo de una página Web:
         https://www.example.com y también
         podemos ver http://www.example.org"""

# Define el patron a buscar
pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.findall(pattern, url)

# Imprime el nuevo texto
print(result)

# Eliminación de variables
del url
del pattern
del result
