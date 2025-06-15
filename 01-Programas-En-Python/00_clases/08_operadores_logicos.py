#   Creado por: Osamudio
#   Fecha : 24-03-2025
#   Descripción: Ejemplos de los operadores logicos
#                and , or, not

# Declaración de variables
# Ejemplo del operador and
# Nota: Imagine que son dos interruptores
# conectados en serie.
resultado1 = False & False
resultado2 = False & True
resultado3 = True & False
resultado4 = True & True

print("Resultado del operador AND")
print(f"Resultado de False & False : {resultado1}")
print(f"Resultado de False & True : {resultado2}")
print(f"Resultado de True & False : {resultado3}")
print(f"Resultado de True & True : {resultado4}")

# Ejemplo del operador or
# Nota: Imagine que son dos interruptores
# conectados en paralelo.
resultado1 = False | False
resultado2 = False | True
resultado3 = True | False
resultado4 = True | True

print("Resultado del operador OR")
print(f"Resultado de False & False : {resultado1}")
print(f"Resultado de False & True : {resultado2}")
print(f"Resultado de True & False : {resultado3}")
print(f"Resultado de True & True : {resultado4}")

# Ejemplo del operador not
resultado1 = not False
resultado2 = not True

print("Resultado del operador NOT")
print(f"Resultado de not False : {resultado1}")
print(f"Resultado de not True : {resultado2}")

# Eliminación de Variables
del resultado1
del resultado2
del resultado3
del resultado4
