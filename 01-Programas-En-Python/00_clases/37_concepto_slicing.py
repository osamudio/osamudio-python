#   Creado por: Osamudio
#   Fecha: 08-Mayo-2025
#   Descripción: Ejemplos del concepto de "slicing"
#                en cadenas, listas y otros objetos

from os import system
system("cls")

# Declaración de variables
# Nota: Recomendado utilizar este concepto con la libreria
# Panda (pd)

# Imprime desde la posición 2 hasta la posición 3
# Nota: No incluye la ultima posición es (n-1)
# concepto slicing numeros[inicio:fin-1]

# Imprimir numeros de la cadena "numeros"
numeros = "0123456789"
print(f"Los números son: {numeros[2:4]}")

# Imprimir los primeros 5 elementos de la cadena
nombre_completo = "Oscar Leonel Fagardo"

# Se realiza slicing desde la posición 0 a la 5
print(f"El nombre es: {nombre_completo[0:5]}")

# Realizando slicing con una lista de números
compras_comida = [1.68, 3.45, 2.50, 4.99, 3.99]
print(f"Lista compras comida: {compras_comida[0:3]}")

# Eliminación de variables
del nombre_completo
del numeros
del compras_comida
