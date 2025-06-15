#    Creado por: Osamudio
#    Fecha: 05-abril-2025
#    Descripción: Métodos y funciones para iterar
#                 una tupla

from os import system
system("cls")


# Declaración de variables
print("--------------------------------------------------")
tupla_animales = ("perro", "gato", "loro", "cocodrilo")
tupla_numeros = (2, 4, 6, 8)
print("Los animales son:")
print(f" - {tupla_animales[0]}")
print(f" - {tupla_animales[1]}")

# Iterando una tupla con ciclo for
# La variable animal tiene el valor
# del elemento de la tupla
print("--------------------------------------------------")
print("Los animales son:")
for animal in tupla_animales:
    print(f" - {animal}")


# Iterando más de una tupla sta al mismo tiempo
# Nota: Deben tener la misma cantidad de elementos
print("--------------------------------------------------")
for numero, animal in zip(tupla_numeros, tupla_animales):
    print(f"El numero es: {numero}")
    print(f"El animal es: {animal}")

# Forma correcta de recorrer la tupla con su indice
print("--------------------------------------------------")
for numero in enumerate(tupla_numeros):
    indice, valor = numero
    print(f"En el indice {indice} es valor es: {valor}")

# Otra forma de recorrer la tupla con su indice
print("--------------------------------------------------")
for numero in enumerate(tupla_numeros):
    indice = numero[0]
    valor = numero[1]
    print(f"En el indice {indice} es valor es: {valor}")

# Eliminación de variables
del tupla_animales
del tupla_numeros
del animal
del indice
del valor
del numero
