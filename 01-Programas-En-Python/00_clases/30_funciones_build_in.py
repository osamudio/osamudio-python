#    Creado por: Osamudio
#    Fecha: 08-abril-2025
#    Descripción: Declaración de funciones en python

from os import system
system("cls")

# Declaración de variables
# Encontrando el número mayor de una lista
# tupla o conjunto
lista_numeros = [5, 6, 20, 10, 15, 13]
maximo_numero = max(lista_numeros)
print(f"El número mas álto es : {maximo_numero}")

# Encontramos el número menor de una lista
minimo_numero = min(lista_numeros)
print(f"El número mas bajo es : {minimo_numero}")

# Redondeamos un número con la funcion round()
pi = 3.1415926535
# Redondear a dos decimales
redondear_pi = round(pi, 2)
print(f"El valor de pi redondeado es {redondear_pi}")

# Función bool()
# Ejemplos del resultado de la función bool()
res_vacio = bool()
print(f"El resultado de la funcion bool() es: {res_vacio}")
res_cero = bool(0)
print(f"El resultado de la función bool(0) es: {res_cero}")
res_uno = bool(1)
print(f"El resultado de la función bool(1) es: {res_uno}")
res_none = bool(None)
print((f"El resultado de la función bool(None) es: {res_none}"))
# Tambien se le puede enviar una lista, tupla vacia
res_lista = bool([])
print(f"El resultado de la función bool([]) es: {res_lista}")

# Ejemplo de la función all()
# Devuele True si todos los elementos son verdaderos
res_all = all([10, "leo", 10.5, 3.05])
print(f"El resultado de la función all() es: {res_all}")

# Ejemplo de la función sum()
# Suma los elementos de un iterable
suma = sum(lista_numeros)
print(f"La suma de los números es: {suma}")

# Eliminación de variables
del lista_numeros
del maximo_numero
del minimo_numero
del pi
del redondear_pi
