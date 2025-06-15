#    Creado por: Osamudio
#    Fecha: 05-abril-2025
#    Descripción: Métodos para manipulación
#                 de diccionarios

from os import system
system("cls")

# Declaración de variables
# Función dict() para crear un diccionario
dic_persona1 = dict(nombre="Leonel", apellido="Barrios")


# Otra manera de crear un diccionario
dic_persona = {
    'nombre': "Leonel",
    'apellido': "Barrios"
}

print(dic_persona1)
print(dic_persona)

# Crea un diccionario vacío
dic_vacio = dict()
print(dic_vacio)

# Creadon un diccionario con fromkey()
# Crea las llaves de un diccionario , le asigna "none"
diccionario_numeros = dict.fromkeys(["valor1", "valor2"])
print(diccionario_numeros["valor1"])
print(diccionario_numeros["valor2"])

# Crea las llaves de un diccionario y le asigna un valor
# por defecto
diccionario_numeros = dict.fromkeys(["valor1", "valor2"], "Por Definir")
print(diccionario_numeros)

# Eliminación de variables
del dic_persona1
del dic_persona
del dic_vacio
del diccionario_numeros
