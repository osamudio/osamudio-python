#    Creado por: Osamudio
#    Fecha: 06-abril-2025
#    Descripción: Métodos y funciones para iterar
#                 un conjunto (set)

from os import system
system("cls")

# Declaración de variables
print("--Inicio -----------------------------------------")
set_animales = {"perro", "gato", "loro", "cocodrilo"}
set_numeros = {2, 4, 6, 8}

# Iterando un conjunto con ciclo for
# La variable animal tiene el valor
# del elemento del conjunto
print("--------------------------------------------------")
print("Los animales son:")
for animal in set_animales:
    print(f" - {animal}")


# Iterando más de un conjunto al mismo tiempo
# Nota: Deben tener la misma cantidad de elementos
print("--------------------------------------------------")
for numero, animal in zip(set_numeros, set_animales):
    print(f"El numero es: {numero}")
    print(f"El animal es: {animal}")

# Forma correcta de recorrer el conjunto con su indice
print("--------------------------------------------------")
for numero in enumerate(set_numeros):
    indice, valor = numero
    print(f"En el indice {indice} es valor es: {valor}")

# Otra forma de recorrer el conjunto con su indice
print("--------------------------------------------------")
for numero in enumerate(set_numeros):
    indice = numero[0]
    valor = numero[1]
    print(f"En el indice {indice} es valor es: {valor}")

# Eliminación de variables
del set_animales
del set_numeros
del animal
del indice
del valor
del numero
