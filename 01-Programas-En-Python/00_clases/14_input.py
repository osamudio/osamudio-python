#    Creado por: Osamudio
#    Fecha: 30-marzo-2025
#    Descripción: Solicitando datos al usuario

from os import system
system("cls")

# Declaración de variables
nombre_persona = input("Introduzca su nombre de usuario: ")
edad_persona = input("Introduzca su edad: ")
salario_semanal = input("Introduzca su salario semanal: ")

# Se calcula el salario mensual de la persona
salario_mensual = float(salario_semanal) * 4

# Se imprime la información de la persona
print(f"El nombre del usuario es : {nombre_persona}")
print(f"La edad de la persona es : {edad_persona}")
print(f"El salario mensual es : {salario_mensual}")

# Eliminacion de variables
del nombre_persona
del edad_persona
del salario_semanal
