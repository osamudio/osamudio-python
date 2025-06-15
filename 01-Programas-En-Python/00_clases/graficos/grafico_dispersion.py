#   Creado por: Osamudio
#   Fecha: 25-Mayo-2025
#   Descripción: Ejemplos de uso de librerias gráficas
#                en python

# Se cuenta con un archivo de tiempo vs dinero

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from os import system
system("cls")

# Declaración de variables
df_tiempo = pd.read_csv("00_clases\\graficos\\tiempo.csv")

# Definir el titulo del grafico
plt.title("Grafico de tiempo vs dinero")
plt.xlabel("tiempo")
plt.ylabel("dinero")

# Creando un gráfico con los datos del dataframe
sns.scatterplot(x="tiempo", y="dinero", data=df_tiempo)

# Mostrando el gráfico
plt.show()

# Eliminación de variables
del df_tiempo
