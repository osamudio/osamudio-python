#    Creado por: Osamudio
#    Fecha: 27-marzo-2025
#    Descripción: Uso del metodo isdisjoin

from os import system
system("cls")

# Declaración de variables
conjunto_numero = {1, 2, 3, 4}
lista_numero = [5, 6]

# Valida si un elemento del conjunto forma
# forma parte de la lista.
resultado = conjunto_numero.isdisjoint(lista_numero)
print(conjunto_numero)
print(lista_numero)
if resultado:
    print("No hay elementos en común")
else:
    print("Hay elementos en común")

# Eliminación de variables
del conjunto_numero
del lista_numero
del resultado
