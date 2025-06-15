#    Creado por: Osamudio
#    Fecha: 01-abril-2025
#    Descripción: Se explica el concepto de desempaquetamiento
#                 técnica que permite asignar los elementos de
#                 una estructura de datos a variables

from os import system
system("cls")

# Declaración de variables
set_persona = {"Lionel", "Degracia", 47, 1.64, 200}

# Desempaquetado de un conjunto
v_uno, v_dos, v_tres, v_cuatro, v_cinco = set_persona

print(set_persona)
print("Los datos de la persona son:")
print(f" - Valor 1 : {v_uno}")
print(f" - Valor 2 : {v_dos}")
print(f" - Valor 3 : {v_tres}")
print(f" - Valor 4 : {v_cuatro}")
print(f" - Valor 5 : {v_cinco}")

# Desempaquetado de un conjunto con *resto
v_uno, v_dos, *v_resto, v_ultimo = set_persona
print(set_persona)
print("Los datos de la persona son:")
print(f" - Valor 1 : {v_uno}")
print(f" - Valor 2 : {v_dos}")
print(f" - Resto  : {v_resto}")
print(f" - Valor 4 : {v_ultimo}")

# Eliminación de variables
del v_uno
del v_dos
del v_tres
del v_cuatro
del v_cinco
del v_resto
del v_ultimo
