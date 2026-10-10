"""
    Las listas nos permiten almacenar informacion en un lugar,
    la cantidad que desee: ya sean pocos elementos
    o millones de elementos.

    Una lista es una coleccion de items (elementos) que tiene
    un orden particular. Se pueden crear listas que incluyen
    strings, enteros, floats, los nombres o las personas de tu
    familia, etcetera, podemoa almacenar (los tipos de datos
    permitidos en Python) lo que queramos en una lista.

    Son elementos Mutables: Pueden modificarse el tamaño de la lista.

    Se recomienda nombrar una variable del tipo lista en plural.

    En Python, los corchetes [ ] indican una lista, 
    sus elementos se separan por comas.

    Ejemplo:  
"""
bicycles = ['trek', "cannodale", 'redline', 'specialized', 'apache']
print(bicycles)

# ¿Como podemos acceder a los elementos de una lista?

"""
    Las listas son volecciones ordenadas. Se pueden acceder
    aun elemento de una lsta diciendole a Python la
    posicion o indice dele elemnto deseado.

    Para obtener el elemento deseado se debe escribir
    el nombre de la lista, seguido del indice del elemento
    entre corchetes.
"""
print(bicycles[2])
print(bicycles[0], bicycles[1], bicycles[2])

print(bicycles[0].upper())

# Los indices comienza en 0, no en 1
# Ejemplo:
print(bicycles[1]) #cannodale
print(bicycles[3]) #redline

# Accediendo al ultimo elemento de una lista
print(bicycles[-1])
print(bicycles[-2])

# Utilizando valores individuales de una lista
message = f"My first bicycle was a {bicycles[-1].upper()}"
print(message)
