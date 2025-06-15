#    Creado por: Osamudio
#    Fecha: 12-abril-2025
#    Descripción: Creación de funciones lambda
#                 que son funciones anonimas
#                 no tienen nombre

from os import system
system("cls")


# Declaracion de funciones def


def sumar_numeros(numero_a, numero_b):
    return numero_a + numero_b


# Uso de funciones lambda


# Eleva al cuadrado la lista de números
lista_numeros = [1, 2, 3, 4, 5]
# Nota: X toma el valor de cada elemento de la lista
lista_cuadrados = list(map(lambda x: x**2, lista_numeros))
# Salida: Los cuadrados son: [1, 4, 9, 16, 25]
print(f"Los cuadrados son: {lista_cuadrados}")
# Salida: Suma todos los elementos de la lista
print(f"La suma total es: {sum(lista_cuadrados)}")

# Valida la lista y extrae los numeros pares
# utilizando la función lambda
lista_numeros = [1, 2, 4, 5, 6]
# Si el resultado de la funcion lambda es True lo agrega a la lista
resultado = filter(lambda numero: numero % 2 == 0, lista_numeros)
print(list(resultado))


valor_a = 5
valor_b = 10
suma_total = sumar_numeros(numero_b=valor_b, numero_a=valor_a)
print(f"La suma de {valor_a} + {valor_b} = {suma_total}")

# Eliminación de variables
del valor_a
del valor_b
del suma_total
