#    Creado por: Osamudio
#    Fecha: 02-abril-2025
#    Descripción: ejemplo del usod de la función tuple()

from os import system
system("cls")

# Declaración de variables
# Creando una tupla con la función tuple()
lista_numero = list([1, 2, 3, 4, 5])
tupla_numero = tuple(lista_numero)
print(tupla_numero)

# Creando una tupla sin parentesis
tupla_impares = 1, 3, 5, 7
print(tupla_impares)

# Creando una tupla con un solo elemento
tupla_precio = 1.89,
print(tupla_precio)
tupla_precio = tuple([1.89])
print(tupla_precio)

# Creando una tupla a partir de una cadena
tupla_persona = tuple("Carlos")
print(tupla_persona)

# Creadno una tupla vacia
tupla_vacia = tuple()
print(tupla_vacia)

# Eliminación de varibles
del lista_numero
del tupla_numero
del tupla_precio
del tupla_persona
del tupla_vacia
