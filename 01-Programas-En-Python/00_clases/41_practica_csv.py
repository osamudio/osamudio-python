#   Creado por: Osamudio
#   Fecha: 25-Mayo-2025
#   Descripción: Practicas para manipular archivos csv

import pandas as pd
from os import system
system("cls")

# Declaración de variables
df_persona = pd.read_csv("00_clases\\archivo\\datos.csv")

# Cambiar el tipo de dato de la columna "edad" a string
df_persona['edad'] = df_persona['edad'].astype(str)
print(df_persona['edad'][0])

# Reemplazar datos de la columna apellido
print("--------------------------------------")
df_persona['apellido'].replace('Camargo', 'Pineda', inplace=True)
print(df_persona)

# Eliminar filas de datos imcompletos
df_persona = df_persona.dropna()
print(df_persona)

# Eliminar filas de datos repetidos
df_persona = df_persona.drop_duplicates()
print(df_persona)

# Eliminar columnas con datos incompletos
# df_persona = df_persona.dropna(axis=1)

# Creando un dataframe nuevo con datos limpios
df_persona.to_csv("00_clases\\archivo\\datos_limpios.csv")

# Eliminación de variables
del df_persona
