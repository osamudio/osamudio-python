#   Creado por:  Osamudio
#   Fecha : 24-03-2025
#   Descripción: Operadores aritméticos en python

# Ejemplo del operador suma (+)
primer_numero = 10
segundo_numero = 20
suma = primer_numero + segundo_numero
print(f"La suma de los número es : {suma}")

# Ejemplo del operador resta (-)
saldo_cuenta = 200
print(f"El saldo de la cuenta es : {saldo_cuenta}")
retiro_cuenta = 20
print(f"El retiro de la cuenta es : {retiro_cuenta}")
saldo_cuenta = saldo_cuenta - retiro_cuenta
print(f"El saldo actualizado de la cuenta es : {saldo_cuenta}")

# Ejemplo del operador de multiplicación (*)
precio_combo = 12.99
print(f"El precio del combo : {precio_combo}")
cantidad_combo = 3
print(f"La cantidad de combos son : {cantidad_combo}")
costo_total = precio_combo * cantidad_combo
print(f"El precio del combo es: {costo_total}")

# Ejemplo del operador de división (/)
hipoteca_mensual = 472.86
print(f"Monto de hipoteca Mensual : {hipoteca_mensual}")
hipoteca_semanal = hipoteca_mensual / 4
print(f"Monto de hipoteca semanal es : {hipoteca_semanal}")

# Ejemplo del operador de potencia (**)
numero = 5
elevado = 3
potencia = numero ** elevado
print(f"El número {numero} elevado a la potencia de {elevado} es : {potencia}")

# Ejemplo del operador division baja (//)
division_baja = 12 // 5
print(f"El resutado de la división baja : {division_baja}")

# Ejemplo del operador de residuo o mod (%)
numero = 10
divisor = 2
residuo = numero % divisor
print(f"El residuo del {numero} mod entre {divisor} es : {residuo}")

# Función para validar que tipo de dato es
tipo_de_dato = type(hipoteca_semanal)
print(f"El tipo de datos es : {tipo_de_dato}")

# Eliminación de variables
del primer_numero
del segundo_numero
del suma

del saldo_cuenta
del retiro_cuenta

del precio_combo
del cantidad_combo

del hipoteca_mensual
del hipoteca_semanal

del numero
del elevado
del potencia

del division_baja

del residuo
del divisor
del tipo_de_dato
