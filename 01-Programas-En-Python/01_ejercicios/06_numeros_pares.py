#    Creado por: Osamudio
#    Fecha: 08-abril-2025
#    Descripción: Validar si un numero es par o impar

from os import system


# Declaración de variables
# Una forma de realizarlo mediante el siguiente código
validar = 's'
while validar.upper() == 'S':
    system("cls")
    numero = int(input("Introduzca un numero entero: "))
    if numero % 2 == 0:
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")

    validar = input("Desea validar otro numero S/N : ")

# Eliminación de variables
del validar
del numero
