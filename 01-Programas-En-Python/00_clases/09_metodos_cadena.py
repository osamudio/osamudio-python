#   Creado por: Osamudio
#   Fecha : 24-03-2025
#   Descripción : Métodos para manipular cadenas(string)

# Declaración de variables
saludo = "Bienvenido al Mundo de Python con analisis de datos"
despedida = "Nos vemos después, hasta pronto."

# Funcion DIR : devuelve la lista de atributos del objeto
resultado = dir(saludo)
# print(resultado)

# Nota: Los metodos tienen formato Objeto.metodo()

# convierte una cadena a mayúscula (upper)
mayuscula = saludo.upper()
print(mayuscula)

# Convierte una cadena a minúscula (lower)
minuscula = saludo.lower()
print(minuscula)

# Convierte la primera letra en mayúscula (capitalize)
capitalizada = saludo.capitalize()
print(capitalizada)

# Busca una cadena dentro de otra cadena
# Devuelve el indice donde encontro la cadena
# Nota: Si no encuentra la cadena devuelve -1
busqueda = saludo.find("venido")
print(busqueda)

# Busca una cadena dentro de otra cadena
# Devuelve el indice donde encontro la cadena
# Nota: Si no encuentra la cadena devuelve una excepción
indice = saludo.index("venido")
print(indice)

# Valida si la cadena es numerica (isnumeric)
es_numerico = saludo.isnumeric()
print(f"¿La cadena saludo es númerica? : {es_numerico}")

# Valida si la cadena es alfanumerica (isalpha)
cadena = "AAABBBCCCddd"
es_alfanumerico = cadena.isalpha()
print(f"¿La cadena es alfanumerica? : {es_alfanumerico}")

# Devuelve el número de coincidencias de una cadena
# en otra cadena (count)
cadena = "Mi primer archivo de python en python"
contar_coincidencias = cadena.count("python")
print(f"La palabra python aparece : {contar_coincidencias} en la cadena")

# Devuelve la longitud de una cadena
# Nota. len() es una función, no es un método
cadena = "Oscar"
longitud_cadena = len(cadena)
print(f"La longitud de la cadena saludo es : {longitud_cadena}")

# Valida si una cadena comienza con una cadena dada.
# Devuelve True
empieza_con = saludo.startswith("Bienvenido")
print(f"¿Comienza con la palabra Bienvenido? : {empieza_con}")

# Valida si una cadena termina con una cadena dada.
# Devuelve True
termina_con = saludo.endswith("datos")
print(f"¿Comienza con la palabra datos? : {termina_con}")

# Reemplaza una parte de la cadena por otra
nueva_cadena = saludo.replace("Python", "java")
print(nueva_cadena)

# Separa una cadena y la convierte en una lista
saludo = "Bienvenido,al,Mundo,de,Python,con,analisis,de,datos,Python"
lista_cadena = saludo.split(",")
print(lista_cadena)

# Eliminación de variables
del mayuscula
del minuscula
del capitalizada
del busqueda
del indice
del es_numerico
del es_alfanumerico
del cadena
del contar_coincidencias
del longitud_cadena
del empieza_con
del termina_con
del nueva_cadena
del lista_cadena
