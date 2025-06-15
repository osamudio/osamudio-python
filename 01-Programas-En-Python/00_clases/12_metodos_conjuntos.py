#    Creado por: Osamudio
#    Fecha: 27-marzo-2025
#    Descripción: Métodos para manipulación de conjuntos

from os import system
system("cls")

# Declaración de variables
print("-----------------------------------------------------------------")
conjunto_herramientas = set({"martillo", "taladro", "destornillador", "pinza"})
print(conjunto_herramientas)

# metodo add(): agrega un elemento al conjunto
conjunto_herramientas.add("pala")
print(conjunto_herramientas)

# método update(): agrega elementos al conjunto
conjunto_herramientas.update(["mazo", "alicate"])
print(conjunto_herramientas)

# método remove(): elimina un elemento del conjunto
# Envía una excepción si el elemento no existe
conjunto_herramientas.remove("martillo")
print(conjunto_herramientas)

# método discard(): elimina un elemento del conjunto
conjunto_herramientas.discard("alicate")
print(conjunto_herramientas)

# método pop(): elimina un elemento del conjunto
# Nota: es un elemento aleatorio
elemento_eliminado = conjunto_herramientas.pop()
print(conjunto_herramientas)
print(elemento_eliminado)

# método clear(): elimina los elementos del conjunto
conjunto_herramientas.clear()
print(conjunto_herramientas)

# Eliminación de variables
del conjunto_herramientas
del elemento_eliminado
