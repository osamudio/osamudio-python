#   Creado por: Osamudio
#   Fecha: 25-Mayo-2025
#   Descripción: Ejemplos de uso de librerias gráficas
#                en python

# Se cuenta con un archivo de categoria vs valor

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from os import system
system("cls")

# Declaración de variables
df_tiempo = pd.read_csv("00_clases\\graficos\\bigotes.csv")

# Definir el titulo del grafico
plt.title("Grafico de categoria vs valor")
plt.xlabel("categoria")
plt.ylabel("valor")

# Creando un gráfico con los datos del dataframe
sns.boxplot(x="categoria", y="valor", data=df_tiempo)

# Mostrando el gráfico
plt.show()

# Eliminación de variables
del df_tiempo
