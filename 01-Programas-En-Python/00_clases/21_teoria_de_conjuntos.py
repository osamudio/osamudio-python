#    Creado por: Osamudio
#    Fecha: 04-abril-2025
#    Descripción: Teoría de conjuntos validando si un
#    conjunto es subconjunto o superconjunto de otro.
#    Valida si un conjunto tiene elementos del otro.

from os import system
system("cls")

# Declaración de variables

# Validando si el conjunto_numero2 es subconjunto
# del conjunto_numero1
conjunto_numero1 = {1, 2, 3, 4, 5}
conjunto_numero2 = {1, 3, 5}
# Primera forma de validar
# resultado = conjunto_numero2.issubset(conjunto_numero1)
# Segunda forma de validar
resultado = conjunto_numero2 <= conjunto_numero1
if resultado:
    print(f"El {conjunto_numero2} es un subconjunto de {conjunto_numero1}")
else:
    print(f"El {conjunto_numero2} no es subconjunto de {conjunto_numero1}")

# Validando si el conjunto_numero1 es superconjunto
# del conjunto_numero2
conjunto_numero1 = {1.0, 2.0, 3.0, 4.0, 5.0}
conjunto_numero2 = {1.0, 3.0, 5.0}
# Primera forma de validar
# resultado = conjunto_numero1.issuperset(conjunto_numero2)
# Segunda forma de validar
resultado = conjunto_numero1 > conjunto_numero2
if resultado:
    print(f"El {conjunto_numero1} es un superconjunto de {conjunto_numero2}")
else:
    print(f"El {conjunto_numero1} no es superconjunto de {conjunto_numero2}")

# Verificar si hay un número en común
conjunto_nombre1 = {"oscar", "leo", "david", "juan"}
conjunto_nombre2 = {"carlos", "leonel"}
resultado = conjunto_nombre2.isdisjoint(conjunto_nombre1)
if resultado:
    print(f"El {conjunto_nombre2} no tiene elementos de {conjunto_nombre1}")
else:
    print(f"El {conjunto_nombre2} tiene elementos de {conjunto_nombre1}")

# Eliminación de variables
del conjunto_numero1
del conjunto_numero2
del conjunto_nombre1
del conjunto_nombre2
del resultado
