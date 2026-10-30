# Tarea realizar un programa q capture los importes introducidos por un usuario.-
# El programa debe:
#   contabilzar cuantos importes a introducido el usuario.
#   acumular los importes que a introducido el usuario
#   establecer el maximo y el minimo de los valores introducidos
#   calcular el promedio de los valores introducidos
#   despues de que el usuario decida terminar el programa se deben mostrar estos datos

"""
Contador de numeros ingresados
el acumhado de los numeros ingresadis
promedio
minimo y mayor valor i gresado
"""

# ==============================================================
# PROGRAMA DE TAREA

# DECLARAR VARIABLES

# ACUMULADOR DE MONTOS INGRESADOS
sum_total = 0.0
# CONTADOR DE LOS VALORES INTRODUCIDOS
counter = 0
# MAXIMO VALOR
max_value = 0.0
# MINIMO VALOR
min_value = 0.0

# INSTRUCCION
message = """
    Programa de Tarea de Acumulacion de Valores
    
    Si quieres salir del programa puedes teclear:
                    q, e, quit, exit
                    
        Ingresa un Valor: 
"""
# CICLO
while True:
    # ESTO AYUDA A QUE EL MENSAJE QUITE LOS ERRORES DE:
    # MAYUSCULAS O MINUSCULAS
    value_txt = input(message).strip().lower()
    # CONDICION POR SI QUIERE SALIR
    if (
        value_txt == "quit"
        or value_txt == "exit"
        or value_txt == "e"
        or value_txt == "q"
    ):
        break
    value = float(value_txt)
    sum_total += value  # SE SUMAN LOS VALORES INTRODUCIDOS
    counter += 1  # SE SUMA DE 1 EN 1 PARA EL CONTADOR

    if counter == 1:
        max_value = value
        min_value = value
    else:
        min_value = min(min_value, value)
        max_value = max(max_value, value)

        """
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
        """

print("\n DATOS ")

if counter > 0:
    average = sum_total / counter
    print(f"Contador de numeros ingresados: {counter}")
    print(f"Total acumulado: {sum_total}")
    print(f"Promedio: {round(average, 2)}")
    print(f"Valor minimo ingresado: {min_value}")
    print(f"Valor mayor ingresado: {max_value}")
else:
    print("No se ingresó ningun valor.")
