# INPUT - SIRVE PARA REALIZAR ENTRADAS DE USUARIOS
"""
METODO BUILD-IN: INPUT

INPUT(ARGUMENTO) - ARGUMENTO (STR): MENSAJE DE TEXTO AL USUARIO

INPUT RETORNA UN STRING
"""

user_welcome = """
        BIENVENIDO AL SISTEMA CREADOR DE NOMBRES COMPLETOS
                    BY CHARLY MERCURY
                
UNIVERSIDAD POLITECNICA DE VICTORIA
"""

firstname = input("Escribe tu Primer Nombre: ")
middlename = input("Escribe tu Segundo Nombre: ")
lastname = input("Escribe tu Apellido (Paterno y Materno)")

fullname = f"{firstname} {middlename} {lastname}"
print(fullname.title())
