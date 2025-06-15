#   Creado por: Osamudio
#   Fecha : 24-03-2025
#   Descripción: Concepto de variables en python

# Declaración de variable nombre_asegurado tipo string(cadena)
nombre_asegurado = "Lionel Samudio"
print(f"El nombre del asegurado es : {nombre_asegurado}")

nombre_asegurado = "Leon Samudio"
print(f"El nombre del asegurado es : {nombre_asegurado}")

# Declaración de la variable edad tipo integer(entero)
edad = 47
print(f"La edad del asegurado es : {edad}")

# Declaración de la variable saldo_cuenta tipo float(flotante)
saldo_cuenta = 15000.40
print(f"El saldo de la cuenta es : {saldo_cuenta}")

# Declaración de la variable seguro_auto
seguro_auto = True

# Declaración de una variable acumuladora
saldo_cuenta = 10
print(f"El saldo de la cuenta es : {saldo_cuenta}")
saldo_cuenta += 15
print(f"El saldo de la cuenta es : {saldo_cuenta}")

# Concatenación de un dato tipo string(cadena)
nombre_completo = "Oscar "
saludo_bienvenida = "Hola " + nombre_completo + ", un gusto saludarte"
print(saludo_bienvenida)

# Concatenación de un dato tipo string(cadena) con f(string)
empresa_trabajo = "GBM"
saludo_bienvenida = f"Bienvenido a {empresa_trabajo}"
print(saludo_bienvenida)

# Busca una valor dentro de un string(cadena)

# Operdores de Pertenencia in o not
print("GBM" in saludo_bienvenida)

# Elimina la declaración de una variable
del saldo_cuenta
del nombre_completo
del saludo_bienvenida
del empresa_trabajo
del seguro_auto
