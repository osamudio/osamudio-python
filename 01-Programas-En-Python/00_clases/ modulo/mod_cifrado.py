#   Creado por: Osamudio
#   Fecha: 16-abril-2025
#   Descripción: Ejemplos de modulos en python

# Declaración de funciones
def validar_contrasena(usuario, contrasena):
    if contrasena == 'LeoLeo' and usuario == 'leonsam':
        return print(f"La contraseña del usuario {usuario} es correcta")
    else:
        return print(f"La contraseña del usuario {usuario} es incorrecta")
