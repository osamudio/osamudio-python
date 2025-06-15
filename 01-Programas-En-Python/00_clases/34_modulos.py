#   Creado por: Osamudio
#   Fecha: 23-Abril-2025
#   Descripción: Programa para explicar el uso de
#                módulos en python

# Importando del módulo: mod_usuario.py
import modulo.mod_usuario

# Importando del módulo: mod_usuario.py con un alias
import modulo.mod_cifrado as cifrado

# Importando del módulo modulos.mod_numeros solamente
# las funciones identificar_pares y identificar_impares
from modulo.mod_numeros import identificar_pares, identificar_impares

# Importando del módulo "os" la función "system()"
from os import system
system("cls")

# llamando a la función del módulo: mod_usuario
login_usuario = "leonsam"
modulo.mod_usuario.validar_usuario(login_usuario)
login_usuario = "leonel"
modulo.mod_usuario.validar_usuario(login_usuario)

# Otra forma es utilizando un alias
login_usuario = "leonsam"
cifrado.validar_contrasena(contrasena="LeoLeo", usuario=login_usuario)

# Otra manera solo importando la función validar_pares
lista_num = [1, 3, 4, 2, 10, 8, 12]
lista_pares = identificar_pares(lista_num)
lista_impares = identificar_impares(lista_num)
print(f"Lista Original: {lista_num}")
print(f"Lista de pares: {lista_pares}")
print(f"Lista de impares: {lista_impares}")

print(type(modulo.mod_usuario))
print(cifrado.__name__)

# Para ver las propiedades y métodos del namespace
print(dir(cifrado))
