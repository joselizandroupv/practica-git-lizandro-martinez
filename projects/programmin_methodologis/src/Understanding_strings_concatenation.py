# Combinacion o Concatenacion de STRING
first_name = "charly"
last_name = "mercury"
full_name = first_name + " " + last_name
print(full_name.title())

# Nativo
print(
    "Hola".upper(),
    "Carlos" + " " + "Tovar",
    first_name.title() + " " + last_name.title(),
)
message = "Hola, " + full_name.title() + "!"
print(message)

# WHITE SPACES

"""
    White Space se refiere a cualquier String
    (caracter) que no se imprime, es decir,
    un espacio (" "), tabuladores (\t) y 
    finales de linea (\n).

    LOs White Spaces se utilizan comunmente para
    organizar las salidas d etextos a usuario
    de tal manera que sea mas amigable de leer
    o ver para los usuarios.
"""
print("Python")
print("\tPython")
print("\t\tPython")
print("Lenguajes: \n Python \n C \n JavaScript")

# F-String

famous_person = "charly mercury"
message = f"{famous_person} una ves dijo: Python es amor."
print(message)

qoute = "Python is in the air"
message_2 = f"{famous_person} una ves dijo {qoute}"
print(message_2)
