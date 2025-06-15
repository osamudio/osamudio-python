#   Creado por: Osamudio
#   Fecha: 28-marzo-2025
#   Descripción: Ejemplo de listas anidadas

from os import system
system("cls")

# Declaración de variables
lista_lenguajes = list(["python", "goland", "java", "docnet"])
print(lista_lenguajes)

# Declaración de la lista_programacion
lista_programacion = list([lista_lenguajes, "UTP", "SIS-701"])
print(lista_programacion)

# Imprime el primer elemento de la lista_programacion
# y el segundo elemento de la lista_lenguajes
selecciona_lenguaje = lista_programacion[0][0]
print(selecciona_lenguaje)
selecciona_lenguaje = lista_programacion[0][1]
print(selecciona_lenguaje)
selecciona_lenguaje = lista_programacion[0][2]
print(selecciona_lenguaje)
selecciona_lenguaje = lista_programacion[0][3]
print(selecciona_lenguaje)

# Ejemplo de operaciones con lista
lista = [1, 2, 3]
print(lista * 2)
