#   Creado por: Osamudio
#   Fecha: 06-Mayo-2025
#   Descripción: Ejemplos de lectura de archivos csv
#                utilizando librería panda

# Declaración de variables
import pandas as pd
from os import system
system("cls")

# Declaración de variables

# Abre el archivo cvs utilizando la libreria panda (pd)
# Nota: los df son dataframe
print("Ejemplo 1 -----------------------------")
df_asegurado = pd.read_csv("00_clases\\archivo\\persona.csv")
# Obtiene los datos de la columna nombre
nombres = df_asegurado["nombre"]
df_asegurado_sort = df_asegurado.sort_values("edad", ascending=False)
print(nombres)
print(df_asegurado)
print(df_asegurado_sort)

# Eliminación de variables
del df_asegurado
