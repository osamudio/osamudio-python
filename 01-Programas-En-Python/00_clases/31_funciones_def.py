#    Creado por: Osamudio
#    Fecha: 11-abril-2025
#    Descripción: Creación de funciones definidas
#                 por el usuario.

from os import system
system("cls")

# Declaración de funciones


def saludar():
    """Imprime un saludo """
    print("Hola estimados. Bienvenidos")


def saludar_nombre(nombre, sexo):
    """Imprime un saludo personalizado con el nombre proporcionado

    Args:
        nombre (str): El nombre de la persona a saludar.
        sexo (str): El sexo de la persona a saludar
    """
    sexo = sexo.lower()
    if sexo == "mujer":
        print(f"{nombre} es una : {sexo}")
    elif sexo == "hombre":
        print(f"{nombre} es un : {sexo}")
    else:
        print(f"{nombre} es un/una {sexo}")


def sumar_numeros(numero_a, numero_b):
    """Suma dos números y devuelve el resultado.

    Args:
        numero_a (int o float): El primer número.
        numero_b (int o float): El segundo número.

    Returns:
        int o float: La suma de numero_a y numero_b.
    """
    resultado = numero_a + numero_b
    return resultado


def restar_numeros(numero_a, numero_b=2):
    """Resta dos números y devuelve el resultado.

    Args:
        numero_a (int o float): El primer número.
        numero_b (int o float): El segundo número.

    Returns:
        int o float: La resta de numero_a y numero_b.
    """
    resultado = numero_a - numero_b
    return resultado


def obtener_info_personal(nombre, edad):
    """Obtiene la información de la persona.

    Args:
        nombre (str): nombre de la persona
        edad (int): edad de la persona

    Returns:
        tuple: Una tupla que contiene el nombre y la edad
    """
    return nombre, edad


saludar()
saludar_nombre("leonel", "HOmbre")
saludar_nombre("Karen", "MujER")
saludar_nombre("Gabriel", "None")

# Devuelve la suma de dos números
primer_numero = 10
segundo_numero = 20.5
resultado = sumar_numeros(primer_numero, segundo_numero)
print(f"La suma de {primer_numero} + {segundo_numero} es: {resultado} ")

# Devuelve la resta de dos números
primer_numero = 10
segundo_numero = 10.5
resultado = restar_numeros(primer_numero, segundo_numero)
print(f"La resta de {primer_numero} + {segundo_numero} es: {resultado} ")

# Devuelve multiples retultados
nombre, edad = obtener_info_personal("Leon", 38)
print(f"El nombre es {nombre} y la edad es {edad} años")


# Eliminación de las variables
del primer_numero
del segundo_numero
del resultado
