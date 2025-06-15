#    Creado por: Osamudio
#    Fecha: 05-abril-2025
#    Descripción: Métodos y funciones para iterar
#                 una lista

from os import system
system("cls")

# Declaración de variables
list_animales = ["perro", "gato", "loro", "cocodrilo"]
list_numeros = [2, 4, 6, 8]
print("Los animales son:")
print(f" - {list_animales[0]}")
print(f" - {list_animales[1]}")

# Iterando una lista con ciclo for
# La variable animal tiene el valor
# del elemento de la lista
print("Los animales son:")
for animal in list_animales:
    print(f" - {animal}")

# Iterando más de una lista al mismo tiempo
# Nota: Deben tener la misma cantidad de elementos
for numero, animal in zip(list_numeros, list_animales):
    print(f"El numero es: {numero}")
    print(f"El animal es: {animal}")

# Forma correcta de recorrer la lista con su indice
for numero in enumerate(list_numeros):
    indice, valor = numero
    print(f"En el indice {indice} es valor es: {valor}")

# Otra forma de recorrer la lista con su indice
for numero in enumerate(list_numeros):
    indice = numero[0]
    valor = numero[1]
    print(f"En el indice {indice} es valor es: {valor}")

# For en una sola línea con listas
lista_numeros = [2, 4, 8, 10]
lista_numeros = [numero*2 for numero in lista_numeros]
print(lista_numeros)

# Eliminación de variables
del list_animales
del list_numeros
del animal
del indice
del valor
del numero
