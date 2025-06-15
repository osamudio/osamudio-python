#    Creado por: Osamudio
#    Fecha: 01-abril-2025
#    Descripción: Se explica el concepto de desempaquetamiento
#                 técnica que permite asignar los elementos de
#                 una estructura de datos a variables

from os import system
system("cls")

# Declaración de variables
# Creado tuplas con la función tuple()
tupla_persona = ("Lionel", "Degracia", 47, 1.64, 200)

# Desempaquetado de una tupla
nombre, apellido, edad, estatura, peso = tupla_persona
print(tupla_persona)
print(f" - Nombre : {nombre}")
print(f" - apellido: {apellido}")
print(f" - Edad : {edad}")
print(f" - Estatura: {estatura}")
print(f" - Peso: {peso}")
