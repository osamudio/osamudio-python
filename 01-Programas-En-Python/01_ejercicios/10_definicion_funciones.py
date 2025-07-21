#    Creado por: Osamudio
#    Fecha: 05-Julio-2025
#    Descripción: Ejemplos practicos de funciones
#                 con argumentos

from os import system
system("cls")

# Declaración de funciones


def imprimir_saludo(mensaje=None):
    # Valida si el argumento fue suministrado
    if mensaje is None:
        # Imprime un mensaje genérico
        return print("Hola mundo a todos")
    else:
        # Imprime el mensaje del argumento del usuario
        return print(f"Mensaje del usuario: {mensaje}")


# Declaracion de variables
saludo = "Hola mundo, Soy Osamudio"
# Llamado de la función con argumento
imprimir_saludo(saludo)

# Llamada de la función sin argumento
imprimir_saludo()

# Llamado de función con argumentos palabra clave


# Eliminación de variables
del saludo
