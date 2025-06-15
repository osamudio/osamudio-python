#    Creado por: Osamudio
#   Fecha : 24-03-2025
#    Descripción:  Sentencias condicionales (if)
#    Problema: Crear un programa para abrir una cuenta de ahorro
#    Condiciones:
#        Deposito igual o mayor a 15000 genera interes del 4.10%
#        Deposito de 10000 a 14999 genera interes del 3.10%
#        Deposito de 5000 a 9999 genera interes del 2.10%
#        Deposito menor a 5000 genera interes del 1.0%

# Declaración de variables
deposito_cuenta = 30000
if deposito_cuenta >= 15000:
    interes = 4.10
    saldo_cuenta = deposito_cuenta * interes / 100
    print(f"El saldo con {interes} final  es : {saldo_cuenta}")
elif deposito_cuenta >= 10000:
    interes = 3.10
    saldo_cuenta = deposito_cuenta * interes / 100
    print(f"El saldo con {interes} final  es : {saldo_cuenta}")
elif deposito_cuenta >= 5000:
    interes = 2.10
    saldo_cuenta = deposito_cuenta * interes / 100
    print(f"El saldo con {interes} final  es : {saldo_cuenta}")
else:
    interes = 1.0
    saldo_cuenta = deposito_cuenta * interes / 100
    print(f"El saldo con {interes} final  es : {saldo_cuenta}")

# Eliminación de variables
del deposito_cuenta
del interes
del saldo_cuenta
