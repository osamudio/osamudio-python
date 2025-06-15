#    Creado por: Osamudio
#    Fecha: 05-abril-2025
#    Descripción: Métodos y funciones para iterar
#                 una diccionario

from os import system
system("cls")

# Declaración de variables
dict_persona = dict(nombre="leo", apellido="Campos", edad=47, altura=1.64)
dict_direccion = dict(direccion="Urb Royal", calle=1, casa=20, provincia="PA")

# Iterando una lista con ciclo for
# La variable persona tiene el valor
# del elemento del diccionario
print("--- Inicio -----------------------------")
print("Los datos son:")
for persona in dict_persona.items():
    print(f" - {persona}")

# Iterando más de un diccionario al mismo tiempo
# Nota: Deben tener la misma cantidad de elementos
print("----------------------------------------")
for persona, direccion in zip(dict_persona.items(),
                              dict_direccion.items()):
    print(f"Datos persona es: {persona}")
    print(f"Datos direccion es: {direccion}")

# Forma correcta de recorrer el diccionario con su indice
print("----------------------------------------")
for persona in dict_persona.items():
    llave, valor = persona
    print(f"En la llave {llave} es valor es: {valor}")

# Otra forma de recorrer el diccionario con su indice
print("----------------------------------------")
for direccion in dict_direccion.items():
    llave = direccion[0]
    valor = direccion[1]
    print(f"En la llave {llave} es valor es: {valor}")

# Eliminación de variables
del dict_persona
del dict_direccion
del persona
del direccion
del llave
del valor
