#   Creado por: Osamudio
#   Fecha: 26-abril-2025
#   Descripción: Ejemplo de importación de un módulo
#                en un directorio atras a la ubicación
#                de este programa en python

# Importando módulos del mismo directorio
import modulo.mod_cifrado as cifrado

# Importando el módulo sys
import sys

# Importo del módulo "os" la función "system()"
from os import system
system("cls")

# Agregar una ruta de módulos al path
agr_path = "d:\\00-Python-Dalto-2025\\01-Programas-En-Python\\00_clases\\mod\\"
sys.path.append(agr_path)

# Importa el modulo "mod_prueba" la función "saludar_usuario()"
from mod.mod_prueba import saludar_usuario

# Declaración de variables
login = "leonsam"
cifrado.validar_contrasena(login, "LeoLeo")

# Para saber donde se encuentran ubicados los módulos
print(sys.path)

# Devulve una tupla con todas los modulos definidos en python
# print(sys.builtin_module_names)

# Uso de la función saludar_usuario del módulo mod_prueba
saludar_usuario(login)

# Eliminación de variables
del login
del agr_path
