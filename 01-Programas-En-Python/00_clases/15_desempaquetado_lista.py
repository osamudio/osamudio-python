#    Creado por: Osamudio
#    Fecha: 01-abril-2025
#    Descripción: Se explica el concepto de desempaquetamiento
#                 técnica que permite asignar los elementos de
#                 una estructura de datos a variables

from os import system
system("cls")

# Declaración de variables
lista_persona = list(["Lionel", "Degracia", 47, 1.64, 200])

# Desempaquetado de una lista list()
nombre, apellido, edad, estatura, peso = lista_persona
print(lista_persona)
print("Los datos de la persona son:")
print(f" - Nombre : {nombre}")
print(f" - apellido: {apellido}")
print(f" - Edad : {edad}")
print(f" - Estatura: {estatura}")
print(f" - Peso: {peso}")

# Desempaquetado de una lista utilizando *
lista_numero = [1, 2, 3, 4, 5]
primero, segundo, *resto, ultimo = lista_numero
print("Los datos de la lista son:")
print(f" - Primer valor: {primero}")  # Salida: 1
print(f" - Segundo valor: {segundo}")  # Salida: 2
print(f" - Resto valor: {resto}")  # Salida: [3, 4]
print(f" - Último valor: {ultimo}")  # Salida: 5

# Eliminación de variables
del nombre
del apellido
del edad
del estatura
del peso
del primero
del segundo
del resto
del ultimo
