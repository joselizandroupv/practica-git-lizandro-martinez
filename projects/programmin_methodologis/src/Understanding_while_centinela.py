"""
While = Sentinel = Centinela

while True:
    actions

Realizar un programa que capture un
importe ingresado por el usuario y
que acumule todos estos importes
en una varable
"""

sum = 0.0
message = """
    Sistema gestor de acumulacion de valores.
    La creatividad esta en tus manos.
    
    En todo momento, si quieres salir del programa
    puedes tipear q, e, quit, exit.
    
    Ingresa unn valor:
"""

while True:
    value_txt = input(message)

    if (
        value_txt == "quit"
        or value_txt == "exit"
        or value_txt == "e"
        or value_txt == "q"
    ):
        break

    value = float(value_txt)
    sum += value  # ESTRUCTURA ACUMULADORA

print(f"Tu total acumulado es: {sum}")
