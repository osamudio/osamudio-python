#   Creado por: Osamudio
#   Fecha: 26-abril-2025
#   Descripción: Programa para mostrar los ejemplos
#                de conversiones numéricas

from os import system
system("cls")

# Declaración de variables
# Convertir un número decimal a binario
numero_decimal = 10
numero_binario = bin(numero_decimal)
print(f"El número decimal {numero_decimal} en binario es {numero_binario}")
# Output:  '0b1010'

# Convertir de binario a decimal
numero_binario = "1010"
numero_decimal = int(numero_binario, 2)
print(f"El número binario {numero_binario} en decimal es {numero_decimal}")
# Output: 10

# Convertir de decimal a octal
numero_decimal = 10
numero_octal = oct(numero_decimal)
print(f"El número decimal {numero_decimal} en octal es {numero_octal}")
# Output: '0o12'

# Convertir de Octal a decimal
numero_octal = "12"
numero_decimal = int(numero_octal, 8)
print(f"El número octal {numero_octal} en decimal es {numero_decimal}")

# Convertir de decimal a hexadecimal
numero_decimal = 10
numero_hexa = hex(numero_decimal)
print(f"El número decimal {numero_decimal} en hexadecimal es {numero_hexa}")
# Output: '0xa'

numero_hexa = 'a'
numero_decimal = int(numero_hexa, 16)
print(f"El número hexadecimal {numero_hexa} en decimal es {numero_decimal}")
# Output: 10

# Eliminación de variables
del numero_decimal
del numero_binario
del numero_octal
del numero_hexa
