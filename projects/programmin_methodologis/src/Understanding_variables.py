# Let's try to use variables
message = "This is my first program :), I am very happy"
another_message = "Really, so so so happy"

# Build-in method print 
print(message)
print(another_message)

print(message, another_message)
print(another_message, message)

message = "Hi boys & girls."
print(message)

"""
 Los nombres de las variables deben nombrarsze solo con:
 
 - Letras, numeros y guion bajo.
 - Deben comenzar con una letra o guion bajo.
 - No utilizar espacio para separar palabras en variables (_).
 - No utilizar palabras reservadas en python o el nombre del archivo 
   como nombre de variable.
 - Nombres cortos, pero descriptivos.
 - Letras minusculas (po ahora).
 - En python utilizamos la notacion snake_case para nombrar variables.

 Ejemplos:
 Correcto: message_1
 Incorrecto: 1_message

"""

message = "Hola amigo Python"
print(message)

"""
Traceback: Es un registro de donde el interprete tuvo problemas al intentar
ejecutar el codigo

NameError: Ocurre cuando olvidamos establecer el valor de una variable antes
de utilizarla o cometimos un error (de ortografia) al ingresar el nombre de la variable
"""