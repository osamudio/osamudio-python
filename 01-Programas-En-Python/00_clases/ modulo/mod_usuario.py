#   Creado por: Osamudio
#   Fecha: 16-abril-2025
#   Descripción: Ejemplos de modulos en python

# Declaración de funciones
def validar_usuario(usuario):
    if usuario == 'leonsam':
        return print(f"El usuario {usuario.lower()} es administrador")
    else:
        return print(f"El usuario {usuario} no es administrador")
