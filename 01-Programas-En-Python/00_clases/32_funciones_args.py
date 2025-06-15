#    Creado por: Osamudio
#    Fecha: 12-abril-2025
#    Descripción: Creación de funciones definidas
#                 por el usuario con parámetros args

from os import system
system("cls")


def calcular_renta(nombre, *renta):
    """Calcula la renta mensual de la persona.

    Args:
        nombre (str): nombre de la persona
        *renta (int o float): monto de la renta

    Returns:
        nombre (str): nombre de la persona
        int o float: La suma de las rentas
    """
    renta_total = sum(renta)
    return nombre, renta_total


def obtener_informacion(nombre, edad):
    """Obtiene la información de la persona

    Args:
        nombre (str): nombre de la persona
        edad (int): edad de la persona


    Returns:
        nombre (str): nombre de la persona
        edad (str): edad de la persona
    """
    return nombre, edad


def sumar_lista(numero):
    print(type(numero))
    # Método 1 para sumar
    resultado_a = sum([*numero])
    # Método 2 código para sumar
    resultado_b = sum(numero)
    return resultado_a, resultado_b


# Calcula la renta de la persona
nombre, renta_mensual = calcular_renta("Leon", 150, 145.50, 150, 0.50)
print(f"El inquilino {nombre} tiene una renta mensual de {renta_mensual}")

# Muestra la información de la persona
# Nota: estos son keyword parameters , se especifica el parametro que
#       recibira el valor
nombre_persona, edad_persona = obtener_informacion(edad=40, nombre="Leon")
print(f"El inquilino {nombre_persona} tiene una edad de {edad_persona}")

# Suma una lista de numeros
numero_a, numero_b = sumar_lista([150, 145.50, 150, 0.50])
print(f"Método 1, la suma es: {numero_a}")
print(f"Método 2, la suma es: {numero_b}")

# Eliminación de variables
del nombre
del renta_mensual
del nombre_persona
del edad_persona
del numero_a
del numero_b
