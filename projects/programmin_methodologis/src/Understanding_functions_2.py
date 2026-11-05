"""
Realizaruna funcion que genere
El nombre completo de una persona.
Dados del primer nombre, segundo nombre y apellido.
La funcion debe retornar el nombre completo.
"""


def create_fullname(first_name: str, last_name: str, middle_name: str = "") -> str:
    """
    Esta función genera el nombre completo de una persona
    con los parámetros dados.
    """
    if middle_name == "":
        full_name = f"{first_name} {last_name}".title()
    else:
        full_name = f"{first_name} {middle_name} {last_name}".title()
    return full_name


# Positional Arguments - Argumentos Posicionales (EL ORDEN IMPORTA)
full_name = create_fullname("Carlos", "Antonio", "Tovar Garcia")
print(full_name)

# Keyword Arguments - Argumentos de Palabra Clave (EL ORDEN NO IMPORTA)
full_name = create_fullname(
    last_name="Tovar Garcia", middle_name="Antonio", first_name="Carlos"
)
print(full_name)

# Positional and Keyword Arguments - Argumentos Posicionales y de Palabra Clave (EL ORDEN IMPORTA)
full_name = create_fullname("Carlos", middle_name="Antonio", last_name="Tovar Garcia")
print(full_name)

# ARGUMENTOS OPCIONALES
full_name = create_fullname("Carlos", "Tovar Garcia")
print(full_name)
