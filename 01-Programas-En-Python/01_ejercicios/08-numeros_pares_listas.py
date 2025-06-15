#   Creado por: Osamudio
#   Fecha: 17-abril-2025
#   Descripción: Crear un programa en python con
#   una lista de números y carge una lista con
#   los números que son pares y otra impares

from os import system
system("cls")

# Declaración de variables
# Primer algoritmo para identificar números pares e impares
numeros = [1, 3, 4, 2, 5, 6, 8, 10]
pares = list(filter(lambda par: par % 2 == 0, numeros))
impares = list(filter(lambda impar: impar % 2 == 1, numeros))

# Imprime la nueva lista
print(f"Lista original: {numeros}")
print(f"Lista pares: {pares}")
print(f"Lista impares: {impares}")

# Segundo algoritmo para identificar números pares e impares
print("----------------------------------------------")
numeros = [1, 3, 4, 2, 5, 6, 8, 10]
num_pares = list()
num_impares = list()
for num in numeros:
    if num % 2 == 0:
        num_pares.append(num)
    else:
        num_impares.append(num)

# Imprime la nueva lista
print(f"Lista original: {numeros}")
print(f"Lista pares: {pares}")
print(f"Lista impares: {impares}")

# Eliminación de variables
del pares
del impares
del numeros
del num_impares
del num_pares
