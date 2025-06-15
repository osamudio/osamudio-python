#   Creado por: Osamudio
#   Fecha: 25-Mayo-2025
#   Descripción: Ejemplos de uso de librerias gráficas
#                en python

# Se cuenta con un archivo de ingresos de un programador

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from os import system
system("cls")

# Declaración de variables
df_ingresos = pd.read_csv("00_clases\\graficos\\ingresos.csv")

# Definir el titulo del grafico
plt.title("Ingresos del año de un programador")
plt.xlabel("fuente")
plt.ylabel("ingresos")

# Creando un gráfico con los datos del dataframe
sns.barplot(x="fuente", y="ingresos", data=df_ingresos)

# Calcular el total de ingresos
# Nota: Esta salida es en consola
total_ingresos = df_ingresos["ingresos"].sum()
print(f"El total de ingresos es: ${total_ingresos} USD")

# Mostrando el gráfico
plt.show()

# Eliminación de variables
del df_ingresos
