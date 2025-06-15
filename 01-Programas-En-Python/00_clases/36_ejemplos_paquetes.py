#    Creado por: Osamudio
#    Fecha: 27-abril-2025
#    Descripción: Programa para mostrar el concepto
#                 de paquetes en python

# Importa del módulo "os" la función "system()"
from os import system

# Se importa el paquete con todos los modulos
import modulo.paquete
import modulo.paquete.mod_conversiones
import modulo.paquete.mod_matematicas

# Se importa del subpaquete "sub_paquete" del paquete "paquete"
import modulo.paquete.sub_paquete.mod_resta as mod_resta

# Limpia la terminal de salida Output
system("cls")

# Se imprime el path del paquete
print(modulo.paquete.__path__)

# Se llama al modulo "mod_converiones"
# del paquete "paquete"
numero_decimal = 10
modulo.paquete.mod_conversiones.convertir_binario(numero_decimal)

# Se llama al modulo "mod_matemáticas"
# del paquete "paquete"
primer_numero = 10
segundo_numero = 5
modulo.paquete.mod_matematicas.sumar_numeros(primer_numero, segundo_numero)

# Se llama a la funcion "restar_numeros()"
primer_numero = 10
segundo_numero = 5
mod_resta.restar_numeros(primer_numero, segundo_numero)

# Eliminación de variables
del numero_decimal
del primer_numero
del segundo_numero
