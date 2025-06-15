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
# Otro ejemplo de abrir un archivo cvs agregando los
# encabezados personalizados "names"
print("Ejemplo 2 -----------------------------")
df_persona = pd.read_csv("00_clases\\archivo\\persona.csv",
                         names=["name", "lastname", "age", "height"])
print(df_persona)

# Eliminación de variables
del df_persona
