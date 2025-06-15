#    Creado por: Osamudio
#    Fecha: 27-marzo-2025
#    Descripción: Métodos para manipular diccionarios

from os import system
system("cls")

print("------------------------------------------------------------")

# Declaración de variables
diccionario_casa = {
    'id': 1,
    'urbanizacion': "Hato Montaña",
    'calle': "3 Norte",
    'color': "Blanco Hueso",
    'techo': "Rojo",
    'ventana': "Francesas"
}
print(diccionario_casa)

# Agrega una nueva llave al diccionario
diccionario_casa["puerta"] = "Rojo"
diccionario_casa["puerta"] = "Amarillo"
print(diccionario_casa)

# método get(): devuelve el elemento de la llave
# Nota: No devuelve excepción su no encuentra el valor
elemento_casa = diccionario_casa.get("puerta")
print(elemento_casa)

# metodo items(): devuelve una lista de tuplas
lista_casas = diccionario_casa.items()
print(lista_casas)

# método key(): devuelve la lista de las key
# del diccionario
lista_llave = diccionario_casa.keys()
print(lista_llave)

# método value(): devulve la lista de los valores
# del diccionario
lista_valor = diccionario_casa.values()
print(lista_valor)

# método pop(): eliminar un elemento del diccionario
# Nota: elimina utilizando el key
diccionario_casa.pop('id')
print(diccionario_casa)


# método clear(): elimina los elementos del diccionario
diccionario_casa.clear()
print(diccionario_casa)

# Eliminación de variables
del diccionario_casa
del lista_casas
del lista_llave
del lista_valor
