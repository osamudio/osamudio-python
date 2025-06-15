#   Creado por: Osamudio
#   Fecha: 17-Mayo-2025
#   Descripción: Cargar la lista de nombres y apellidos
#                en el archivo alumnos.txt

from os import system
system("cls")

# Declaración de variables
nombres = ["Leonidas", "Lucas", "Leonel", "Mario", "Angel"]
apellidos = ["Escudero", "Cruz", "Cedeño", "Ramirez", "Martinez"]

# Creando archivo de manera eficiente con python
with open("00_clases\\archivo\\alumnos.txt", "w", encoding="UTF-8") as archivo:
    archivo.writelines("Cargando información de alumnos en el archivo \n\n")
    [archivo.writelines(f"Nombre: {nombre} \nApellido: {apellido} \n-------\n")
     for nombre, apellido in zip(nombres, apellidos)]

# Eliminación de variables
del nombres
del apellidos
