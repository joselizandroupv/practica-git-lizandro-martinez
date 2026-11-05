"""
Realizar  un programa en el que el usuario
deba iingresar su Pin de acceso.

Si el PIN es correcto, entonces el mensaje debe decir:
"Ingreso Autorizado"

Si el PIN es incorrecto, entonces el mensaje debe decir:
"PIN Incorrecto, intentos restantes: 0"

Si el usuario ha ingresado mas de 3 veces el
PIN incorrecto, entonces el mensaje debe decir:
"PIN Incorrecto, cuneta bloqueada temporalmente"
"""

PIN_CORRECTO = "1234"  # Pin correcto - constante
MAX_INTENTOS = 3  # Maximo de intentos - constante
intentos = 0  # Contador de intentos - variable
acceso = False  # Variable de control de acceso

while intentos < MAX_INTENTOS:
    line = input("Ingrese su PIN (4 Digitos): ")

    if line == PIN_CORRECTO:
        print("Ingreso Autorizado")
        acceso = True
        break

    intentos += 1  # Contador de intentos
    restantes = MAX_INTENTOS - intentos  # Intentos restantes

    if restantes > 0:
        print(f"PIN Incorrecto, intentos restantes: {restantes}")
    else:
        print("PIN Incorrecto, cuenta bloqueada temporalmente")

if acceso:
    print("Bienvenido a la UPV")
