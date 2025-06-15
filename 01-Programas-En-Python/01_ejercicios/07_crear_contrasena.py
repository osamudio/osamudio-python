#    Creado por: Osamudio
#    Fecha: 11-abril-2025
#    Descripción: Crear una función para generar
#                 contraseñas aleatorias

from os import system
system("cls")


def generar_contrasena_random(numero):
    cadena = "abcdefghij"
    cadena_entero = str(numero)
    # toma solo el primer caracter
    num = int(cadena_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasena = f"{cadena[c1]}{cadena[c2]}{cadena[c3]}{num * 2}"
    return contrasena


number = 90
nueva_contrasena = generar_contrasena_random(number)
print(number)
print(f"La nueva contraseña es: {nueva_contrasena}")
print(type(nueva_contrasena))
