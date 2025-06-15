#    Creado por: Osamudio
#    Fecha: 01-abril-2025
#    Descripción: Se explica el concepto de desempaquetamiento
#                 técnica que permite asignar los elementos de
#                 una estructura de datos a variables

from os import system
system("cls")

# Declaración de variables
# Declaración del diccionario persona
diccionario_persona = {
    'nombre': "Lionel",
    'apellido': "Degracia",
    'edad': 47,
    'estatura': 1.64,
    'peso': 200
}


# Desempaquetado de un diccionario
# nombre, apellido, edad, estatura, peso = diccionario_persona.keys()
# nombre, apellido, edad, estatura, peso = diccionario_persona.items()
nombre, apellido, edad, estatura, peso = diccionario_persona.values()

print(diccionario_persona)
print("Los datos de la persona son:")
print(f" - Nombre : {nombre}")
print(f" - Apellido: {apellido}")
print(f" - Edad: {edad}")
print(f" - Estatura: {estatura}")
print(f" - Peso: {peso}")

# Desempaquetado de un diciconario con *corporal
# Nota: la variable corporal toma el resto de valores
# para lograrlo hay que colocar el * previo a la variable
# nombre, apellido, *corporal = diccionario_persona.items()
# nombre, apellido, *corporal = diccionario_persona.keys()

nombre, apellido, *corporal = diccionario_persona.values()
print(diccionario_persona)
print(f" - Nombre : {nombre}")
print(f" - Apellido: {apellido}")
print(f" - Corporal : {corporal}")

# Eliminación de variables
del diccionario_persona
del nombre
del apellido
del edad
del estatura
del peso
del corporal
