#    Creado por: Osamudio
#    Fecha: 05-abril-2025
#    Descripción: Métodos y funciones para iterar
#                 mediante el ciclo for

from os import system
system("cls")

# Declaración de variables

print("----------------------------------------------")
# Imprimir numeros del 1 al 10
for numero in range(5):
    print(f"El número es: {numero}")

# Imprimir numeros del 1 al 10
for numero in range(1, 11):
    print(f"El número es: {numero}")

# Imprimir numeros del 5 al 9
for numero in range(5, 10):
    print(f"El número es: {numero}")
else:
    print("Se acabaron los elementos")

# Ejemplo ciclo for con sentencia continue y else
# Imprime todas las frutas menos limón
# el "continue" lo que realiza es un salto al
# inicio del siguiente ciclo for.
lista_frutas = ["sandia", "melon", "granadilla", "limón"]
for fruta in enumerate(lista_frutas):
    indice, elemento = fruta
    if elemento == "granadilla":
        continue
    else:
        print(f"En el indice {indice} la fruta es : {elemento}")
else:
    print("No hay más frutas")

# Ejemplo ciclo for con sentencia break
# Imprime que se comerá una pera
# si se la come se sentira mal, no debe comer más
# frutas
# inicio del siguiente ciclo for.
lista_frutas = ["sandia", "pera", "melon", "limón", "manzana"]
for fruta in enumerate(lista_frutas):
    indice, elemento = fruta
    print(f"Indice : {indice}, Me comeré la fruta: {elemento}")
    if elemento == "pera":
        break
else:
    print("No hay más frutas")

print("No puede comer mas frutas")

# Eliminación de variables
del numero
del fruta
del lista_frutas
del indice
del elemento
