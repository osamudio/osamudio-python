#   Creado por: Osamudio
#   Fecha : 24-03-2025
#   Descripción: Métodos para manipular list(listas)

from os import system
system("cls")

# Declaración de variables

print("------------------------------------------------------------")
# Función list(): crea una lista
lista_frutas = list(["manzana", "pera", "uva", "sandia", "melon", "limon"])
print(lista_frutas[0])

# Función len(): devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista_frutas)
print(f"La cantidad de elementos de la lista es : {cantidad_elementos}")
print(lista_frutas)

# "slicing" (rebanado) de listas.
# Permite extraer una porción de una lista
# lista[a:b] o lista[indicea:indiceb]
# Nota: El indiceb se excluye de la nueva lista
lista_postre = lista_frutas[1:4]
print(lista_postre)

# Extraer una copia completa de la lista
lista_postre = lista_frutas[:]
print(lista_postre)

# Método append(): agregar un elemento a la lista
lista_frutas.append("piña")
print(lista_frutas)

# Método insert(): agrega un elemento en un indice especifico
lista_frutas.insert(2, "fresas")
print(lista_frutas)

# Método extend() : agrega varios elementos a la lista
# Nota: Lo que realiza es unir dos listas
otras_frutas = list(["naranja", "mora"])
lista_frutas.extend(otras_frutas)
print(f"Une dos listas: {lista_frutas}")

# Método pop(): elimina un elemento de la lista por su indice
# Nota: Si coloca el indice (-1) elimina el ultimo elemento.
#       Si coloca el indice (-2) elimina el penultimo elemento
lista_frutas.pop(1)
print(lista_frutas)


# Método remove(): elimina un elemento por su valor
lista_frutas.remove("mora")
print(lista_frutas)

# Método clear(): elimina todos los elementos de la lista
lista_frutas.clear()
print(lista_frutas)

# Método sort(): Ordena la lista en forma ascendente
lista_numeros = list([1, 2, 5, 7, 0, 9, 10, True, False])
lista_numeros.sort()
print(lista_numeros)
# Método sort(): Ordena la lista en forma descendente
lista_numeros.sort(reverse=True)
print(lista_numeros)

# Método reverse(): invierte los elementos de la lista
lista_numeros = list([1, 2, 5, 7, 0, 9, 10, True, False])
lista_numeros.reverse()
print(lista_numeros)

# Método index(): devuele el indice donde se encuentra
# un elemento de la lista
# Busca el elemento 10 de la lista de números
elemento_encontrado = lista_numeros.index(10)
print(elemento_encontrado)
