"""
TUPLAS

Las tuplas son listas de elementos que no cambian de tamaño.
Las tuplas son listas inmutables

Se utilizan los parentesis () para definir una tupla

Ejemplo:

-Si tenemos un rectangulo (largo, ancho) que siempre va
a tener cierto tamaño, podemos asegurar que sus dimensiones
no van a cambiar si colocamos sus valores en una tupla.

"""

print("TUPLAS")

dimensions = (200, 50)  # 200 de largo x 50 de ancho
print(dimensions)

print("\nAcceder a elementos de una tupla")

# Vamos a imprimir elementos de una tupla
# Se realiza de la misma manera que  con una lista,
# utilizando el indice del elemento que queremos imprimir

print(dimensions[0])  # Imprime el primer elemento de la tupla
print(dimensions[1])  # Imprime el segundo elemento de la tupla

print("\nMetodos de una Tupla")
print(dir(dimensions))  # Imprime los metodos disponibles para una tupla

# Vamos a modificar el valor de una lista
# names = ["Carlos", "Charly", "Juan", "Wendy"]
# print(names)
# names[0] = "Mercury"
# print(names)

# Esto NO SE PUEDE HACER EN UNA TUPLA
# dimensions[0] = 500  # Esto no se puede hacer, ya que las tuplas son inmutables

# Looping through a tuple
for dimension in dimensions:
    print(dimension)

"""
    No podemos modificar una tupla,
    lo que si podemos hacer es cambiar 
    la asiganacion de una variable que 
    almacena una tupla.
"""

print("\nCambiando la asignacion de la variable dimensions")
dimensions = (500, 1000, 20)  # Cambiamos la asignacion de la variable dimensions
print("Tupla Reasignada:", dimensions)  # Imprime la nueva tupla

# METODOS DE DEMAS ESTRUCTURAS DE DATOS
# Lista
# dimensions_2 = (200, 50)  # 200 de largo x 50 de ancho
# print("\nMetodos de una Lista")
# print(dir(dimensions_2))  # Imprime los metodos disponibles para una tupla

# String
# name = "Charly"
# print("\nMetodos de una Cadena de Texto")
# print(dir(name))  # Imprime los metodos disponibles para una cadena de texto

# Age
# age = 20
# print("\nMetodos de un Entero")
# print(dir(age))  # Imprime los metodos disponibles para un entero

# TIPOS DE DATOS BOOLEANOS

answer = True
print(answer)

# print("\nMetodos de un Booleano")
# print(dir(answer))  # Imprime los metodos disponibles para un booleano
