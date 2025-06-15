#   Creado por: Osamudio
#   Fecha: 25-Mayo-2025
#   Descripción: Ejemplo de programa en python
#                manipulando excepciones

from os import system
system('cls')


def sumar():
    while True:
        print("Introduzca los números por favor")
        # Solicita dos valores y devulve la suma de los mismos
        primero = input("Introduzca el primer número: ")
        segundo = input("Introduzca el segundo número: ")
        # validando errores y convirtiendo a entero
        try:
            # Sumando lo dos números
            valor = int(primero) + int(segundo)
        except Exception as e:
            # Si se genera excepción soliciga ingresar números
            print("Es necesario ingresar números enteros")
            # Nos muestra el tipo del error generado
            print(f"Error: {type(e).__name__}")
        except ZeroDivisionError:
            print("No dividas por Cero")
        else:
            # Sale del ciclo while
            break
        finally:
            print("Se finaliza la función de sumar")
    # Retorno el resultado de la función
    return valor


# Declaración de variables
resultado = sumar()
print(f"La suma es {resultado}")

# Eliminación de variables
del resultado
