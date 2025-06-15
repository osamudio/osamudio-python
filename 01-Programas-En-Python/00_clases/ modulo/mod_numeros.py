def identificar_pares(lista_numeros):
    return list(filter(lambda num: num % 2 == 0, lista_numeros))


def identificar_impares(lista_numeros):
    return list(filter(lambda num: num % 2 == 1, lista_numeros))
