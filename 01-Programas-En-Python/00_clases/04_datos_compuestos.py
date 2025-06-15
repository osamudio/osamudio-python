#   Creado por: Osamudio
#   Fecha : 24-03-2025
#   Descripción: Declaración de datos compuestos

# Declaración de list(listas)
# Nota: Puede contener diferentes datos y se puede modificar
lista_usuario = ["Lionel Samudio", "Sysadmin Aix", 47, 1.64, 200]
# Imprimir toda la lista
print(lista_usuario)
# Imprimir el elemento 1 de la lista
print(lista_usuario[0])
# Imprimir el elemento 2 de la lista
lista_usuario[1] = "Especialista Cloud"
print(lista_usuario[1])

# Declaración de una tupla
# Nota: Puede contener diferentes datos y no se puede modificar los elementos
tupla_universidad = ("Tecnológica", "Panamá", "Latina", "Istmo")
print(tupla_universidad)
# Imprimir elemento 1 de la tupla
print(tupla_universidad[0])
# Imprimir elemento 2 de la tupla
print(tupla_universidad[1])

# Nota: Puedes volver a declarar la tupla
tupla_universidad = ("Ulacit", "Panamá", "Latina", 90210)
print(tupla_universidad)
# Imprimir elemento 1 de la tupla
print(tupla_universidad[0])

# Declaración de un set(conjunto)
# Nota: No tienen orden fijo, No se puede acceder por indices
#       Los elementos no pueden cambiar.
#       No permite elementos duplicados
conjunto_fruta = {"Manzana", "Pera", "Sandia", "Uva", 10}
print(conjunto_fruta)

# Declaración de un dictionary(diccionario)
# La estructura es key(llave) : value(valor)
diccionario_usuario = {
    'id': 200,
    'nombre': "Oscar Samudio",
    'usuario': "osamudio",
    'grupo': "staff",
    'shell': "/usr/bin/bash"
}
# Imprimir el contenido del diccionario
print(diccionario_usuario)
# Imprimir el elemento 1 del diccionario
print(diccionario_usuario["usuario"])
diccionario_usuario["usuario"] = "leonsam"
print(diccionario_usuario["usuario"])

# Eliminación de variables
del lista_usuario
del tupla_universidad
del conjunto_fruta
del diccionario_usuario
