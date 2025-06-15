#    Creado por: Osamudio
#    Fecha: 12-Mayo-2025
#    Descripción: Ejemplos utilizando la libreria Panda
#                 junto con los dataframe (concatenar dos)
#                 dataframe

import pandas as pd
from os import system
system("cls")

# Declaración de variables
# Abre el archivo cvs utilizando la libreria panda (pd)
# Nota: los df son dataframe
df_persona_01 = pd.read_csv("00_clases\\archivo\\persona.csv")
df_cliente_02 = pd.read_csv("00_clases\\archivo\\cliente.csv")

# Concatenando los dos dataframe
# el metodo recibe una lista como parámetro
df_clientes = pd.concat([df_persona_01, df_cliente_02])

# Ordena e imprime el dataframe ordenado
df_clientes_sort = df_clientes.sort_values("edad", ascending=False)
print(df_clientes_sort)

# Accediendo a las 3 primeras filas con head()
primeras_filas = df_clientes_sort.head(3)
print(primeras_filas)

# Accediendo a las 3 últimas filas con tail()
ultimas_filas = df_clientes_sort.tail(3)
print(ultimas_filas)

# Accediendo a la cantidad de filas y columnas con shape
filas_totales, columnas_totales = df_clientes_sort.shape
print(f"Cantidad de filas: {filas_totales}")
print(f"Cantidad de columnas: {columnas_totales}")

# Obteniendo data estadistica del dataframe
# df_informacion = df_clientes_sort.describe()
# print(df_informacion)

# Accediendo a un elemento especifico "edad" del df con loc()
# Fila 2
edad_especifica_loc = df_persona_01.loc[2, "edad"]
print("--------------------------------------------------")
print(f"La edad del elemento 2 es : {edad_especifica_loc}")
print("--------------------------------------------------")
print(df_persona_01)

# Accediendo a un elemento especifico "edad" del df con iloc()
# Fila 2
edad_especifica_iloc = df_persona_01.iloc[2, 2]
print("--------------------------------------------------")
print(f"La edad del elemento 2 es : {edad_especifica_iloc}")
print("--------------------------------------------------")
print(df_persona_01)

# Accediendo a todas las filas de una columna con slicing
# con loc , columna "apellido"
todos_apellido_loc = df_persona_01.loc[:, "apellido"]
print("--------------------------------------------------")
print(todos_apellido_loc)
print("--------------------------------------------------")

# Accediendo a todas las filas de una columna con slicing
# con iloc , columna "apellido"
todos_apellido_iloc = df_persona_01.iloc[:, 1]
print("--------------------------------------------------")
print(todos_apellido_iloc)
print("--------------------------------------------------")

# Accediendo a todas las columnas de una fila con slicing
# con loc, fila 1
toda_fila_loc = df_persona_01.loc[1, :]
print("--------------------------------------------------")
print(toda_fila_loc)
print("--------------------------------------------------")


# Accediendo a todas las columnas de una fila con slicing
# con loc, fila 1
toda_fila_iloc = df_persona_01.loc[1, :]
print("--------------------------------------------------")
print(toda_fila_iloc)
print("--------------------------------------------------")

# Accediendo a filas con edad mayor igual a 25
# utilizando slicing con loc
df = pd.read_csv("00_clases\\archivo\\persona.csv")
filas_edad_condicional_loc = df.loc[df["edad"] >= 25, :]
print("--------------------------------------------------")
print(filas_edad_condicional_loc)
print("--------------------------------------------------")

# Eliminación de variables
del df_persona_01
del df_cliente_02
del df_clientes
del df_clientes_sort
del primeras_filas
del filas_totales
del columnas_totales
# del df_informacion
del edad_especifica_loc
del edad_especifica_iloc
del todos_apellido_loc
del todos_apellido_iloc
del toda_fila_loc
del toda_fila_iloc
del filas_edad_condicional_loc
