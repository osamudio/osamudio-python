#    Creado por: Osamudio
#    Fecha: 25-marzo-2025
#    Descripción: Métodos para manipular tuplas

# Declaración de variables

# Declaración de una tupla
tupla_arboles = ("roble", "caoba", "cedro", "caoba", "pinotea", "espabe")
print(tupla_arboles)
print(tupla_arboles[0])

# función dir():
# resultado = dir(tupla_arboles)
# print(resultado)

# función len(): devuelve la lontiud de la tupla
longitud_tupla = len(tupla_arboles)
print(longitud_tupla)

# Método count(): devuelve la cantida de veces
# que aparece un elemento en la tupla
valor_encontrado = tupla_arboles.count("caoba")
print(valor_encontrado)
