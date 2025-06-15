class MiExcepcion(Exception):
    # Creando mi propia exepción
    # Se define el constructor de la clase
    def __init__(self, err):
        print(f"Impresionante, cometiste el siguiente error {err}")

# Vamos a probar la expeción


try:
    # Lanzando mi propia excepción
    raise MiExcepcion("Ohh, me sorprendiste")
except MiExcepcion:
    # Manejando mi propia excepción
    print("Cometiste un error")
