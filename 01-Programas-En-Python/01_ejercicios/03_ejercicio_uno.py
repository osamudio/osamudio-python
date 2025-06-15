#    Creado por: Osamudio
#    Fecha: 31-marzo-2025
#    Descripción:

from os import system
system("cls")

# Declaración de variables
# Tiempo de duración de cursos en horas
tiempo_minimo = 2.5
tiempo_promedio = 4.0
tiempo_maximo = 7.0
tiempo_oscar = 1.5
porcentaje = 100

# a) Porcentaje de diferencia de duración
# de los cursos vs oscar
#  x  = 1.5
# 100 = 2.5

por_min = porcentaje - round(tiempo_oscar * porcentaje / tiempo_minimo, 1)
print(f"El curso dura un {por_min}% que el mínimo")

por_max = porcentaje - round(tiempo_oscar * porcentaje / tiempo_maximo, 1)
print(f"El curso dura un {por_max}% que el máximo")

por_prom = porcentaje - round(tiempo_oscar * porcentaje / tiempo_promedio, 1)
print(f"El curso dura un {por_prom}% que el promedio")

# b) calculando el porcentaje de tiempo removido
# de los videos cursos vs oscar
#   x  = 4
# 100  = 5
material_promedio = 5
material_oscar = 3.5
por_editado = porcentaje - tiempo_promedio * porcentaje / material_promedio
por_editado = round(por_editado, 2)
print(f"Se remueve un {por_editado}% que el curso promedio")

por_editado = porcentaje - tiempo_oscar * porcentaje / material_oscar
por_editado = round(por_editado, 2)
print(f"Se remueve un {por_editado}% que el curso oscar")

# Mostrando diferencia si los cursos duraran a 10 horas


del tiempo_oscar
del tiempo_maximo
del tiempo_promedio
del tiempo_minimo
del porcentaje
del por_max
del por_min
del por_prom
