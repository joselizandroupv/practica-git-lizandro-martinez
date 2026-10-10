# Trabajndo en listas
print("\n\t Hoy toca trabajar con listas \n".upper())

# Vamos a crear una lista de puros strings con nombres 
magicians = ['harry', 'ron', 'hermione', 'snape']
print(magicians)

print(magicians[0], magicians[1], magicians[2], magicians[3])
# print(magicians[0], magicians[1], magicians[2], magicians[3])

#CICLO FOR
print("\n\t Ciclo For \n".upper())

for magician in magicians: 
    print(magician)

# A esto se le llama looping

# Ahora vamos a imprimri un mensaje para cada mago
print("\n")
for magician in magicians: 
    print(f"{magician.title()} ese fue un gran hechizo.")
    print(f"No puedo esperar a ver el siguiente hechizo, {magician.upper()}")
    print("\n")
print("Gracias a todos. Fue un gran espectaculo.")

print("\n\t Identacion - Indentation \n".upper())
# Identacion
"""
Python usa la identacion para determinar
cuando una linea de codigo esta conectada a la
linea de codigo anterior.

Basicamente, se utiliza 4 espacios en blanco para 
obligarnos a escribir codigo ordenado y estructurado.
"""

# No olvides la identacion, de lo contrario, te saldra un error - Traceback Identation Error 
magicians = ['alice', 'david', 'caroline']
# for magician in magicians:
# print(magician)

print("\n\t Error de Logica - Logic Error - Identation Error \n".upper())
# Error de Logica - Logic Error - Identation Error
for magician in magicians:
    print(magician)
print(f"No puedo esperar a ver el siguiente truco, {magician}.")

# Identacion Inecesaria - Unnecessary Indentation
message = "Hello Python world!"
#    print(message)

# No olvidar los 2 Puntos - SyntaxError: expected ':'
# for magician in magicians
#    print(magician)