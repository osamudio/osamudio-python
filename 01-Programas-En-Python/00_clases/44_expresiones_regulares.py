#   Creado por: Osamudio
#   Fecha: 01-Junio-2025
#   Descripción: Ejemplo de expresiones regulares

# Modulo de expresiones regulares
import re

from os import system
system("cls")

# Declaración de varibles
parrafo = '''Esta es una prueba de texto para las expresiones regulares
             creado por osamudio el 01 de junio del 2025. 
             espero poder resolver sus dudas con este programa en python,
             utiliza este texto de prueba para realizar Expresiones regulares.
             SR105489756325
             ababbbababab
            '''

# Busca el texto indicado en la cadena "parrafo"
resultado = re.search("osamudio", parrafo)
print(resultado)

# Busca todas las coincidencia del texto en la cadena "parrafo"
resultado = re.findall("expresiones", parrafo, flags=re.IGNORECASE)
print(resultado)

# \d -> busca dígitos numéricos
resultado = re.findall(r"\d", parrafo)
print(resultado)

# \D -> busca todo lo que no sea dígitos numéricos
# resultado = re.findall("\D", parrafo)
# print(resultado)

# \w -> busca caracteres alfanumericos
# a-z,  _ , A-Z, 0-9
resultado = re.findall(r"\w", parrafo)
print(resultado)

# \W -> busca caracteres no alfanumericos
# resultado = re.findall(r"\W", parrafo)
# print(resultado)

# \S -> Busca todo los espacios en blancos
# tabs, salto de línea
resultado = re.findall(r"\s", parrafo)
print(resultado)

# \S -> Busca todo menos espacios en blancos
# tabs, salto de línea
# resultado = re.findall(r"\S", parrafo)
# print(resultado)

# . -> Busca todo menos saltos de línea
resultado = re.findall(r".", parrafo)
print(resultado)

# \n -> Busca saltos de línea
# resultado = re.findall(r"\n", parrafo)
# print(resultado)

# \. -> Cancela caracteres especiales. en este caso
# busca el caracter "."
resultado = re.findall(r"\.", parrafo)
print(resultado)

# Búsqueda de una cadena que contenga el siguiente patron
# busque un número, seguido de un punto "." y un espacio
# en blaco "\n"
resultado = re.findall(r"\d\.\s", parrafo)
print(resultado)

# ^ --> Búsqueda el inicio de una línea una palabra
# Nota: El flags actividado "M" indica multilinea
resultado = re.findall(r"^Esta", parrafo, flags=re.M)
print(resultado)

# $ --> Búsqueda una palabra al final de una línea
# Nota: El flags actividado "M" indica multilinea
resultado = re.findall(r"python,$", parrafo, flags=re.M)
print(resultado)

# {n} --> busca n cantidad de veces el valor de la izquierda
# Nota: El flags actividado "M" indica multilinea
# En este caso busca un numero de 4 cifras
resultado = re.findall(r"\d{4}", parrafo, flags=re.M)
print(resultado)

# {n,m} --> busca por lo menos n cantidad de veces el valor
# hasta m cantidad de valores
# Nota: El flags actividado "M" indica multilinea
# En este caso busca un numero por lo menos 2 hasta 4 cifras
resultado = re.findall(r"\d{1,4}", parrafo, flags=re.M)
print(resultado)

# {n,m} --> busca por lo menos n cantidad de veces el valor
# hasta m cantidad de valores
# Nota: El flags actividado "M" indica multilinea
# En este caso buscar el patrón "ab"
resultado = re.findall(r"(ab){2,4}", parrafo, flags=re.M)
print(resultado)

# {n} --> busca n cantidad de veces el valor
# Nota: El flags actividado "M" indica multilinea
# En este caso buscar el patrón "abab"
resultado = re.findall(r"[ab]{4}", parrafo, flags=re.M)
print(resultado)

# | -->  Busca una cosa oa la otra
# Nota: El flags actividado "M" indica multilinea
# En este caso busca un numero por lo menos 2 hasta 4 cifras
resultado = re.findall(r"\d{1,4}|osamudio", parrafo, flags=re.M)
print(resultado)

# Eliminación de variables
del parrafo
del resultado
