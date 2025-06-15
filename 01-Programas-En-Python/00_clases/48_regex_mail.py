#   Creado por: Osamudio
#   Fecha: 04-Junio-2025
#   Descripción: Práctica de expresiones regulares
#                Validar una cadena con email

import re
from os import system
system("cls")

# Declaración de variables
email = "example_01@sindominio.com"

# Define el patron a buscar
pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%.-]+\.[a-zA-Z]{2,}"

result = re.match(pattern, email)

# Imprime el nuevo texto
if result:
    print(f"La cadena de correo es valida : {email}")
else:
    print(f"La cadena de correo No es valida : {email}")

# Eliminación de variables
del email
del pattern
del result
