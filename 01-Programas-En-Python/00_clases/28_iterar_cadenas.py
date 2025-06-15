#    Creado por: Osamudio
#    Fecha: 08-abril-2025
#    Descripción: Métodos y funciones para iterar
#                 una cadenas

from os import system
system("cls")

# Declaración de variables
# Iterar un dato cadena
correo_corporativo = "oscarsam@correo.com"
for correo in enumerate(correo_corporativo):
    indice, letra = correo
    print(f"El indice {indice} tiene la letra {letra}")

# Otra forma de iterar una cadena
correo_corporativo = "oscarsam@correo.com"
for correo in correo_corporativo:
    print(f"La letra es: {correo}")

# Eliminación de variables
del correo_corporativo
del correo
