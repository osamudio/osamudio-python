#    Creado por: Osamudio
#    Fecha: 08-abril-2025
#    Descripción: Ejemplo del uso del ciclo while

from os import system
system("cls")

# Declaración de variables
cantidad_numeros = int(input("Introduzca la cantidad de números: "))
contador = 1
suma = 0
while contador <= cantidad_numeros:
    # contador = contador + 1
    contador += 1
    numero = int(input("Introduzca el número: "))
    # suma = suma + numero
    suma += numero

print(f"La suma de los número es: {suma}")

# Eliminación de variables
del cantidad_numeros
del contador
del numero
del suma
