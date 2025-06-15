#    Creado por: Osamudio
#    Fecha: 27-marzo-2025
#    Descripción: Métodos set y frozenset para crear conjuntos

from os import system
system("cls")

# Declaración de variables
# Creación de un conjunto función set()
conjunto_numero = set([1, 2, 3, 4, 5])
print(conjunto_numero)
print(type(conjunto_numero))

# Creación de un conjunto dentro de otro conjunto
# metodo frozenset()
conjunto_inicial = frozenset([2, 4, 6, 8])
conjunto_resultado = set({conjunto_inicial, 3, 5, 7})
print(conjunto_resultado)

# Eliminación de variables
del conjunto_numero
del conjunto_inicial
del conjunto_resultado
