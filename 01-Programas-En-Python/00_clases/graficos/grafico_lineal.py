#   Creado por: Osamudio
#   Fecha: 25-Mayo-2025
#   Descripción: Ejemplos de uso de librerias gráficas
#                en python

# Se cuenta con un archivo de barcos que pasan por
# el canal de Panamá por fechas


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from os import system
system("cls")

# Declaración de variables
df_barcos = pd.read_csv("00_clases\\graficos\\barcos.csv")

# Creando un gráfico con los datos del dataframe
sns.lineplot(x="fechas", y="barcos", data=df_barcos)

# Marcar un punto en el valor mas alto de paso de barcos
plt.plot("01-09", 17, "o")

# Mostrando el gráfico
plt.show()

# Eliminación de variables
del df_barcos
