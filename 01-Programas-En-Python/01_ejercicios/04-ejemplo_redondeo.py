#    Creado por: Osamudio
#    Fecha: 01-abril-2025
#    Descripción: Ejemplos de redondear variables
#                 Flotantes

from os import system
system("cls")

# Declaración de variables
pi = 3.14159

# Ejemplo de redondeo con funcion round()
# Redondeo de pi a dos decimales
redondeo_pi = round(pi, 2)
print(f"El valor de pi es {redondeo_pi}")

# Ejemplo de redondeo con f""

formateado_pi = "{:.2f}".format(pi)
print(f"El valor de pi es {formateado_pi}")

# Usando f-strings (Python 3.6+)
formateado_pi_fstring = f"{pi:.2f}"
print(f"El valor de pi es {formateado_pi_fstring}")
